from RageComm import RageComm
import numpy as np
from matplotlib import pyplot as plt
import socket, struct, re as rege

IP = "169.254.70.191"
SIGLEN = 1024
PORT = 7


def toComplx(text):
    f = text.split(',')
    return int(f[0]) + 1j * int(f[1])


def SetUpDma(ip):
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)
        s.connect((ip, PORT))
        s.send(b'r')
        data = s.recv(1024)
        return data
    except OSError as e:
        print(f"SetUpDma: socket error: {e}")
        return b""
    finally:
        if s is not None:
            try:
                s.shutdown(2)
            except Exception:
                pass
            s.close()


def getDmaLen(ip):
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3.0)
        s.connect((ip, PORT))
        s.send(b's')
        raw = s.recv(1024)
        if not raw:
            print("getDmaLen: no data received")
            return 0
        data = int.from_bytes(raw, byteorder='little', signed=False)
        if data <= 0:
            print(f"getDmaLen: invalid DMA length {data}")
        return data
    except OSError as e:
        print(f"getDmaLen: socket error: {e}")
        return 0
    finally:
        if s is not None:
            try:
                s.shutdown(2)
            except Exception:
                pass
            s.close()


def Read(ip, dma_length, navg, keep_i_only):
    navg = int(navg)
    if dma_length <= 0:
        print("Read: dma_length <= 0, skipping")
        return [], True
    if navg < 1:
        print("Read: navg < 1, forcing to 1")
        navg = 1

    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.0)
        s.connect((ip, PORT))

        chunks, got = [], 0
        while got < dma_length:
            s.send(b'd')
            ch = s.recv(min(dma_length - got, 8192))
            if not ch:
                print("Read: socket closed before full DMA length")
                break
            chunks.append(ch)
            got += len(ch)

        if got < dma_length:
            print(f"Read: expected {dma_length} bytes, got {got}")
            if not chunks:
                return [], True

        raw = b''.join(chunks)

        if len(raw) % 2 != 0:
            print(f"Read: odd raw length {len(raw)}, truncating last byte")
            raw = raw[:-1]

        if not raw:
            print("Read: empty raw buffer")
            return [], True

        u = np.frombuffer(raw, dtype='<u2').copy()
        u ^= 0x8000
        sig = u.view('<i2').astype(np.int32)
        sig //= 16

        if keep_i_only and sig.size >= 2:
            sig = sig[::2]

        if sig.size == 0:
            print("Read: no samples after processing")
            return [], True

        if navg > sig.size:
            print(f"Read: navg ({navg}) > samples ({sig.size}), forcing navg=1")
            navg = 1

        segs = np.array_split(sig, navg)
        return segs, False

    except OSError as e:
        print(f"Read: socket error: {e}")
        return [], True
    except Exception as e:
        print(f"Read: unexpected error: {e}")
        return [], True
    finally:
        if s is not None:
            try:
                s.shutdown(2)
            except Exception:
                pass
            s.close()


def plotSpectrum(segments, center, band, navg, plot_avg, plot_samples, fs):
    if not segments:
        print("plotSpectrum: no segments to process")
        return

    adcFullScale = 2048.0
    f_ref = None
    sum_db = None
    fs = float(fs)
    if fs <= 0:
        print(f"plotSpectrum: invalid fs={fs}")
        return

    avgCount = 0
    for seg in segments:
        signal = np.asarray(seg, dtype=float)
        N = len(signal)
        if N == 0:
            print("plotSpectrum: empty segment, skipping")
            continue

        signal = signal - np.mean(signal)

        win = np.hamming(N)
        scale = np.mean(win) if np.mean(win) != 0 else 1.0

        try:
            fft = np.fft.fft(signal * win / adcFullScale / scale * 2) / N
        except Exception as e:
            print(f"plotSpectrum: FFT error: {e}")
            continue

        fft_abs = np.abs(fft[:N // 2])
        fft_abs[fft_abs == 0.0] = 1e-5
        fft_abs_dB = 20 * np.log10(fft_abs)

        f_MHz = np.linspace(0.0, (fs / 2), N // 2, endpoint=False)
        f_ref = f_MHz

        if sum_db is None:
            sum_db = fft_abs_dB.copy()
        else:
            sum_db += fft_abs_dB
        avgCount += 1

        if plot_samples:
            plt.plot(f_MHz, fft_abs_dB)
            if (center is not None) and (band is not None):
                min_freq = center - (band / 2)
                max_freq = center + (band / 2)
                plt.axvspan(min_freq, max_freq, alpha=0.1)
            plt.grid(True)
            plt.xlim(0, fs / 2.0)
            plt.xlabel("Frequency [MHz]")
            plt.ylabel("Amplitude [dBFS]")
            plt.show()

    if sum_db is None or f_ref is None:
        print("plotSpectrum: no valid data after processing segments")
        return

    avg_dB = sum_db / avgCount

    k = int(np.argmax(avg_dB))
    print(f"Max Value: {avg_dB[k]:.3f} dBFS at {f_ref[k]:.6f} MHz")

    if (center is not None) and (band is not None):
        min_freq = center - (band / 2)
        max_freq = center + (band / 2)
        print(f"CF_OUT(MHz) = {center:.3f}")

        sel = (f_ref >= min_freq) & (f_ref <= max_freq)
        if not np.any(sel):
            print("plotSpectrum: no points in selected band")
        else:
            band_signal = avg_dB[sel]
            band_power = 10 * np.log10(np.sum(10 ** (band_signal / 10)) + 1e-30)
            print(f"BP_OUT(dBFS) = {band_power:.3f}")

    if plot_avg:
        plt.plot(f_ref, avg_dB)
        if (center is not None) and (band is not None):
            plt.axvspan(min_freq, max_freq, alpha=0.3)
        plt.grid(True)
        plt.title("Average")
        plt.xlim(0, fs / 2.0)
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Amplitude [dBFS]")
        plt.show()


def initHw(com, antenna, iscomplx):
    resp = com.consoleIo('seq off')
    if antenna is not None:
        resp = com.consoleIo(f'rxport {antenna}')
    if iscomplx:
        resp = com.consoleIo('rxdata iq')
    else:
        resp = com.consoleIo('rxdata real')


def noiseInit(navg, com):
    port_map = {
        '0x0000': int(navg) * ["0x000"],
        '0x0100': int(navg) * ["0x100"],
        '0x0110': int(navg) * ["0x110"],
        '0x0200': int(navg) * ["0x200"],
        '0x0220': int(navg) * ["0x220"],
        '0x0400': int(navg) * ["0x400"],
        '0x0440': int(navg) * ["0x440"],
        '0x0800': int(navg) * ["0x800"],
        '0x0880': int(navg) * ["0x880"]
    }
    if navg < 1:
        print("noiseInit: navg < 1, forcing to 1")
        navg = 1

    com.consoleIo(f'wr reg 0x05 {int(navg)}')
    com.consoleIo(f'wr reg 0x0A {int(navg) * 4}')
    com.consoleIo('wr reg 0x19 0x0020')
    resp = com.consoleIo('rd table 3')

    key = None
    if ':' in resp:
        key = resp.split(':', 1)[1].strip()
    else:
        print(f"noiseInit: unexpected rd table 3 response: {resp}")

    if key not in port_map:
        print(f"noiseInit: key {key} not in port_map, defaulting to 0x0000")
        key = '0x0000'

    com.consoleIo(f'wr table 3 {" ".join(port_map[key])}')
    com.consoleIo("wr table 0x10 1 5 9 13 17 21 25 29 33 37 41 45 49 53 57 61")
    com.consoleIo("wr table 0x11 2 6 10 14 18 22 26 30 34 38 42 46 50 54 58 62")
    com.consoleIo("wr table 0x12 3 7 11 15 19 23 27 31 35 39 43 47 51 55 59 63")
    com.consoleIo("wr table 0x13 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64")
    com.consoleIo('sos')
    com.close()


def main(argv):
    loop = False
    infile = None
    outfile = None
    do_fft = False
    cf = None
    bw = None
    data = False
    navg = 1
    fs = 150.0
    iscomplx = False
    plot = False
    plotSam = False
    port_name = None
    antenna = None

    argn = 1
    while argn < len(argv):
        arg = argv[argn]
        argn += 1

        if rege.fullmatch(r'-[cC][oO][mM]\d+', arg):
            port_name = arg.lstrip('-')
        elif arg == "-loop":
            loop = True
        elif arg == "-i":
            infile = argv[argn]
            argn += 1
        elif arg == "-o":
            outfile = argv[argn]
            argn += 1
        elif arg == "-a":
            try:
                antenna = int(argv[argn])
            except (ValueError, IndexError):
                print("Invalid or missing antenna after -a")
                return
            argn += 1
        elif arg == "-fft":
            do_fft = True
        elif arg == "-data":
            data = True
        elif arg == "-plot":
            plot = True
        elif arg == "-plotSam":
            plotSam = True
        elif arg == "-navg":
            try:
                navg = int(float(argv[argn]))
            except (ValueError, IndexError):
                print("Invalid or missing value after -navg")
                return
            argn += 1
        elif arg == "-cf":
            try:
                cf = float(argv[argn])
            except (ValueError, IndexError):
                print("Invalid or missing value after -cf")
                return
            argn += 1
        elif arg == "-iq":
            iscomplx = True
        elif arg == "-bw":
            try:
                bw = float(argv[argn])
            except (ValueError, IndexError):
                print("Invalid or missing value after -bw")
                return
            argn += 1
        elif arg == "-fs":
            try:
                fs = float(argv[argn])
            except (ValueError, IndexError):
                print("Invalid or missing value after -fs")
                return
            argn += 1
        elif arg in ("-h", "-help"):
            print("-a <antenna>   RX antenna 1-8")
            print("-i/-o <file>  input/output")
            print("-fft          spectrum")
            print("-data         time plots")
            print("-cf/-bw <MHz> center/bandwidth")
            print("-navg <N>     average segments (1..10)")
            print("-plot         plot average")
            print("-plotSam      plot each segment")
            print("-COMxx        choose serial port")
            return
        else:
            print(f"Unknown option {arg}")
            return

    if navg < 1:
        print("main: navg < 1, forcing to 1")
        navg = 1

    if fs <= 0:
        print("main: invalid fs, forcing to 150 MHz")
        fs = 150.0

    # LC-only default. Rev C (fs==150) ignores antenna selection.
    if antenna is None:
        antenna = 1

    try:
        com = RageComm()
        if infile is None:
            ports = com.getPorts()
            if not ports:
                print("No COM port found.")
                return
            if port_name and (port_name not in ports):
                print(f"{port_name} not found. Available: {ports}")
                return

            com.setPortName(port_name or ports[0])
            try:
                com.open()
            except Exception as e:
                print(f"Failed to open COM port: {e}")
                return

            firstTime = True

        try:
            while True:
                if infile is None:
                    initHw(com, antenna, iscomplx)
                    if firstTime:
                        firstTime = False
                        noiseInit(navg, com)
                    SetUpDma(IP)
                    dma_len = getDmaLen(IP)

                    usehalf = (fs == 75)
                    segs, had_err = Read(IP, dma_len, navg, usehalf)
                    if had_err:
                        print("main: Read() failed, skipping this iteration")
                        if not loop:
                            break
                        continue
                else:
                    v = []
                    try:
                        with open(infile, "r") as fp:
                            for line in fp:
                                s = line.strip()
                                if s:
                                    try:
                                        v.append(int(s.split(',')[0]))
                                    except ValueError:
                                        pass
                    except OSError as e:
                        print(f"Error reading input file {infile}: {e}")
                        return

                    if not v:
                        print("main: no samples read from file")
                        return

                    segs = np.array_split(np.array(v, dtype=np.int32),
                                          max(1, navg))

                if outfile:
                    try:
                        with open(outfile, "w") as fp:
                            for seg in segs:
                                for val in seg:
                                    fp.write(f"{int(val)}\n")
                    except OSError as e:
                        print(f"Error writing output file {outfile}: {e}")
                        # non-fatal; continue

                if data:
                    for seg in segs:
                        plt.plot(seg)
                    plt.xlabel("Sample #")
                    plt.ylabel("Amplitude")
                    plt.grid(True)
                    plt.show()

                if do_fft:
                    chz = cf if cf is not None else None
                    bhz = bw if bw is not None else None
                    plotSpectrum(segs, chz, bhz, navg, plot, plotSam, fs)

                if not loop:
                    break

        except KeyboardInterrupt:
            print("Interrupted by user.")

    finally:
        try:
            com.close()
        except Exception:
            pass


if __name__ == "__main__":
    import sys
    main(sys.argv)

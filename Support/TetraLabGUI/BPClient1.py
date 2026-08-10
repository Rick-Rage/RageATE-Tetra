from RageComm import RageComm  # unused now but fine to keep
import numpy as np
from matplotlib import pyplot as plt
import re
import socket
import struct
from pathlib import Path

IP = "169.254.70.191"
port = 7


def toComplx(text):
    f = text.split(',')
    return int(f[0]) + 1j * int(f[1])


def SetUpDma(s):
    try:
        s.sendall(b'r')
        data = s.recv(1024)
        if not data:
            print("SetUpDma: no data received")
            return ""
        return data.decode(errors='ignore')
    except OSError as e:
        print(f"SetUpDma: socket error: {e}")
        return ""


def getDmaLen(s):
    try:
        s.sendall(b's')
        raw = s.recv(1024)
        if not raw:
            print("getDmaLen: no data received")
            return 0
        dma_len = int.from_bytes(raw, byteorder='little', signed=False)
        if dma_len <= 0:
            print(f"getDmaLen: invalid DMA length {dma_len}")
        return dma_len
    except OSError as e:
        print(f"getDmaLen: socket error: {e}")
        return 0


def Read(s, dma_length, assume_offset_binary=True, keep_i_only=True):
    if dma_length <= 0:
        print("Read: dma_length <= 0, skipping")
        return np.asarray([], dtype=np.int32)

    chunks, got = [], 0
    try:
        while got < dma_length:
            s.sendall(b'd')
            ch = s.recv(min(dma_length - got, 8192))
            if not ch:
                print("Read: socket closed before full DMA length")
                break
            chunks.append(ch)
            got += len(ch)
    except OSError as e:
        print(f"Read: socket error during recv: {e}")
        return np.asarray([], dtype=np.int32)

    recv = b''.join(chunks)
    if len(recv) == 0:
        print("Read: empty buffer")
        return np.asarray([], dtype=np.int32)

    if len(recv) % 2 != 0:
        print(f"Read: odd length {len(recv)}, truncating last byte")
        recv = recv[:-1]

    try:
        u = np.frombuffer(recv, dtype='<u2')
    except ValueError as e:
        print(f"Read: frombuffer error: {e}")
        return np.asarray([], dtype=np.int32)

    if assume_offset_binary:
        u = (u ^ 0x8000)
    x = u.view('<i2').astype(np.int32)
    x //= 16

    if keep_i_only and x.size >= 2:
        x = x[::2]

    if x.size == 0:
        print("Read: no samples after processing")
    return x


def plotSignal(signal, iscomplx):
    if signal is None or signal.size == 0:
        print("plotSignal: empty signal")
        return
    plt.ylabel("Amplitude")
    plt.xlabel("Sample #")
    if iscomplx:
        plt.plot(np.real(signal), label="Real")
        plt.plot(np.imag(signal), label="Imag")
        plt.legend()
    else:
        plt.plot(signal)
    plt.ylim(-2048, 2048)
    plt.grid(True)
    plt.show()


def plotSpectrum(signal, center, band, plot, fs):
    if signal is None or signal.size == 0:
        print("plotSpectrum: empty signal")
        return
    if center is None or band is None:
        print("plotSpectrum: center/band not provided")
        return
    try:
        fs = float(fs)
    except Exception:
        print("plotSpectrum: invalid fs, skipping")
        return
    if fs <= 0:
        print("plotSpectrum: fs <= 0, skipping")
        return

    N = len(signal)
    if N < 2:
        print("plotSpectrum: too few samples")
        return

    min_freq = center - (band / 2)
    max_freq = center + (band / 2)

    f = np.linspace(0, fs / 2, N // 2)  # Frequency axis in MHz

    signal = signal.astype(float)
    signal = signal - np.mean(signal)

    win = np.hamming(N)
    scale = np.mean(win) if np.mean(win) != 0 else 1.0

    try:
        fft = np.fft.fft(signal * win / 2048 / scale * 2) / N
    except Exception as e:
        print(f"plotSpectrum: FFT error: {e}")
        return

    fft_abs = np.abs(fft[:N // 2])
    fft_abs[fft_abs == 0.0] = 1e-5
    fft_abs_dB = 20 * np.log10(fft_abs)

    if fft_abs_dB.size == 0 or f.size == 0:
        print("plotSpectrum: empty FFT result")
        return

    max_ix = int(np.argmax(fft_abs_dB))
    print(f"Max Value: {fft_abs_dB[max_ix]:.3f} dBFS at {f[max_ix]:.6f} MHz")
    print(f"CF_OUT(MHz) = {center:.3f}")

    band_sel = (f >= min_freq) & (f <= max_freq)
    if not np.any(band_sel):
        print("plotSpectrum: no bins in band")
    else:
        band_signal = fft_abs_dB[band_sel]
        band_power = 10 * np.log10(np.sum(10 ** (band_signal / 10)) + 1e-30)
        print(f"BP_OUT(dBFS) = {band_power:.3f}")

    if plot:
        plt.ylabel("Amplitude [dBFS]")
        plt.xlabel("Frequency [MHz]")
        plt.plot(f, fft_abs_dB)
        plt.axvspan(min_freq, max_freq, color='red', alpha=0.5)
        plt.grid(True)
        plt.show()


def ReadFpgaRegister(com, address):
    resp = com.consoleIo('rd reg 0x%x' % address)
    fields = resp.split()
    if len(fields) < 2:
        print(f"ReadFpgaRegister: unexpected response: {resp}")
        return 0
    try:
        return int(fields[1][2:], 16)
    except Exception as e:
        print(f"ReadFpgaRegister: parse error: {e}, resp={resp}")
        return 0


def initHw(com, antenna, iscomplx):
    if antenna is None:
        antenna = 1
    try:
        ch = antenna >> 1
        port_sel = (antenna & 1) ^ 1
        _ = ch  # currently unused
        _ = port_sel
    except Exception:
        pass

    fpga_control2 = ReadFpgaRegister(com, int("70", 16))

    if antenna:
        _ = com.consoleIo(f'rxport {antenna}')

    if iscomplx:
        _ = com.consoleIo('wr reg 0x70 0x%04x' % (fpga_control2 & int("FEFF", 16)))
        _ = com.consoleIo('wr table 0x10 1')
        _ = com.consoleIo('wr table 0x11 0')
        _ = com.consoleIo('wr table 0x12 0')
        _ = com.consoleIo('wr table 0x13 0')
    else:
        _ = com.consoleIo('wr reg 0x70 0x%04x' % (fpga_control2 | int("0100", 16)))
        _ = com.consoleIo('wr table 0x10 1')
        _ = com.consoleIo('wr table 0x11 2')
        _ = com.consoleIo('wr table 0x12 3')
        _ = com.consoleIo('wr table 0x13 4')

    _ = com.consoleIo('wr reg 0x02 0x0400')
    _ = com.consoleIo('wr reg 0x03 0x0000')
    _ = com.consoleIo('wr reg 0x04 1032')
    _ = com.consoleIo('wr reg 0x05 4')
    _ = com.consoleIo('wr reg 0x06 10')
    _ = com.consoleIo('wr reg 0x08 256')
    _ = com.consoleIo('wr reg 0x09 51')
    _ = com.consoleIo('wr reg 0x0A 4')
    _ = com.consoleIo('wr reg 0x0E 8000')
    _ = com.consoleIo('wr reg 0x0F 0x5555')
    _ = com.consoleIo('wr reg 0x10 0x0055')
    _ = com.consoleIo('wr reg 0x11 0xAAAA')
    _ = com.consoleIo('wr reg 0x12 0x00AA')
    _ = com.consoleIo('wr reg 0x1A 0x0000')
    _ = com.consoleIo('wr reg 0x1B 0x0000')
    _ = com.consoleIo('wr reg 0x17 0x0300')
    _ = com.consoleIo('wr reg 0x18 0x0000')


def ping_once(comm_port, antenna, iscomplx, fs):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    try:
        s.connect((IP, port))
    except OSError as e:
        print(f"ping_once: failed to connect to {IP}:{port}: {e}")
        s.close()
        return
    try:
        _ = SetUpDma(s)
        dma_length = getDmaLen(s)
        if dma_length <= 0:
            print("ping_once: invalid DMA length")
            return
        # In "ping" mode we want visibility into both:
        # - raw 16-bit words reported by the server (dma_length / 2)
        # - post-processed sample count (optionally I-only decimation)
        keep_i_only = (float(fs) == 75.0) and (not iscomplx)
        sig = Read(s, dma_length, assume_offset_binary=True, keep_i_only=keep_i_only)
        raw_words = dma_length // 2
        if sig.size > 0:
            print(f"Server Status Ok. Received {sig.size} samples")
        else:
            print("Server status not OK (no samples).")
    finally:
        try:
            s.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        s.close()


def main():
    import sys
    loop = False
    input_file = None
    output_file = None
    fft = False
    cf = None
    bw = None
    fs = 150
    data = False
    help_flag = False
    antenna = 1
    iscomplx = False
    comm_port = None
    do_plot = False
    do_ping = False

    argn = 1
    args = sys.argv
    while argn < len(args):
        raw = args[argn]
        argn += 1
        if re.fullmatch(r'-[cC][oO][mM]\d+', raw):
            comm_port = raw.lstrip('-')
            continue
        a = raw.lower()
        try:
            if a == "-loop":
                loop = True
            elif a == "-i":
                input_file = args[argn]
                argn += 1
            elif a == "-o":
                output_file = args[argn]
                argn += 1
            elif a == "-a":
                antenna = int(args[argn])
                argn += 1
            elif a == "-fft":
                fft = True
            elif a == "-data":
                data = True
            elif a == "-cf":
                cf = float(args[argn])
                argn += 1
            elif a == "-bw":
                bw = float(args[argn])
                argn += 1
            elif a == "-fs":
                fs = float(args[argn])
                argn += 1
            elif a in ("-h", "-help"):
                help_flag = True
            elif a == "-iq":
                iscomplx = True
            elif a == "-plot":
                do_plot = True
            elif a == "-ping":
                do_ping = True
            else:
                print(f"Unknown option {raw}")
                return
        except IndexError:
            print(f"Missing value after {raw}")
            return
        except ValueError:
            print(f"Invalid numeric value after {raw}")
            return

    if help_flag:
        print("-a <antenna>   RX antenna 1-8")
        print("-loop          Run in loop mode")
        print("-i/-o          Input/Output file")
        print("-data          Plot time-domain")
        print("-fft           Plot spectrum")
        print("-iq            Use I/Q data (kept for file input)")
        print("-cf/-bw        Center/Bandwidth (MHz) for BP")
        print("-fs            Sampling frequency (MHz), default 75")
        print("-COMxx         Set COM port explicitly (not needed for socket)")
        print("-plot          Show plots")
        print("-ping          Quick connectivity check (socket read one frame)")
        return

    if do_ping:
        ping_once(comm_port, antenna, iscomplx, fs)
        return

    if fs <= 0:
        print("main: invalid fs, forcing to 150")
        fs = 150

    if not data and not fft and not output_file:
        data = True

    while True:
        if not input_file:
            com = RageComm()
            try:
                ports = com.getPorts()
            except Exception as e:
                print(f"Error getting COM ports: {e}")
                return

            if not ports:
                print("No COM port found.")
                return

            if comm_port:
                if comm_port not in ports:
                    print(f"{comm_port} not found. Available: {ports}")
                    return
            else:
                comm_port = ports[0]

            try:
                com.setPortName(comm_port)
                com.open()
            except Exception as e:
                print(f"Failed to open COM port {comm_port}: {e}")
                try:
                    com.close()
                except Exception:
                    pass
                return

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5.0)
            try:
                try:
                    s.connect((IP, port))
                except OSError as e:
                    print(f"Failed to connect to {IP}:{port}: {e}")
                    return

                initHw(com, antenna, iscomplx)
                _ = SetUpDma(s)
                dma_length = getDmaLen(s)
                print(dma_length)

                useHalf = (fs == 75)
                signal = Read(s, dma_length, True, useHalf)
            finally:
                try:
                    s.shutdown(socket.SHUT_RDWR)
                except OSError:
                    pass
                s.close()
                try:
                    com.close()
                except Exception:
                    pass

            iscomplx = False
        else:
            vals = []
            iscomplx_file = None
            try:
                with open(input_file, "r") as fp:
                    for line in fp:
                        fields = line.strip().split(',')
                        if not fields or not fields[0]:
                            continue
                        if len(fields) == 1:
                            if iscomplx_file is True:
                                print("Improper input file (mixed real/complex)")
                                break
                            try:
                                vals.append(int(fields[0]))
                            except ValueError:
                                print(f"Skipping bad line: {line.strip()}")
                                continue
                            iscomplx_file = False
                        elif len(fields) == 2:
                            if iscomplx_file is False:
                                print("Improper input file (mixed real/complex)")
                                break
                            try:
                                vals.append(int(fields[0]) + 1j * int(fields[1]))
                            except ValueError:
                                print(f"Skipping bad line: {line.strip()}")
                                continue
                            iscomplx_file = True
            except OSError as e:
                print(f"Error reading input file {input_file}: {e}")
                return

            iscomplx = bool(iscomplx_file)
            signal = np.asarray(vals)

        if signal is None or signal.size == 0:
            print("No samples captured.")
            if not loop:
                break
            continue

        if output_file:
            p = Path(output_file)
            try:
                p.parent.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"Error creating output directory: {e}")
            output_str = str(p)
            try:
                with open(output_str, "w", newline="") as fp:
                    if iscomplx:
                        for r, i in zip(np.real(signal), np.imag(signal)):
                            fp.write(f"{int(r)},{int(i)}\n")
                    else:
                        for v in signal:
                            fp.write(f"{int(v)}\n")
            except OSError as e:
                print(f"Error writing output file {output_str}: {e}")

        if data and do_plot:
            plotSignal(signal, iscomplx)
        if fft:
            if cf is None or bw is None:
                print("Provide -cf and -bw (MHz) for BP readout.")
            plotSpectrum(signal, cf, bw, do_plot, fs)

        if not loop:
            break


if __name__ == "__main__":
    main()

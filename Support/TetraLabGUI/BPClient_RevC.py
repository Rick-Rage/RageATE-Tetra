from RageComm import RageComm
import time
import numpy as np
from matplotlib import pyplot as plt
import math
import socket
import struct

SIGNAL_LEN = 2048  # Number of signal samples
IP = "169.254.70.191"  # Server IP Address


def SetUpDma(s):
    """Sets up the DMA and checks server status."""
    s.send(b'r')
    data = s.recv(1024)
    return data.decode()  # Simplified decoding


def getDmaLen(s):
    """Fetches the DMA length from the server."""
    s.send(b's')
    data = s.recv(1024)
    return int.from_bytes(data, byteorder='little')


def Read(s,dma_length):
    signal = []
    iscomplx = False
    port = 7
    bytes_recv = 0
    write = b"d"
    chunks = []
    while bytes_recv < dma_length:
        s.send(write)
        chunk = s.recv(min(dma_length - bytes_recv, 8192))
        chunks.append(chunk)
        # print(chunk.decode('utf-16'))
        bytes_recv = bytes_recv + len(chunk)
    # print("You received {} bytes".format(bytes_recv))
    recvdata = b''.join(chunks)
    count = len(recvdata)//2
    signal  = struct.unpack('h'*count, recvdata)
    signal = np.array(signal)

    with open('outputhex9_13.txt', 'w') as file_obj:
        for word in signal:
            # print("%04x\n"%(word & 0xFFFF))
            file_obj.write("{0:6d},{1:016b},{1:016b},{1:04x}\n".format(word, word & 0xFFFF))

    # Convert from offset binary to two's complement
    signal = signal & 0xFFFF
    signal = signal ^ (1 << 15)
    # Convert to signed
    signal = np.array([int.from_bytes(int(word).to_bytes(2, 'little'), 'little', signed=True) for word in signal])
    signal = signal //16
    return signal


def plotSpectrum(signal, center, band, plot):
    """
    Plots the spectrum of the signal within the specified center frequency and bandwidth.
    """
    Fs = 150e6  # Sampling frequency
    min_freq = center - (band / 2)
    max_freq = center + (band / 2)
    f = np.linspace(0, Fs / 2, len(signal) // 2) / 1e6  # Frequency axis in MHz

    # DC offset correction
    signal = signal - np.mean(signal)

    # Apply Hamming window and compute FFT
    N = len(signal)
    
    win = np.hamming(N)
    scale = np.mean(win)
    fft = np.fft.fft(signal * win  /2048/ scale * 2 ) / N
    fft_abs = np.absolute(fft)
    fft_abs_dB = 20 * np.log10(np.abs(fft[:N // 2]))

    # Identify max value and frequency
    max_ix = np.argmax(fft_abs_dB)
    print(f"Max Value: {fft_abs_dB[max_ix]:.3f} dBFS at {f[max_ix]:.6f} MHz")
    print(f"CF_OUT(MHz) = {center / 1e6:.3f}")

    # Band-limited signal for power calculation
    band_signal = fft_abs_dB[(f >= min_freq / 1e6) & (f <= max_freq / 1e6)]
    band_power = 10 * np.log10(np.sum(10 ** (band_signal / 10)))
    print(f"BP_OUT(dBFS) = {band_power:.3f}")

    if (plot): 
        # Plot spectrum
        plt.ylabel("Amplitude [dBFS]")
        plt.xlabel("Frequency [MHz]")
        plt.plot(f, fft_abs_dB)
        plt.axvspan(min_freq / 1e6, max_freq / 1e6, color='red', alpha=0.5)
        plt.grid(True)
        plt.xlim(0, 75)
        plt.show()


def plotSignal(signal):
    """Plots the time-domain signal."""
    plt.ylabel("Amplitude")
    plt.xlabel("Sample #")
    plt.plot(signal)
    plt.ylim(-2048, 2048)
    plt.show()

"""
python BPlient.py -ping
Server Status Ok. Received 60000 samples
"""
def main(argv):
    """
    Main entry point for the program, handles command-line arguments,
    processes signals, and performs FFT or raw data plotting.
    """
    loop = False
    input_file = None
    output_file = None
    fft = False
    cf = None
    bw = None
    data = False
    ping = False
    plot = False
    # Parse command-line arguments
    argn = 1
    while argn < len(argv):
        arg = argv[argn]
        argn += 1
        if arg == "-loop":
            loop = True
        elif arg == "-i":
            input_file = argv[argn]
            argn += 1
        elif arg == "-o":
            output_file = argv[argn]
            argn += 1
        elif arg == "-fft":
            fft = True
        elif arg == "-data":
            data = True
        elif arg == '-cf':
            cf = float(argv[argn]) * 1e6
            argn += 1
        elif arg == '-bw':
            bw = float(argv[argn]) * 1e6
            argn += 1
        elif arg == "-plot":
            plot = True
        elif arg == '-ping':
            ping = True
        elif arg in ("-h", "-help"):
            print("Usage:")
            print("-loop          Run in loop mode")
            print("-i <filename>  Input file for signal data")
            print("-o <filename>  Output file to save signal data")
            print("-fft           Plot the spectrum")
            print("-data          Plot raw signal data")
            print("-cf <value>    Center frequency in MHz")
            print("-bw <value>    Bandwidth in MHz")
            print("-ping          Check server connectivity")
            return


    while True:
        if input_file is None:  # Live mode
            port = 7
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((IP, port))
                status = SetUpDma(s)
                try:
                    clean_status = status.split("b")[1].split('\\')[0].split("'")[1]
                except IndexError:
                    clean_status = status.strip()

                if ping:
                    if clean_status == 'OK':
                        dma_length = getDmaLen(s)
                        print(f'Server Status Ok. Received {dma_length // 2} samples')
                    else:
                        print("Server status not OK")
                    s.shutdown(2)
                    s.close()
                    break  # exit ping after response
                else:
                    if "OK" in clean_status:
                        print("Server Status OK. DMA configured!")
                        dma_length = getDmaLen(s)
                        if dma_length // 2 == SIGNAL_LEN:
                            signal = Read(s, dma_length)
                        else:
                            print(f"DMA length mismatch. Expected: {SIGNAL_LEN}, Received: {dma_length // 2}")
                            return
                    else:
                        print("Server Status not OK.")
                s.shutdown(2)
                s.close()
            except OSError as e:
                print(f"Socket error: {e}")
                break

        if output_file:
            with open(output_file, "w") as fp:
                for sample in signal:
                    fp.write(f"{sample}\n")

        if fft:
            if cf is None or bw is None:
                print("Center frequency and bandwidth must be provided for FFT.")
                break
            plotSpectrum(signal, cf, bw, plot)

        if data:
            plotSignal(signal)

        if not loop:
            break


if __name__ == '__main__':
    import sys
    main(sys.argv)

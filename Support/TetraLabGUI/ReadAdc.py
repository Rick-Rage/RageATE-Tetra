from RageComm import RageComm
import numpy as np
from matplotlib import pyplot as plt
import re


def toComplx(text):
    """Converts a string of comma-separated real and imaginary values to a complex number."""
    fields = text.split(',')
    return int(fields[0]) + 1j * int(fields[1])


def readAdc(com):
    """
    Reads ADC data via RageComm and determines if the data is complex.
    Returns:
        - intData: Signal data as a NumPy array
        - iscomplx: Boolean indicating if the data is complex
    """
    resp = com.consoleIo('rd data')
    strData = resp.split()
    if ',' in strData[0]:
        intData = np.array([toComplx(s) for s in strData])
        iscomplx = True
    else:
        intData = np.array([int(s) for s in strData])
        iscomplx = False
    return intData, iscomplx


def plotSignal(signal, iscomplx):
    """
    Plots the time-domain signal.
    If the signal is complex, plots real and imaginary parts separately.
    """
    plt.ylabel("Amplitude")
    plt.xlabel("Sample #")
    if iscomplx:
        plt.plot(np.real(signal), label="Real")
        plt.plot(np.imag(signal), label="Imaginary")
        plt.legend()
    else:
        plt.plot(signal)
    plt.ylim(-2048, 2048)
    plt.show()

def plotSpectrum(signal, iscomplx, Fs, band, center, plot):
    """
    Plots the frequency spectrum of the signal.
    Adjusts the sampling frequency if the signal is complex.
    """
    N = len(signal)
    print(N)
    if iscomplx:
        Fs = 18.75
        f = np.linspace(-Fs / 2, Fs / 2, N)  # Frequency axis in MHz
    else:
        f = np.linspace(0, Fs / 2, N // 2)  # Frequency axis in MHz

    # Remove DC offset
    signal = signal - np.mean(signal)

    # Apply Hamming window and compute FFT
    win = np.hamming(N)
    scale = np.mean(win)
    #fft = np.fft.fft(signal * win / 2048 / scale * 2 ) / N
    fft = np.fft.fft(signal / 2048) / N
    if iscomplx:
        fft_abs = np.fft.fftshift(np.abs(fft))
    else:
        fft_abs = np.abs(fft[:N//2])
    fft_abs[fft_abs == 0.0] = 1e-5
    fft_abs_dB = 20 * np.log10(fft_abs)

    max_index = np.argmax(fft_abs_dB)
    max_value = fft_abs_dB[max_index]
    max_freq = f[max_index]

    print(f"Max Value: {max_value:.3f} dBFS at {max_freq:.3f} MHz")

    if band and center:
        min_freq = center - (band/2)
        max_freq = center + (band/2)

        band = band * 1e6
        center = center * 1e6

        # old code
        print(f"CF_OUT(MHz) = {center / 1e6:.3f}")

        # Band-limited signal for power calculation
        band_signal = fft_abs_dB[(f >= min_freq) & (f <= max_freq)]
        band_sum = np.sum(10 ** (band_signal / 10))
        band_power = 10 * np.log10(band_sum)
        print(f"BP_OUT(dBFS) = {band_power:.3f}")

        if plot:
            # Plot spectrum
            plt.ylabel("Amplitude [dBFS]")
            plt.xlabel("Frequency [MHz]")
            plt.plot(f, fft_abs_dB)
            plt.axvspan(min_freq, max_freq, color='red', alpha=0.5)
            plt.grid(True)
            #plt.xlim(0, Fs / 2 // 1e6)
            plt.show()
    else:
        if plot:
            plt.ylabel("Amplitude [dBFS]")
            plt.xlabel("Frequency [MHz]")
            plt.plot(f, fft_abs_dB)
            plt.grid(True)
            plt.show()

def ReadFpgaRegister(com, address):
    """Reads the value of a register from the FPGA."""
    resp = com.consoleIo(f'rd reg 0x{address:x}')
    fields = resp.split()
    return int(fields[1][2:], 16)


def initHw(com, antenna, iscomplx):
    """
    Initializes the hardware with the specified antenna and I/Q data configuration.
    Configures FPGA registers for operation.
    """
    
    resp = com.consoleIo('seq off')
    resp = com.consoleIo(f'rxport {antenna}')
    if iscomplx:
        resp = com.consoleIo(f'rxdata iq')
    else:
        resp = com.consoleIo(f'rxdata real')

    com.consoleIo('sos')  # Save configuration


def main():
    """
    Main function to parse command-line arguments and execute operations.
    Supports signal plotting, spectrum plotting, and hardware initialization.
    """
    import sys
    loop = False
    input_file = None
    output_file = None
    fft = False
    cf = False
    bw = False
    fs = 75
    data = False
    help_flag = False
    antenna = 1
    iscomplx = False
    comm_port = None
    plot = False

    # Parse command-line arguments
    argn = 1
    args = sys.argv
    while argn < len(sys.argv):
        arg = args[argn]
        argn += 1

        if re.fullmatch(r'-[cC][oO][mM]\d+', arg):
            comm_port = arg.lstrip('-')
            continue
        arg = arg.lower()
        if arg == "-loop":
            loop = True
        elif arg == "-i":
            input_file = args[argn]
            argn += 1
        elif arg == "-o":
            output_file = args[argn]
            argn += 1
        elif arg == "-a":
            antenna = int(args[argn])
            argn += 1
        elif arg == "-fft":
            fft = True
        elif arg== '-cf':
            cf = float(sys.argv[argn])
            argn += 1
        elif arg == '-bw':
            bw = float(sys.argv[argn])
            argn += 1
        elif arg == '-fs':
            fs = float(sys.argv[argn])
            argn += 1
        elif arg == "-h" or arg == "-help":
            help_flag = True
        elif arg == "-iq":
            iscomplx = True
        elif arg == "-plot":
            plot = True
        else:
            print("Unknown option %s" % arg)
            return

    if help_flag:
        print("-a <antenna>   RX antenna 1-8")
        print("-loop          Run in loop mode")
        print("-i <filename>  Input file for signal data")
        print("-o <filename>  Output file to save signal data")
        print("-fft           Plot spectrum of the signal")
        print("-iq            Use I/Q data")
        print("-cf            Center frequency in MHz")
        print("-bw            Bandwidth in MHz")
        print("-fs            Sampling frequency in MHz")
        print("-COMxx         Set com port to COMxx")
        print("-plot          Plot the FFT if -fft")
        return

    while True:
        if not input_file:
            com = RageComm()
            ports = com.getPorts()
            if not ports:
                print("No COM port found.")
                break
            if comm_port:
                if not comm_port in ports:
                    print(f"{comm_port} not found.")
                    break
            else:
                comm_port = ports[0]
            com.setPortName(comm_port)
            com.open()
            initHw(com, antenna, iscomplx)
            signal, iscomplx = readAdc(com)

            com.close()
        else:
            signal = []
            iscomplx = None
            with open(input_file, "r") as fp:
                for line in fp:
                    fields = line.split(',')
                    if len(fields) == 1:
                        if iscomplx == True:
                            print("Improper input file")
                            break
                        signal.append(int(fields[0]))
                        iscomplx = False
                    elif len(fields) == 2:
                        if iscomplx == False:
                            print("Improper input file")
                            break
                        signal.append(int(fields[0]) + 1j * int(fields[1]))
                        iscomplx = True

        if output_file:
            with open(output_file, "w") as fp:
                if iscomplx:
                    for r, i in zip(np.real(signal), np.imag(signal)):
                        fp.write(f"{r},{i}\n")
                else:
                    for sample in signal:
                        fp.write(f"{sample}\n")

        if fft:
            plotSpectrum(signal, iscomplx, fs, bw, cf, plot)

        elif plot:
            plotSignal(signal, iscomplx)

        if not loop:
            break


if __name__ == "__main__":
    main()

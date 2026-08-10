import socket
import struct
import numpy as np
from matplotlib import pyplot as plt
import ant_rx_tx_map as a_p


# --- Configuration Functions ---

def ReadIni(path):
    """Reads an .ini configuration file and parses it into a dictionary."""
    ini = {}
    current_section = {}
    folder = ''
    with open(path, "r") as fp:
        for line in fp:
            # Remove comments
            if ';' in line:
                line = line.split(';')[0]
            line = line.strip()
            if not line:
                continue
            # Handle section headers
            if line.startswith('[') and line.endswith(']'):
                if current_section:
                    ini[folder] = current_section
                folder = line[1:-1]
                current_section = {}
            elif '=' in line:
                key, value = map(str.strip, line.split('=', 1))
                current_section[key] = value
        if current_section:
            ini[folder] = current_section
    return ini


# Load configuration file
config = ReadIni('bandpower.ini')
ip = "169.254.70.191"


# --- Utility Functions ---

def toComplx(signal):
    """Converts interleaved I/Q data into a complex signal array."""
    signal_chunks = np.array_split(signal, 42)
    signal_data = []
    for chunk in signal_chunks:
        I = chunk[::2]
        Q = chunk[1::2]
        signal_data.append(Q + 1j * I)  # Swap I/Q to match field test plot
    return signal_data


def isOpen(ip):
    """Checks if a TCP socket connection can be established to the given IP."""
    port = 7
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.shutdown(2)
            return True
    except:
        return False


def SetUpDma(ip):
    """Sets up the DMA connection by sending an initialization command."""
    port = 7
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send(b'r')
        data = s.recv(1024)
        print(data)


def getDmaLen(ip):
    """Retrieves the DMA length from the server."""
    port = 7
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send(b's')
        data = s.recv(1024)
    dma_len = int.from_bytes(data, byteorder='little')
    print(f"DMA Length: {dma_len}")
    return dma_len


def Read(ip, dma_length):
    """
    Reads signal data from the server, converts it to two's complement format,
    and splits it into complex I/Q data.
    """
    port = 7
    signal = []
    write = b"d"
    chunks = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        bytes_recv = 0
        while bytes_recv < dma_length:
            s.send(write)
            chunk = s.recv(min(dma_length - bytes_recv, 86016))
            chunks.append(chunk)
            bytes_recv += len(chunk)
    recvdata = b''.join(chunks)
    count = len(recvdata) // 2
    signal = np.array(struct.unpack('h' * count, recvdata))

    # Convert from offset binary to two's complement
    signal = signal & 0xFFFF
    signal = signal ^ (1 << 15)
    signal = np.array([int.from_bytes(int(word).to_bytes(2, 'little'), 'little', signed=True) for word in signal])
    signal = signal // 16
    return toComplx(signal), True


# --- Plotting Functions ---

def plotSpectrum(signal, Fs, iscomplx, plot):
    """
    Plots the spectrum for each antenna pairing and evaluates against frequency
    and power limits.
    """
    if iscomplx:
        Fs = Fs / 8

    results_dict = {}
    for i, antenna_signal in enumerate(signal):
        N = len(antenna_signal)
        pxx = plt.psd(antenna_signal, NFFT=N, Fs=Fs, window=np.hamming(N))
        fft, freqs = pxx
        max_idx = np.argmax(fft)
        max_freq = freqs[max_idx]
        max_value_db = 10 * np.log10(fft[max_idx])

        # Evaluate frequency range and power limits
        ant = f"Tx_{a_p.decoderRingFieldTest[i][1]} Rx_{a_p.decoderRingFieldTest[i][3]}"
        results_dict[ant] = {
            "Frequency": "Passed" if float(config["FreqRange"]["lower"]) <= max_freq / 1e6 <= float(config["FreqRange"]["upper"]) else "Failed",
            "Power": "Passed" if float(config["PowerLimits"]["lower"]) <= max_value_db <= float(config["PowerLimits"]["upper"]) else "Failed"
        }

        print(f"{ant}: {results_dict[ant]}")
        print(f"Max Value: {max_value_db:.3f} dBFS at {max_freq / 1e6:.3f} MHz")

        # Plot if enabled
        if plot:
            plt.title(f"Antenna Pairing {i + 1}/42 Tx {a_p.decoderRingFieldTest[i][1]} Rx {a_p.decoderRingFieldTest[i][3]}")
            plt.ylim(-80, 10)
            plt.yticks(np.arange(-80,10, step=5))
            plt.xticks(np.arange(-10e6,10e6, step=1e6))
            plt.grid(True)
            plt.show()


def plotDynamicSignal(signal):
    """Plots the real and imaginary parts of dynamic signals for all antenna pairings."""
    for i, sig in enumerate(signal):
        plt.plot(np.real(sig), label="Real")
        plt.plot(np.imag(sig), label="Imaginary")
        plt.ylabel("Amplitude")
        plt.xlabel("Sample #")
        plt.title(f"Antenna Pairing {i + 1}/42 Tx {a_p.decoderRingFieldTest[i][1]} Rx {a_p.decoderRingFieldTest[i][3]}")
        plt.ylim(-2048, 2048)
        plt.legend()
        plt.grid(True)
        plt.show()


# --- Main Function ---

def main():
    import sys
    loop = False
    input_file = None
    output_file = None
    fft = False
    data = False
    help_flag = False
    plot = False

    # Parse command-line arguments
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == "-loop":
            loop = True
        elif arg == "-i":
            input_file = args[i + 1]
        elif arg == "-o":
            output_file = args[i + 1]
        elif arg == "-fft":
            fft = True
        elif arg == "-data":
            data = True
        elif arg == "-plot":
            plot = True
        elif arg in ("-h", "-help"):
            help_flag = True

    if help_flag:
        print("-loop          Run in loop mode")
        print("-i <filename>  Input file for signal data")
        print("-o <filename>  Output file to save signal data")
        print("-fft           Plot spectrum of the signal")
        print("-data          Plot dynamic signals")
        print("-plot          Enable plots")
        return

    while True:
        if input_file is None:
            SetUpDma(ip)
            dma_length = getDmaLen(ip)
            signal, iscomplx = Read(ip, dma_length)
        else:
            with open(input_file, "r") as fp:
                signal = [int(value) for line in fp for value in line.strip().split(',')]
                signal = toComplx(signal)
                iscomplx = True

        if output_file:
            with open(output_file, "w") as fp:
                for y in signal:
                    for re, im in zip(np.real(y), np.imag(y)):
                        fp.write(f"{int(re)},{int(im)}\n")

        if data:
            plotDynamicSignal(signal)
        if fft:
            plotSpectrum(signal, 150e6, iscomplx, plot)

        if not loop:
            break


if __name__ == "__main__":
    main()

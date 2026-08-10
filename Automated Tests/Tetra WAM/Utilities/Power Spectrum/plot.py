import numpy as np
import matplotlib.pyplot as plt

def band_power(center_frequency,band,path):
    """Calculate the power within a frequency band.

    Parameters
    ----------
    center_frequency : int
        band center in hertz
    band : int
        bandwidth in hertz.
    path : string
        absolute path to the csv file containing the signal
    """
    x = []
    y = []

    with open (path) as fh:
    	for line in fh:
            data = line.split(',')

            x_value = data[0]
            y_value = data[1]
            x.append(x_value.strip())
            y.append(float(y_value.strip()))

    newdata = np.array(y)
    new_signal = []

    f_naught = center_frequency
    spread = band
    min = f_naught - spread/2
    max = f_naught + spread/2

    for i,j in zip(x,newdata):
        if(float(i) > min):
            if (float(i) < max):

                new_signal.append((np.power(10,j/10)))
    #
    new_signal= np.array(new_signal)
    #
    band_power = 20*np.log10(np.sum(new_signal)/len(new_signal))
    return band_power

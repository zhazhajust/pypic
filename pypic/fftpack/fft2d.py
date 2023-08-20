import numpy as np

def fft(field_array, dt, axis = 0):
    freqs_data = np.fft.rfft(field_array, axis = axis)
    freqs = np.fft.rfftfreq(field_array.shape[axis], d = dt)
    return freqs, freqs_data
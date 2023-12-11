import numpy as np
from scipy.constants import c
from scipy.fft import rfft, rfftfreq

def fft1d(data, dt, axis = -1):
    xf = rfft(data, axis = axis)
    freq = rfftfreq(data.shape[axis], d = dt)
    return freq, xf

def wave_front(xf, idx):
    amplitude = np.abs(xf[:, :, idx])
    phase = np.unwrap(np.unwrap(np.angle(xf)[:, :, idx], axis = 0), axis = 1)
    return amplitude, phase

def reconstract(data, dt, freq_limit = 30e12):
    freq, xf = fft1d(data, dt)
    xf_line = np.sum(np.sum(np.abs(xf), axis = 0), axis = 0)[freq < freq_limit]
    # xf_line = np.abs(xf[50, 50, :][freq < freq_limit])
    # plt.plot(freq[freq < 30e12], xf_line)
    idx = np.argmax(xf_line)
    print(f"Peak frequency: {freq[idx]/1e12:.3f} [THz]")
    amplitude, phase = wave_front(xf, idx)
    return amplitude, phase
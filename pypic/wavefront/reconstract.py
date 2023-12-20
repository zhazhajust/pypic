import numpy as np
from scipy.constants import c
from scipy.fft import rfft, rfftfreq
from skimage.restoration import unwrap_phase

def fft1d(data, dt, axis = -1):
    xf = rfft(data, axis = axis)
    freq = rfftfreq(data.shape[axis], d = dt)
    return freq, xf

def wave_front(xf, idx):
    amplitude = np.abs(xf[:, :, idx])
    # phase = np.unwrap(np.unwrap(np.angle(xf)[:, :, idx], axis = 0), axis = 1)
    phase = unwrap_phase(np.angle(xf)[:, :, idx])
    return amplitude, phase

def reconstract(data, dt, freq_limit = 30e12):
    freq, xf = fft1d(data, dt)

    # xf_line = np.sum(np.sum(np.abs(xf), axis = 0), axis = 0)[freq < freq_limit]
    # # xf_line = np.abs(xf[50, 50, :][freq < freq_limit])
    # # plt.plot(freq[freq < 30e12], xf_line)
    # idx = np.argmax(xf_line)

    array_3d = np.abs(xf[:, :, freq < freq_limit])
    # Find the indices of the maximum value in the entire array
    max_index = np.unravel_index(np.argmax(array_3d), array_3d.shape)
    idx = max_index[2]

    print(f"Peak frequency: {freq[idx]/1e12:.3f} [THz]")
    amplitude, phase = wave_front(xf, idx)
    return amplitude, phase

def reconstract2d(data, dt, freq_limit = 30e12):
    xf = rfft(data, axis = 0)
    freq = rfftfreq(data.shape[0], d = dt)

    # max_idx = np.argmax(np.sum(np.abs(xf[freq < freq_limit]), axis = 1))
    # print(freq[max_idx]/1e12, "THz")

    array_2d = np.abs(xf[:, freq < freq_limit])
    # Find the indices of the maximum value in the entire array
    max_index = np.unravel_index(np.argmax(array_2d), array_2d.shape)
    max_idx = max_index[1]

    amp_line = np.abs(xf[max_idx])
    angle_line = np.unwrap(np.angle(xf[max_idx]))
    return amp_line, angle_line

###################################
############# Axis 0 ##############
###################################

import numpy as np
from skimage.restoration import unwrap_phase

def wavefront(Ey, idx):
    xf = np.fft.rfft(Ey, axis = 0)[idx, ...]
    amplitude, phase = np.abs(xf), unwrap_phase(np.angle(xf))
    return amplitude, phase
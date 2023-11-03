from numpy import fft
#from ..constants import c, fs

def fft(field_array, dt, axis = 0):
    freqs_data = fft.rfft(field_array, axis = axis)
    freqs = fft.rfftfreq(field_array.shape[axis], d = dt)
    return freqs, freqs_data


#########################################
################ 1D FFT #################
#########################################

def fft1d(ey_data, dt):
    xf = fft.rfft(ey_data, axis = 0)
    freqs = fft.rfftfreq(n = ey_data.shape[0], d = dt)
    return freqs, xf
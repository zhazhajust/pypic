import numpy as np

def get_max_index_1d(ey, dt):
    freq = np.fft.rfftfreq(ey.shape[0], d = dt) 
    xf = np.abs(np.fft.rfft(ey))
    idx = np.argmax(xf)
    print(f"{freq[idx]/1e12} THz")
    return idx
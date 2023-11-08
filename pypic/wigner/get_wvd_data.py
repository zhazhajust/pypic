####################################
####################################
####################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c
try:
    import matlab
    import matlab.engine
except:
    pass
class MlabWrapper:
    def __init__(self, Field, interval):
        self.Field = Field
        self.interval = interval
        return
    
    def __getitem__(self, key):
        Ey = self.Field[key]
        Ey = Ey[::self.interval]
        eng = matlab.engine.start_matlab()
        WVD = eng.wvd(matlab.double(Ey.tolist()))
        pyWvd = np.asarray(WVD)
        
        return np.abs(pyWvd)
    
    def __call__(self):
        Ey = self.Field
        Ey = Ey[::self.interval]
        eng = matlab.engine.start_matlab()
        WVD = eng.wvd(matlab.double(Ey.tolist()))
        pyWvd = np.asarray(WVD)
        
        return np.abs(pyWvd)
    
    @property
    def shape(self):
        return self.Field.shape
    
def getWvdData(z, Field, interval):
    z = z[::interval]
    dt = (z[1] - z[0])/c
    fs = 1/dt

    freqs = np.linspace(0, fs/2, z.shape[0]) #pyWvd.shape[0])
    zZ = np.linspace(z.min(), z.max(), z.shape[0] * 2) #pyWvd.shape[1])
    
    return zZ, freqs, MlabWrapper(Field, interval)()

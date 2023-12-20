import numpy as np
import matplotlib.pyplot as plt
#from ..font import setFont
#setFont()

def plotField(x, y, Field, figsize = [4, 3]):
    plt.figure(figsize = figsize)
    plt.pcolormesh(x, y, Field.T, vmin = -Field.max(), vmax = Field.max(), cmap = 'seismic')
    cbar = plt.colorbar()
    return cbar

def plotFreq(freqX, freqY, Ey_F):
    plt.figure(figsize = [4, 3])
    #XF = np.abs(Ey_F)**2
    XF = Ey_F
    plt.pcolormesh(freqX, freqY, XF.T, cmap = getCmap())
    cbar = plt.colorbar()
    #plt.xlim([-20e12, 20e12])
    #plt.ylim([-20e12, 20e12])
    return cbar

def plotGaussKernel(times, gauss_kernel):
    plt.figure(figsize = [4, 3])
    plt.plot(times, gauss_kernel)
    return

def plotGaussFreq(gauss_freq, gauss_f):
    plt.figure(figsize = [4, 3])
    plt.plot(gauss_freq, np.abs(gauss_f)**2)
    plt.xlim([0, 30e12])
    return

def plotFreqSum(freq, theta, Im_fft):
    plt.figure(figsize = [3.6, 3])
    plt.plot(freq, np.sum(Im_fft, axis = 0))
    plt.xlim([0.1e12, 10e12])

    plt.figure(figsize = [3.6, 3])
    plt.plot(theta, np.sum(Im_fft, axis = 1))
    #plt.plot(33 * 3.14/180, 0.04, 'xr-')
    return

def plotStepFreq(times, gauss_f):
    line_f = gauss_f.copy()
    line_f[:] = 1
    line_f[np.abs(gauss_freq) > 10e12] = 0
    line_f[np.abs(gauss_freq) < 0.1e12] = 0

    plt.figure(figsize = [4, 3])
    plt.plot(gauss_freq, np.abs(line_f)**2)
    plt.xlim([-30e12, 30e12])
    line_r = (np.fft.ifft(np.fft.ifftshift(line_f))).real

    plt.figure(figsize = [4, 3])
    plt.plot(times, line_r)
    return

def plotFieldLine(times, im, im_filter, theta, theta_point):
    EySum = im[:, np.argmin(np.abs(theta * 180/3.14 - theta_point))]
    plt.figure(figsize = [3.6, 3])
    plt.plot(times, EySum)
    
    dt = times[1] - times[0]
    THzSum = im_filter[:, np.argmin(np.abs(theta * 180/3.14 - theta_point))]
    #plt.figure(figsize = [3.6, 3])
    plt.plot(times, THzSum)
    
    
    XFLine = np.fft.rfft(THzSum)
    freq = np.fft.rfftfreq(THzSum.shape[0], d = dt)
    plt.figure(figsize = [3.6, 3])
    plt.plot(freq, np.abs(XFLine)**2)
    plt.xlim([0.1e12, 10e12])
    return

def plotField(self, y_limit = 0):
    theta = self.theta
    NewEy = self.NewEy
    ###################
    theta_limit = np.arcsin(y_limit/self.R0)
    NewEy = NewEy[:, np.abs(theta) >= theta_limit]
    theta = theta[np.abs(theta) >= theta_limit]
    ###################   
    ################### 
    with h5py.File(self.datadir + "/cachField.hdf5", "w") as f:
        dset = f.create_dataset("Field/theta", data = theta)
        dset = f.create_dataset("Field/times", data = self.times)
        dset = f.create_dataset("Field/Ey", data = NewEy)           
    ###################
    plt.figure(figsize=[4,3])
    plt.pcolormesh(theta[::10]*180/3.14, self.times, self.NewEy[:,::10] , vmin = -self.NewEy.max(), vmax = self.NewEy.max(), cmap = 'seismic')
    cbar = plt.colorbar()
    cbar.set_label('cBz[$m_ew_r/e$]')
    plt.xlabel('Theta[degree]')
    plt.ylabel('Times[s]')        
    plt.savefig(self.figdir + '/' + str(self.Field) + '.jpg',dpi=160,bbox_inches = 'tight')        
    return

def plotFieldAndTHz(theta_point, theta, times, Im_fft):
    EySum = im[:, np.argmin(np.abs(theta * 180/3.14 - theta_point))]
    THzSum = im_filter[:, np.argmin(np.abs(theta * 180/3.14 - theta_point))]
    plt.figure(figsize = [3.6, 3])
    plt.plot(times, EySum)
    plt.plot(times, THzSum)
    plt.xlim([1.5e-12, 3.0e-12])

    XFLine = np.fft.rfft(THzSum)
    dt = times[1] - times[0]
    freq = np.fft.rfftfreq(THzSum.shape[0], d = dt)

    plt.figure(figsize = [3.6, 3])
    plt.plot(freq, np.abs(XFLine)**2)
    plt.xlim([0.1e12, 10e12])
    return

def plotTotalFreq(theta, freq, Im_fft):
    plt.figure(figsize = [4, 3])
    plt.plot(freq[freq < 10e12], np.sum(Im_fft[:, freq < 10e12], axis = 0))
    plt.plot(freq[np.argmax(np.sum(Im_fft[:, freq < 10e12], axis = 0))], 
             np.max(np.sum(Im_fft[:, freq < 10e12], axis = 0)), 'xr-')
    print(f'Max Loc: {freq[np.argmax(np.sum(Im_fft[:, freq < 10e12], axis = 0))]/1e12:.3f}THz')

    plt.figure(figsize = [4, 3])
    plt.plot(theta, np.sum(Im_fft[:, freq < 10e12], axis = 1))
    plt.plot(theta[np.argmax(np.sum(Im_fft[:, freq < 10e12], axis = 1))], 
             np.max(np.sum(Im_fft[:, freq < 10e12], axis = 1)), 'xr-')
    print(f'Max Loc: {theta[np.argmax(np.sum(Im_fft[:, freq < 10e12], axis = 1))] * 180/3.14:.3f} Degree')
    return

if __name__ == '__main__':
    plotField(screen, y_limit = 0)

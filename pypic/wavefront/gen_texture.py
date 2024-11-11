import numpy as np
from functools import partial
from scipy.constants import c
from pypic.wavefront import get_ellipse
from lasy.profiles.transverse import HermiteGaussianTransverseProfile

def get_profile(y, z, w0, z_foc, phase_0, n_x = 0, n_y = 1, frequency = 12.04e12):
    # frequency = 12.04e12
    wavelength = c/frequency
    laser_per = HermiteGaussianTransverseProfile(w0, n_x, n_y, wavelength=wavelength, z_foc=z_foc)
    Y, Z = np.meshgrid(y, z)
    return laser_per._evaluate(Y, Z)*np.exp(1j*phase_0)

def gen_texture(y: np.ndarray, z: np.ndarray, w00: float, w01: float, z_foc00: float, 
                z_foc01: float, ket_0: float, ket_1: float, theta_0: float, 
                phase_00: float, phase_01: float, frequency = 12.04e12):
    
    profile00 = ket_0*get_profile(y, z, w00, z_foc00, phase_00, 0, 0, frequency)
    profile01 = ket_1*get_profile(y, z, w01, z_foc01, phase_01, 0, 1, frequency)*np.exp(1j*theta_0)
    psi, chi = get_ellipse(np.abs(profile00), np.abs(profile01), np.angle(profile00), np.angle(profile01))
    amp = np.sqrt(np.abs(profile00)**2 + np.abs(profile01)**2)
    colors_alpha = amp/amp.max()
    return psi, chi, colors_alpha

######################################################

def gen_texture2(y: np.ndarray, z: np.ndarray, w00: float, w01: float, z_foc00: float, 
                z_foc01: float, ket_0: float, ket_1: float, theta_0: float, 
                phase_00: float, phase_01: float):
    '''
    y: y
    z: z
    '''
    frequency = 12.04e12
    wavelength = c/frequency
    # print(f"Wavelength: {wavelength/1e-6:.3f} um")

    laser_per_01 = HermiteGaussianTransverseProfile(w01, 0, 1, wavelength=wavelength, z_foc=z_foc00)
    laser_per_00 = HermiteGaussianTransverseProfile(w00, 0, 0, wavelength=wavelength, z_foc=z_foc01)

    Y, Z = np.meshgrid(y, z)

    profile_01 = laser_per_01._evaluate(Y, Z)*np.exp(1j*phase_01)
    profile_00 = laser_per_00._evaluate(Y, Z)*np.exp(1j*phase_00)
    # profile_01 = laser_per_01._evaluate(Y, Z)
    # profile_00 = laser_per_00._evaluate(Y, Z)
    profile_01 /= np.abs(profile_01).max()
    profile_00 /= np.abs(profile_00).max()
    # profile_01 /= profile_01.real.max()
    # profile_00 /= profile_00.real.max()

    # print(np.abs(profile_01).max(), np.abs(profile_00).max())
    # theta_0 = phase_01 - phase_00
    #########################################################
    #########################################################
    #########################################################

    ket_R = np.asarray([0, 1])
    ket_L = np.asarray([1, 0])
    
    ket_H = np.cos(1/2*1/2*np.pi)*ket_R + np.exp(1j*0)*np.sin(1/2*1/2*np.pi)*ket_L
    ket_V = np.cos(1/2*1/2*np.pi)*ket_R + np.exp(1j*np.pi)*np.sin(1/2*1/2*np.pi)*ket_L
    
    ket_phi_0 = ket_0 * profile_00 * ket_H[0] + ket_1 * np.exp(1j * theta_0) * profile_01 * ket_V[0]
    ket_phi_1 = ket_0 * profile_00 * ket_H[1] + ket_1 * np.exp(1j * theta_0) * profile_01 * ket_V[1]
    # ket_phi_0 = ket_0 * profile_00 * ket_H[0] + ket_1 * profile_01 * ket_V[0]
    # ket_phi_1 = ket_0 * profile_00 * ket_H[1] + ket_1 * profile_01 * ket_V[1]
    amp0 = np.abs(ket_phi_0)
    amp1 = np.abs(ket_phi_1)
    angle0 = np.angle(ket_phi_0)
    angle1 = np.angle(ket_phi_1)
    theta = 2 * np.arccos(amp0/np.sqrt(amp0**2 + amp1**2))
    alpha = angle1 - angle0
    chi = (np.pi/2 - theta)/2
    psi = alpha/2
    amp = np.sqrt(np.abs(profile_00)**2 + np.abs(profile_01)**2)
    colors_alpha = amp/amp.max()
    return psi, chi, colors_alpha

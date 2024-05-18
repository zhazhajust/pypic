from numpy import arcsin, arctan, tan, sin, cos
import numpy as np

# def get_ellipse(amplitude, amplitude2, phase, phase2):
#     E0y = amplitude2
#     E0x = amplitude
#     phi_y = phase2
#     phi_x = phase
#     phi = phi_y - phi_x
#     alpha = arctan(E0y/E0x)
#     psi = arctan(tan(2 * alpha) * cos(phi))/2
#     chi = arcsin(sin(2 * alpha) * sin(phi))/2
#     return psi, chi

def get_ellipse(amplitude, amplitude2, phase, phase2):
    return calculate_psi_chi(amplitude, phase, amplitude2, phase2)

def calculate_psi_chi(amplitude_x, phase_x, amplitude_y, phase_y):
    # Convert amplitude and phase to complex electric field components
    Ex = amplitude_x * np.exp(1j * phase_x)
    Ey = amplitude_y * np.exp(1j * phase_y)
    
    # Calculate Stokes parameters
    I = np.abs(Ex)**2 + np.abs(Ey)**2
    Q = np.abs(Ex)**2 - np.abs(Ey)**2
    U = 2 * np.real(Ex * np.conj(Ey))
    V = 2 * np.imag(Ex * np.conj(Ey))
    
    # Calculate psi and chi
    psi = 0.5 * np.arctan2(U, Q)
    # chi = 0.5 * np.arctan2(V, I)
    chi = 0.5 * np.arcsin(V/I)
    
    return psi, chi

def generate_rotated_ellipse(center, radius, psi_angle, chi_angle):
    # Calculate height based on the given angle
    width = radius * np.cos(np.radians(chi_angle))
    height = radius * np.sin(np.radians(chi_angle))

    # Generate points for the ellipse
    theta = np.linspace(0, -2*np.pi, 100)
    x = center[0] + width/2 * np.cos(theta)
    y = center[1] + height/2 * np.sin(theta)

    # Rotate the points around the center
    rotated_x = center[0] + (x - center[0]) * np.cos(np.radians(psi_angle)) - (y - center[1]) * np.sin(np.radians(psi_angle))
    rotated_y = center[1] + (x - center[0]) * np.sin(np.radians(psi_angle)) + (y - center[1]) * np.cos(np.radians(psi_angle))

    return rotated_x, rotated_y

def get_stokes_vector(psi, chi):
    psi_rad = np.radians(psi)
    chi_rad = np.radians(chi)
    # Calculate the Stokes parameters
    S0 = 1
    S1 = np.cos(2 * psi_rad) * np.cos(2 * chi_rad)
    S2 = np.sin(2 * psi_rad) * np.cos(2 * chi_rad)
    S3 = np.sin(2 * chi_rad)
    # Normalize the Stokes parameters
    norm = np.sqrt(S1**2 + S2**2 + S3**2)
    S1 /= norm
    S2 /= norm
    S3 /= norm
    return [S0, S1, S2, S3]

# ## Wraper
# def get_ellipse_point(center, width, psi, chi):
#     #width = 20.0 #ey.max()*2
#     psi_angle = psi * 180/3.14  # Change psi angle as needed
#     rotation_angle = chi * 180/3.14
#     y, z = generate_rotated_ellipse(center, width, psi_angle, rotation_angle)
#     print(y.shape, z.shape)
#     return y, z

# #################################################################

# def plot_wavefront(y, z, psi, chi):
#     plt.figure()
#     plt.pcolormesh(y, z, psi, cmap = "RdBu_r")
#     cbar = plt.colorbar()
#     plt.xlabel("Y [um]")
#     plt.ylabel("Z [um]")
#     cbar.set_label("$\psi$ [rad]")
    
#     plt.figure()
#     plt.pcolormesh(y, z, chi, cmap = "RdBu_r")
#     cbar = plt.colorbar()
#     plt.xlabel("Y [um]")
#     plt.ylabel("Z [um]")
#     cbar.set_label("$\chi$ [rad]")
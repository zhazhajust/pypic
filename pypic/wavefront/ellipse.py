from numpy import arcsin, arctan, tan, sin, cos
import numpy as np

def get_ellipse(amplitude, amplitude2, phase, phase2):
    E0y = amplitude2
    E0x = amplitude
    phi_y = phase2
    phi_x = phase
    phi = phi_y - phi_x
    alpha = arctan(E0y/E0x)
    psi = arctan(tan(2 * alpha) * cos(phi))/2
    chi = arcsin(sin(2 * alpha) * sin(phi))/2
    return psi, chi

# def generate_rotated_ellipse(center, width, psi_angle, rotation_angle):
def generate_rotated_ellipse(center, width, psi_angle, chi_angle):
    # Calculate height based on the given angle
    # height = width * np.tan(np.radians(psi_angle))

    height = width * np.tan(np.radians(chi_angle))

    # Generate points for the ellipse
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + width/2 * np.cos(theta)
    y = center[1] + height/2 * np.sin(theta)

    # Rotate the points around the center
    rotated_x = center[0] + (x - center[0]) * np.cos(np.radians(psi_angle)) - (y - center[1]) * np.sin(np.radians(psi_angle))
    rotated_y = center[1] + (x - center[0]) * np.sin(np.radians(psi_angle)) + (y - center[1]) * np.cos(np.radians(psi_angle))

    return rotated_x, rotated_y

## Wraper
def get_ellipse_point(center, width, psi, chi):
    #width = 20.0 #ey.max()*2
    psi_angle = psi * 180/3.14  # Change psi angle as needed
    rotation_angle = chi * 180/3.14
    y, z = generate_rotated_ellipse(center, width, psi_angle, rotation_angle)
    print(y.shape, z.shape)
    return y, z

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
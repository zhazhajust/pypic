import numpy as np

def generate_rotated_ellipse(center, radius, psi_angle, chi_angle):
    # Calculate height based on the given angle
    width = radius * np.cos(chi_angle)
    height = radius * np.sin(chi_angle)

    # Generate points for the ellipse
    # theta = np.linspace(0, -2*np.pi, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + width/2 * np.cos(theta)
    y = center[1] + height/2 * np.sin(theta)

    # Rotate the points around the center
    rotated_x = center[0] + (x - center[0]) * np.cos(np.radians(psi_angle)) - (y - center[1]) * np.sin(np.radians(psi_angle))
    rotated_y = center[1] + (x - center[0]) * np.sin(np.radians(psi_angle)) + (y - center[1]) * np.cos(np.radians(psi_angle))

    return rotated_x, rotated_y

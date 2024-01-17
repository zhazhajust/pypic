import numpy as np
import matplotlib.pyplot as plt

# Function to map psi and chi to RGB colors
def map_to_rgb(psi, chi, alpha):
    h = np.cos(psi)*np.cos(chi)
    s = np.sin(psi)*np.cos(chi)
    v = np.sin(chi)
    # Scale values to [0, 1] range
    h = (h + 1.0) / 2.0
    s = (s * 1.0 + 1.0) / 2.0
    v = (v * 1.0 + 1.0) / 2.0
    # return np.asarray([h, s, v]).transpose(1, 2, 0)
    return np.asarray([s, v, h, alpha]).transpose(1, 2, 0)

def get_example():
    # Define the range for psi and chi
    psi_range = np.linspace(-np.pi, np.pi, 500)
    chi_range = np.linspace(-np.pi/2, np.pi/2, 500)

    # Create a 2D grid for psi and chi
    Psi, Chi = np.meshgrid(psi_range, chi_range)

    test_colors = map_to_rgb(Psi, Chi, np.ones_like(Chi))
    # # Plot using pcolormesh and set colormap to "jet"
    plt.figure(figsize=[1.5, 1.5])
    im = plt.pcolormesh(np.degrees(psi_range), np.degrees(chi_range), test_colors)
    plt.xlabel('2$\psi$', fontsize = 10)
    plt.ylabel('2$\chi$', fontsize = 10)
    plt.title('Poincare Sphere Visualization', fontsize = 10)
    plt.xticks([])
    plt.yticks([])
    # plt.ylim([-0.2, 0.2])
    # plt.xlim([-0.5, 0.5])
    return im

if __name__ == "__main__":
    get_example()
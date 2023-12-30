import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# def plot_poincare_sphere(psi, chi):
#     # Convert psi and chi to radians
#     psi_rad = np.radians(psi)
#     chi_rad = np.radians(chi)

#     # Calculate the Stokes parameters
#     S0 = 1
#     S1 = np.cos(2 * psi_rad) * np.cos(2 * chi_rad)
#     S2 = np.sin(2 * psi_rad) * np.cos(2 * chi_rad)
#     S3 = np.sin(2 * chi_rad)

#     # Normalize the Stokes parameters
#     norm = np.sqrt(S1**2 + S2**2 + S3**2)
#     S1 /= norm
#     S2 /= norm
#     S3 /= norm

#     # Background points for horizontal and vertical polarizations
#     h_points = np.array([[1, 0, 0], [-1, 0, 0]])
#     v_points = np.array([[0, 1, 0], [0, -1, 0]])

#     # Background points for right-handed and left-handed circular polarizations
#     r_points = np.array([[0, 0, 1], [0, 0, -1]])
#     l_points = np.array([[0, 0, -1], [0, 0, 1]])

#     # Plot on the Poincaré sphere
#     fig = plt.figure(figsize=(8, 8))
#     ax = fig.add_subplot(111, projection='3d')
    
#     # Plot the Poincaré sphere
#     u = np.linspace(0, 2 * np.pi, 100)
#     v = np.linspace(0, np.pi, 100)
#     x = 1 * np.outer(np.cos(u), np.sin(v))
#     y = 1 * np.outer(np.sin(u), np.sin(v))
#     z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
#     ax.plot_surface(x, y, z, color='b', alpha=0.1, antialiased=False, label='Poincaré Sphere')

#     # Plot the ellipse as a point
#     ax.scatter(S1, S2, S3, color='r', s=100, label='Ellipse Laser')
#     ax.text(S1, S2, S3, f'({S1:.2f}, {S2:.2f}, {S3:.2f})', fontsize=10, ha='right')

#     # Add arrow from center to the ellipse point
#     ax.quiver(0, 0, 0, S1, S2, S3, color='black', arrow_length_ratio=0.1)

#     # Connect background points with dotted lines
#     for points in [h_points, v_points, r_points, l_points]:
#         ax.plot(points[:, 0], points[:, 1], points[:, 2], linestyle='-.', color='black', alpha=0.5)

#     # Background points for horizontal and vertical polarizations
#     #ax.scatter(v_points[:, 0], v_points[:, 1], v_points[:, 2], color='gray', s=50, alpha=0.5, label='Horizontal/Vertical Polarizations')
#     ax.text(1, 0, 0, 'Horizontal', fontsize=8, ha='left', va='center')
#     ax.text(0, 1, 0, 'Vertical', fontsize=8, ha='left', va='center')

#     #ax.scatter(h_points[:, 0], h_points[:, 1], h_points[:, 2], color='gray', s=50, alpha=0.5, label='Horizontal/Vertical Polarizations')
#     # Background points for right-handed and left-handed circular polarizations
#     #ax.scatter(r_points[:, 0], r_points[:, 1], r_points[:, 2], color='blue', s=50, alpha=0.5, label='Circular Polarizations')
#     #ax.scatter(l_points[:, 0], l_points[:, 1], l_points[:, 2], color='red', s=50, alpha=0.5)

#     ax.text(0, 0, 1, 'Right Circular', fontsize=8, ha='left', va='center')
#     ax.text(0, 0, -1, 'Left Circular', fontsize=8, ha='left', va='center')

#     # Set axis labels
#     ax.set_xlabel('S1')
#     ax.set_ylabel('S2')
#     ax.set_zlabel('S3')

#     # Add legend
#     ax.legend()

#     # Add title
#     plt.title('Poincaré Sphere Representation')

#     plt.show()

# def plot_poincare_sphere(S1, S2, S3):

def plot_poincare_sphere(stokes_vectors: list[float], labels: list[str] = None):
    # Background points for horizontal and vertical polarizations
    h_points = np.array([[1, 0, 0], [-1, 0, 0]])
    v_points = np.array([[0, 1, 0], [0, -1, 0]])

    # Background points for right-handed and left-handed circular polarizations
    r_points = np.array([[0, 0, 1], [0, 0, -1]])
    l_points = np.array([[0, 0, -1], [0, 0, 1]])

    # Plot on the Poincaré sphere
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the Poincaré sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 1 * np.outer(np.cos(u), np.sin(v))
    y = 1 * np.outer(np.sin(u), np.sin(v))
    z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='b', alpha=0.1, antialiased=False, label='Poincaré Sphere')

    idx = 0
    for S1, S2, S3 in stokes_vectors:
        # Plot the ellipse as a point
        if labels:
            label = labels[idx]
        else:
            label = 'Ellipse Laser'
        ax.scatter(S1, S2, S3, color='r', s=100, label=label)
        ax.text(S1, S2, S3, f'({S1:.2f}, {S2:.2f}, {S3:.2f})', fontsize=10, ha='right')

        # Add arrow from center to the ellipse point
        ax.quiver(0, 0, 0, S1, S2, S3, color='black', arrow_length_ratio=0.1)
        idx += 1
        
    # Connect background points with dotted lines
    for points in [h_points, v_points, r_points, l_points]:
        ax.plot(points[:, 0], points[:, 1], points[:, 2], linestyle='-.', color='black', alpha=0.5)

    # Background points for horizontal and vertical polarizations
    #ax.scatter(v_points[:, 0], v_points[:, 1], v_points[:, 2], color='gray', s=50, alpha=0.5, label='Horizontal/Vertical Polarizations')
    ax.text(1, 0, 0, 'Horizontal', fontsize=8, ha='left', va='center')
    ax.text(0, 1, 0, 'Vertical', fontsize=8, ha='left', va='center')

    #ax.scatter(h_points[:, 0], h_points[:, 1], h_points[:, 2], color='gray', s=50, alpha=0.5, label='Horizontal/Vertical Polarizations')
    # Background points for right-handed and left-handed circular polarizations
    #ax.scatter(r_points[:, 0], r_points[:, 1], r_points[:, 2], color='blue', s=50, alpha=0.5, label='Circular Polarizations')
    #ax.scatter(l_points[:, 0], l_points[:, 1], l_points[:, 2], color='red', s=50, alpha=0.5)

    ax.text(0, 0, 1, 'Right Circular', fontsize=8, ha='left', va='center')
    ax.text(0, 0, -1, 'Left Circular', fontsize=8, ha='left', va='center')

    # Set axis labels
    ax.set_xlabel('S1')
    ax.set_ylabel('S2')
    ax.set_zlabel('S3')

    # Add legend
    ax.legend()

    # Add title
    plt.title('Poincaré Sphere Representation')

    plt.show()
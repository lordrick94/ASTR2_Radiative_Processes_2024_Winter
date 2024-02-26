import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def random_theta_phi():
    """
    Generate random theta and phi values.
    
    Returns:
    tuple: theta and phi values in radians.
    """
    eta_1 = np.random.uniform(0, 1)
    eta_0 = np.random.uniform(0, 1)
    theta = np.arccos(2 * eta_0 - 1)
    phi = 2 * np.pi * eta_1

    return theta, phi

def spherical_to_cartesian(theta, phi, r=5):
    """
    Convert spherical coordinates to Cartesian coordinates.
    
    Parameters:
    theta (float): azimuthal angle in radians.
    phi (float): polar angle in radians.
    r (float): length of the vector, default is 5.
    
    Returns:
    tuple: Cartesian coordinates (x, y, z).
    """
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    
    return x, y, z

def plot_spherical_vector(ax, theta, phi, color):
    """
    Plot a vector on the given 3D axis.
    
    Parameters:
    ax (matplotlib.axes._subplots.Axes3DSubplot): The 3D subplot to plot on.
    theta (float): azimuthal angle in radians.
    phi (float): polar angle in radians.
    color (str): Color of the vector.
    """
    # Get Cartesian coordinates
    x, y, z = spherical_to_cartesian(theta, phi)

    # Plot the vector
    ax.quiver(0, 0, 0, x, y, z, color=color, arrow_length_ratio=0.1)




def plot_axes_at_origin(ax):
    """
    Draw axes lines through the origin.
    
    Parameters:
    ax (matplotlib.axes._subplots.Axes3DSubplot): The 3D subplot to draw axes on.
    """
    # Limits for the axes (adjust as necessary)
    lim = 5
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim, lim])
    
    # Hide the default axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    
    # Draw new axes lines: X, Y, Z
    ax.quiver(0, 0, 0, lim, 0, 0, color='k', arrow_length_ratio=0.05)
    ax.quiver(0, 0, 0, 0, lim, 0, color='k', arrow_length_ratio=0.05)
    ax.quiver(0, 0, 0, 0, 0, lim, color='k', arrow_length_ratio=0.05)
    
    # Label the axes
    ax.text(lim, 0, 0, 'X', color='k')
    ax.text(0, lim, 0, 'Y', color='k')
    ax.text(0, 0, lim, 'Z', color='k')

# Example usage
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plot_axes_at_origin(ax)

colors = ['b', 'g', 'r', 'c', 'm']  # Different colors for different vectors

# Assuming the plot_spherical_vector function is defined as before but includes the ax parameter
for i in range(5):
    theta, phi = random_theta_phi()
    plot_spherical_vector(ax, theta, phi, colors[i % len(colors)])

plt.title('Multiple 3D Vectors from Spherical Coordinates with Axes at Origin')
plt.show()

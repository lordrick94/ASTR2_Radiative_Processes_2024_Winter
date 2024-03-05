import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import default_rng
import pandas as pd



def plot_tau_theta_phi(phot_num):
    df = pd.read_csv(f'photon_num{phot_num}.csv')
    fig, ax = plt.subplots()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('3D Vector Plot')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    
    # Initial origin
    origin = [0, 0]
    
    while True:
        theta, phi = df['theta'], df['phi']
        tau = df['tau']
        
        # Accumulate the positions of all vectors
        positions = [origin]
        
        # Generate random colors for each vector
        colors = np.random.rand(len(tau), 3)
        
        for i in range(len(theta)):
            x = tau[i] * np.sin(theta[i]) * np.cos(phi[i]) + positions[-1][0]
            y = tau[i] * np.sin(theta[i]) * np.sin(phi[i]) + positions[-1][1]
            positions.append([x, y])

        # Plot all vectors
        for i,clr in zip((range(1, len(positions))), colors):
            ax.scatter([positions[i-1][0], positions[i][0]], [positions[i-1][1], positions[i][1]], color='blue', marker='o',alpha=0.5,s=2)
            ax.annotate("", xy=(positions[i][0], positions[i][1]), xytext=positions[i-1],
                        arrowprops=dict(arrowstyle="->", color=clr))
            ax.set_xlim(-4, 4)
            ax.set_ylim(-6, 7)
            
            # Plot the axes
            ax.axhline(0, color='black', lw=0.5, alpha=0.3)
            ax.axvline(0, color='black', lw=0.5, alpha=0.3)
            
            plt.draw()
            plt.pause(0.001)
        
        # Wait for user input to continue or quit
        if input("Press Enter to continue, or 'q' to quit: ").strip().lower() == 'q':
            break
        ax.clear()
        

    plt.close()

plot_tau_theta_phi()

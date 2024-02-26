import numpy as np
import pandas as pd


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

def random_tau():
    """
    Generate random optical depth for the particle to move
    
    Returns:    
        float: optical depth
        
    """
    eta_1 = np.random.uniform(0, 1)
    tau = -np.log(1-eta_1)

    return tau
import numpy as np
import pandas as pd

from numpy.random import default_rng 


seed = 42

def random_theta_phi(seed,n):
    """
    Generate random theta and phi values.
    
    Returns:
    tuple: theta and phi values in radians.
    """
    rng = default_rng(seed,n)
    eta_1 = rng.uniform(0, 1,n)
    eta_0 = rng.uniform(0, 1,n)
    theta = np.arccos(2 * eta_0 - 1)
    phi = 2 * np.pi * eta_1

    return theta, phi

def random_tau(seed,n):
    """
    Generate random optical depth for the particle to move
    
    Returns:    
        float: optical depth
        
    """
    rng = default_rng(seed)
    eta_1 = rng.uniform(0, 1,n)
    tau = -np.log(1-eta_1)

    return tau
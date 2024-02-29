# Getting PDF from the R(w, w') integral
import numpy as np

import scipy.integrate as spi

data = np.loadtxt('Rwwp.txt')

def get_pdf(Rwwp):
    """
    This function takes the Rwwp matrix and returns the PDF of the w' direction
    """
    for i in range(len(Rwwp[0])):

        k = spi.trapezoid(Rwwp[:,i])

        Rwwp[:,i] = Rwwp[:,i]/k # Normalize the Rwwp in the w' direction

    np.savetxt('Rwwp_normalized.txt', Rwwp)

if __name__ == "__main__":
    get_pdf(data)
    
    



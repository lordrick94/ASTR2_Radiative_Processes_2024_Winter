import numpy as np
from utils import random_theta_phi, random_tau, get_tau_h, get_wp_from_random_variate, write_results_to_file
from numpy.random import default_rng 


# Constants
MAX_NUM_SCAT = 1000000
ESCAPED_PHOTONS_THRESHOLD = 1000

def main():
    phot_num = 0
    escaped_photons = 0
    # Make results file
    filename = 'results.txt'
    
    params = 'phot_num,scat_num,escape_w'
    
    ete = open(filename, 'w')
    
    ete.write(params + '\n')
    

    while escaped_photons < ESCAPED_PHOTONS_THRESHOLD:
        scat_num = 0
        w, x = 0, 0
        

        while True:
            for _ in range(MAX_NUM_SCAT):
                # Get tau_h for the current w
                tau_h_in = get_tau_h(w)
                
                # Get random direction
                theta, phi = random_theta_phi(phot_num, scat_num)
                
                # Get random tau for how far the photon will travel
                tau = random_tau(phot_num, scat_num)
                tau_eff = tau * np.sin(theta) * np.cos(phi)
                
                # Get distance traveled in the x direction
                del_x = tau_eff / tau_h_in
                
                new_x = x + del_x
                
                w_next = get_wp_from_random_variate(phot_num, scat_num, wc=w)
                print(f'Next w = {w_next}')
                
                print(f'New x = {new_x}')
                
                    
                if np.abs(new_x) > 1:
                    print("Yaaay!!!!Photon has escaped at w =", w,"\n")
                    write_results_to_file(phot_num, scat_num, escape_w=w)
                    escaped_photons += 1

                    w = 0
                    
                    scat_num = 0
                    
                    break
                else:
                    print("Photon has not escaped at w =", w)
                    w = w_next
                    print("New w =", w)
                    
                    x = new_x
                    scat_num += 1
                    print("Scat_num =", scat_num)

            if escaped_photons >= ESCAPED_PHOTONS_THRESHOLD:
                break

            phot_num += 1

if __name__ == "__main__":
    main()

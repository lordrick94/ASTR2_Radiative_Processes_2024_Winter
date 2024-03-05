import numpy as np
from utils import random_theta_phi, random_tau, get_tau_h, get_wp_from_random_variate, write_results_to_file

# Constants
MAX_NUM_SCAT = 1000000
ESCAPED_PHOTONS_THRESHOLD = 5

def main():
    phot_num = 0
    escaped_photons = 0
    
    #Make results file
    filename = 'results.txt'
    
    params = 'phot_num,scat_num,escape_w'
    
    ete = open(filename, 'w')
    
    ete.write(params + '\n')
    

    while escaped_photons < ESCAPED_PHOTONS_THRESHOLD:
        scat_num = 0
        w, x = 0, 0
        
        # Make output file for each photon
        outfile = open(f'photons/phot_num{phot_num}.csv', 'w')
        
        # Write the column headers
        params = 'phot_num,scat_num,theta,phi,tau,del_x'
        
        outfile.write(params + '\n')

        while True:
            for _ in range(MAX_NUM_SCAT):
                theta, phi = random_theta_phi(phot_num, scat_num)
                tau = random_tau(0, scat_num)
                tau_eff = tau * np.sin(theta) * np.cos(phi)
                tau_h_in = get_tau_h(w)
                tau_h = tau_h_in / (np.sin(theta) * np.cos(phi))
                print(f"w = {w}, tau_h = {tau_h}, tau_eff = {tau_eff}")

                del_x = tau_eff / tau_h

                if x + del_x > 1:
                    print("Photon has escaped at w =", w)
                    write_results_to_file(phot_num, scat_num, escape_w=w)
                    escaped_photons += 1
                    
                    # Choose randomly one of these two values [-2,2]
                    
                    w = np.random.choice([-2, 2])
                    
                    
                    
                    break
                else:
                    
                    print("Photon has not escaped at w =", w)
                    wp = w
                    w = get_wp_from_random_variate(0, scat_num, wc=wp)
                    print("New w =", w)
                    x += del_x
                    scat_num += 1
                    print("Scat_num =", scat_num)
                    print()

                if escaped_photons >= ESCAPED_PHOTONS_THRESHOLD:
                    break

            phot_num += 1

if __name__ == "__main__":
    main()

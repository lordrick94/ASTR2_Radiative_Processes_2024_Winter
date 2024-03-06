import numpy as np
from utils import random_theta_phi, random_tau, get_tau_h, get_wp_from_random_variate, write_results_to_file



# Constants
MAX_NUM_SCAT = 1000000
ESCAPED_PHOTONS_THRESHOLD = 1000

def main():
    phot_num = 1
    escaped_photons = 0
    # Make results file
    filename = 'results.txt'
    
    params = 'phot_num,scat_num,escape_w'
    
    ete = open(filename, 'w')
    
    ete.write(params + '\n')
    

    while escaped_photons < ESCAPED_PHOTONS_THRESHOLD:
        scat_num = 1
        w_min = np.random.uniform(1.5,2.5)
        w = np.random.choice([w_min,-1*w_min])
        x = 0

        while True:
            for _ in range(MAX_NUM_SCAT):
                # Get tau_h for the current w
                print(f'Current w = {w}')
                print(f'phot_num = {phot_num}, scat_num = {scat_num}')
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
                
                if np.isnan(new_x):
                    print("NaN encountered, moving to next scatter")
                    scat_num += 1
                    w_min = np.random.uniform(1.5,2.5)
                    wp = np.random.choice([w_min,-1*w_min])
                    w = get_wp_from_random_variate(phot_num, scat_num, wc=wp)

                elif w_next>20 or w_next<-20:
                    print("W_next out of bounds, moving to next scatter")
                    scat_num += 1
                    w_min = np.random.uniform(1.5,2.5)
                    wp = np.random.choice([w_min,-1*w_min])
                    w = get_wp_from_random_variate(phot_num, scat_num, wc=wp)
                    
                elif np.abs(new_x) > 1:
                    print("Yaaay!!!!Photon has escaped at w =", w,"\n")
                    write_results_to_file(phot_num, scat_num, escape_w=w)
                    escaped_photons += 1
                    
                    # Choose randomly one of these two values [-2,2]
                    w = np.random.choice([w_min,-1*w_min])
                    
                    scat_num = 0
                    
                    break
                else:
                    print("Photon has not escaped at w =", w)
                    w = w_next
                    print("New w =", w)
                    
                    if w > 30 or w < -30:
                        print("W out of bounds, moving to next photon")
                        break
                    else:
                        x = new_x
                        scat_num += 1
                        print("Scat_num =", scat_num)

            if escaped_photons >= ESCAPED_PHOTONS_THRESHOLD:
                break

            phot_num += 1

if __name__ == "__main__":
    main()

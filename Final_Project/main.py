from utils import *

import numpy as np


# For photon number 1

phot_num = 0

scat_num = 0

max_num_scat = 1000000

escaped_photons = 0

w = 0

while escaped_photons < 1000:

    for i in range(0, max_num_scat):
        

        # Get random direction
        theta,phi = random_theta_phi(phot_num=phot_num,scat_num=scat_num)
        

        # Random tau

        tau = random_tau(0,scat_num=scat_num)


        #get tau_geo
        tau_geo = get_tau_to_surface(theta,phi,tau)

        tau_int = get_tau_int(w)

        print(f"w ={w}, tau_int = {tau_int}")
        print("Theta, phi, Tau_geo = ", theta, phi,tau_geo)

        

        if tau_int < tau_geo:
            print("Photon has escaped at w = ", w)

            # Write the results
            write_results_to_file(phot_num=phot_num,
                                  scat_num=scat_num,
                                  escape_w=w)
            escaped_photons+=1

            # Reset w

            w = 0

            scat_num = 0

            break

        else:
            print("Photon has not escaped at w = ", w)
            wp = w
            # Update w
            w = get_wp_from_random_variate(phot_num=0,
                                        scat_num=scat_num,
                                        wc=wp)
            
            print("New w = ", w)

            # Update scat_num 
            scat_num += 1

            print("Scat_num = ", scat_num)

            print("")

    phot_num+=1




import numpy as np
from utils import random_theta_phi, random_tau, get_tau_h, get_wp_from_random_variate, write_results_to_file
from numpy.random import default_rng
from joblib import Parallel, delayed

# Constants
MAX_NUM_SCAT = 1000000
ESCAPED_PHOTONS_THRESHOLD = 1000

def simulate_photon(phot_num):
    escaped_photons = 0
    scat_num = 0
    w, x = 0, 0

    while escaped_photons < ESCAPED_PHOTONS_THRESHOLD:
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
            if np.abs(new_x) > 1:
                write_results_to_file(phot_num, scat_num, escape_w=w)
                escaped_photons += 1
                w = 0
                scat_num = 0
                break
            else:
                w = w_next
                x = new_x
                scat_num += 1

        phot_num += 1

def main():
    # Make results file
    filename = 'results.txt'
    params = 'phot_num,scat_num,escape_w'

    with open(filename, 'w') as ete:
        ete.write(params + '\n')

        Parallel(n_jobs=-1)(delayed(simulate_photon)(phot_num) for phot_num in range(ESCAPED_PHOTONS_THRESHOLD))

if __name__ == "__main__":
    main()

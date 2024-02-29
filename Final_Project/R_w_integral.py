import numpy as np
from scipy.integrate import quad
from joblib import Parallel, delayed

def main():
    def r_w_w_prime(x, w, w_prime):
        J = (np.pi)**(-3.5)
        a = 4.7e-4
        w_lower = np.min(np.array([np.abs(w), np.abs(w_prime)]))
        w_upper = np.max(np.array([np.abs(w), np.abs(w_prime)]))
        return J * (np.exp(-x**2)) * ((np.arctan((w_lower+x)/a)) - (np.arctan((w_upper-x)/a)))

    def integrate_r_w_w_prime(i, j, wx, wpy):
        w_1 = wx[i, j]
        w_prime_1 = wpy[i, j]
        w_lower = np.min(np.asarray([np.abs(w_1), np.abs(w_prime_1)]))
        w_upper = np.max(np.asarray([np.abs(w_1), np.abs(w_prime_1)]))
        l_lim = 0.5 * np.abs(w_upper - w_lower)
        int_result, err = quad(r_w_w_prime, l_lim, np.inf, args=(w_1, w_prime_1))
        return i, j, int_result

    w_min = -10.0
    w_max = 10.0
    wp_min = -30.0
    wp_max = 30.0
    n_w = 1001
    n_wp = 1001

    w = np.linspace(w_min, w_max, n_w)
    wp = np.linspace(wp_min, wp_max, n_wp)
    wx, wpy = np.meshgrid(w, wp)

    # Prepare for parallel computation
    n_jobs = -1  # Use all available CPUs
    result_mesh = np.zeros(wx.shape)

    # Perform parallel computation
    results = Parallel(n_jobs=n_jobs)(delayed(integrate_r_w_w_prime)(i, j, wx, wpy) for i in range(wx.shape[0]) for j in range(wx.shape[1]))

    # Fill in the result mesh with computed values
    for i, j, res in results:
        result_mesh[i, j] = res

    np.savetxt('int_table.txt', result_mesh)

if __name__ == '__main__':
    # Time the execution of the script
    import time
    start_time = time.time()
    print('Start time: ', start_time)
    print('Running the script...')
    main()  
    print('Elapsed time: ', time.time() - start_time)
    print('End time: ', time.time())
    print('Done!')

import numpy as np
from numpy.random import default_rng
from IPython import embed

def get_wp_from_random_variate(phot_num=0,scat_num=0,Rint=None,wc=1,seed=103):
    
    if Rint is None:
        Rint = np.loadtxt('Rwwp_cdf.txt')
    
    #how many random variates?

    rng = default_rng((phot_num+1)*seed)
    n_rand = 100000

    #get the xi_p
    xi_p = rng.uniform(0,1,n_rand)

    #make our array of output wp values
    wpc = np.zeros(n_rand)
    w_min  = -10.0
    w_max  =  10.0
    wp_min = -30.0
    wp_max =  30.0

    #how many samples in each direction?
    n_w  = 1001
    n_wp = 1001

    #produce arrays of w, w'
    w = np.linspace(w_min,w_max,n_w)
    wp = np.linspace(wp_min, wp_max, n_wp)

    #begin a loop over the random variates
        
    #what is our range of w,w'?

    #find the w indices bounding current w
    wi = np.searchsorted(w,wc,side="left")
    
    #define i, i+1
    i   = wi-1
    ip1 = wi
    
    #embed()
    #find the wp indices bounding xi_p
    
    wpi  = np.searchsorted(Rint[:,i],xi_p[scat_num])
    wpia = np.searchsorted(Rint[:,ip1],xi_p[scat_num])

    #define j, j+1 for each w
    j  = wpi-1
    ja = wpia-1
    
    #ensure the bounding box is large enough
    if(j>ja):
        ja = j
    elif(j<ja):
        j = ja
        
    jp1 = j+1
        
    #define t, z0, z1, z2, z3, and z
    t = (wc - w[i])/(w[ip1]-w[i])
    z0 = Rint[j,i]
    z1 = Rint[jp1,i]
    z2 = Rint[j,ip1]
    z3 = Rint[jp1,ip1]
    
    #find u
    u = (xi_p[20] - z2*t - z0*(1.-t))/((z1-z0)*(1.-t) + (z3-z2)*t)
    
    #get wp
    wpc = u*(wp[jp1] - wp[j]) + wp[j]

    return wpc

if __name__ == "__main__":
    Rint = np.loadtxt('Rwwp_cdf.txt')
    wpc = get_wp_from_random_variate(12222,1,Rint,7.6,103)
    print(wpc)

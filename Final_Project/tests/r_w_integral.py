# Evaulating the integral and find the PDF of R(w,w')

import numpy as np


w = np.arange(-20,20,0.1)
w_prime = np.arange(-20,20,0.1)

int_table = np.meshgrid(w,w_prime)

#Write the result to a file

np.savetxt('int_table.txt', int_table)

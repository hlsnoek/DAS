# Author: Hella Snoek en ...
# Studentnummer: 
# Date: Dec 2019
# Code for UvA/VU Data Analyse en Statistiek course

import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
import math as math

def poisson(k, lamda) :
    kans = math.pow(lamda,k)* math.exp(-lamda) / math.factorial(k)
    return kans

# Print hier de resultaten voor l=3, k=1:
print(poisson(1,3),poisson(2,3),poisson(3,3))

x = [i for i in range(1,40)]
yp_3 = [poisson(xi,2) for xi in x]
yp_5 = [poisson(xi,5) for xi in x]
yp_10 = [poisson(xi,10) for xi in x]
yp_20 = [poisson(xi,20) for xi in x]

# Door eerst expliciet een figure aan te maken kunnen we meerdere plotjes maken.
fig_d1 = plt.figure('Poisson Distributies')
plt.plot(x,yp_3,'-o',label='3')
plt.plot(x,yp_5,'-o',label='5')
plt.plot(x,yp_10,'-o',label='10')
plt.plot(x,yp_20,'-o',label='20')
plt.legend()
fig_d1.show()


## Deel twee Uniforme distributies:
#xu_r = [i for i in range(1,7)]
#yu = [30/6 for xu in xu_r]

np.random.seed(1)
rand = np.random.uniform()
xu = [(int)(0.5 + np.random.uniform()*6) for r in range(0,30)]

fig_du = plt.figure('uniforme distributie')
plt.hist(xu, range=(0.5,6.5), bins=6)
#plt.plot(xu_r,yu,'-o')
fig_du.show()

#fig_d4 = plt.figure('variatie per bin')
#po = [0  for i in range(1,7)]
#for xi in xr_3 :
#    po[xi-1] += 1
#    
#plt.hist(po, range=(0.5,10.5), bins=10)
#fig_d4.show()


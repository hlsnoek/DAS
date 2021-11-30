import numpy as np
import matplotlib.pyplot as plt
from random import seed
from random import random
import math as math
import os
from lmfit import models

print('Even controleren of je installatie helemaal werkt... ')
# test matplotlib
fig = plt.figure()

test = 4
# test numpy
np.sqrt(test)
# test math
math.sqrt(test)

#test random
p = np.random.uniform(1,6,40)

#test scipy:
x = [i for i in range(1,40)]

def functie(x,a) : 
    return a

ons_model = models.Model(functie)


print('    ... Je bent geslaagd!')

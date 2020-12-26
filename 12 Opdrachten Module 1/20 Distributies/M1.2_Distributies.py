# Author: Hella Snoek en ...
# Studentnummer: 
# Date: Dec 2019
# Code for UvA/VU Data Analyse en Statistiek course

import matplotlib.pyplot as plt
import numpy as np
import random
from random import seed
import math as math

def poisson(k, lamda) :
    # Hier je definitie van kans
    return kans

##  Print hier de resultaten voor k=1 en lambda=3:
print('k is 1, l = 3, p = ', poisson(1,3))

##  Door eerst expliciet een figure aan te maken kunnen we meerdere plotjes maken.
fig_d1 = plt.figure('Poisson Distributies')

##  maak een grafiek (plt.plot) van de data, geef hiervoor de lijsten met x en y waardes:
##  de optie -o zorgt ervoor dat de punten zelf worden getekend en verbonden met een lijn.
##  gebruik de optie label om een referentie aan te maken voor een legende


##  Hiermee laat je de grafiek uiteindelijk zien.
fig_d1.show()


### ---  Deel twee Uniforme distributies:




# Een nieuw figure aanmaken (zodat je ze allebei kan plotten)
fig_du = plt.figure('Uniforme Distributie')
#Hier je plots maken
fig_du.show()


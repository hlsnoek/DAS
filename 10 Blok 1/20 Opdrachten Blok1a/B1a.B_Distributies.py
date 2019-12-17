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
    kans = #math.pow(lamda,k)* math.exp(-lamda) / math.factorial(k)
    return kans

##  Print hier de resultaten voor k=1 en lambda=3:
print(poisson(1,3))

##  Genereer nu eerst een lijst met 40 punten van 1 t/40:
#x = [i for i in range(1,40)]

##  Vul de lijst met punten je voor elke punt P(k=i, lambda =3) berekend:
yp_3 = [poisson(i,3) for i in x]

##  Door eerst expliciet een figure aan te maken kunnen we meerdere plotjes maken.
#fig_d1 = plt.figure('Poisson Distributies')

##  maak een grafiek van de data, geef hiervoor de lijsten met x en y waardes:
##  de optie -o zorgt ervoor dat de punten zelf worden getekend en verbonden met een lijn.
##  de optie label maakt een referentie aan voor de legende
#plt.plot(x,yp_3,'-o',label='3')

##  Als je meerder grafieken wilt plotten kun je die toevoegen.
#plt.plot(x,yp_5,'-o',label='5')

##  Hiermee maak je de legende aan
#plt.legend()

##  Hiermee laat je de grafiek uiteindelijk zien.
#fig_d1.show()


### ---  Deel twee Uniforme distributies:

#fig_du = plt.figure('Uniforme Distributie')
#fig_du.show()


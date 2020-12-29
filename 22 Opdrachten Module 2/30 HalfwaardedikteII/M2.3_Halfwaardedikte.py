# Author: Hella Snoek en ...
# Date: Jan 2021
# Code for Data Analyse en Statistiek course

import DAS_DatasetGenerator as ds
import numpy as np
import matplotlib.pyplot as plt


halfdiktewaardes = []

for j in range(0,50) : 
    counts,diktes = ds.DataSetHalfwaardeDikte(j)
    # jouw code om de halfwaardedikte te vinden.
    # verzamel deze dan in een list:
    # halfdiktewaardes.append(d_half)
    

fig_d1 = plt.figure(1)
plt.hist(halfdiktewaardes, bins=len(diktes),range=(diktes[0],diktes[-1]))
fig_d1.show()

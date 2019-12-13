# Author: Hella Snoek
# Date: Nov 2019
# Code for Data Analyse en Statistiek course

import DAS_DatasetGenerator as ds
import numpy as np
import matplotlib.pyplot as plt

def berekenGemiddelde(dataset, n) :
    # schrijf hier je code die uit dataset het gemiddelde
    # uitrekent over de eerste n punten
    som =0
    gemiddelde = -1
    if n<5 : print('totale som is: %f \n het gemiddelde is: %f' % (som,gemiddelde))
    return gemiddelde

def maakSetGemiddeldes(dataset) :
    N = []
    gemiddeldes = []
#    for i in range(1,len(dataset)+1) :
    for i in range(1,4) :
        N.append(i)
        gemiddeldes.append(berekenGemiddelde(dataset,i))
    return N, gemiddeldes

def maakGrafiek(x,y) :
    graph = plt.plot(x, y, '-o')
    return graph

set_gauss = ds.DataSetGroteAantallen() 

# Schrijf hieronder je code om een histogram te maken van de set_gauss dataset.


# Schrijf hieronder je code om het gemiddelde over de eerste n punten uit te rekenen.
#mu = berekenGemiddelde(set_gauss, 2)
#print('mu')

# Schrijf hieronder de code om automatisch de gemiddeldes uit te rekenen 
#N, means = maakSetGemiddeldes(set_gauss) 



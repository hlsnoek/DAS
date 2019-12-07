import B1_DatasetGenerator as ds
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
#    for i in range(1,len(set_gauss)+1) :
    for i in range(1,4) :
        N.append(i)
        gemiddeldes.append(berekenGemiddelde(dataset,i))
    return N, gemiddeldes

def maakGrafiek(x,y) :
    graph = plt.plot(x, y, '-o')
    return graph

set_gauss = ds.DataSetGroteAantallen() 
N, means = maakSetGemiddeldes(set_gauss) 



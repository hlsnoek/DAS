# Author: Hella Snoek and ...
# Studentnummer: 
# Date: Dec 2019
# Code for UvA/VU Data Analyse en Statistiek course

import numpy as np
import matplotlib.pyplot as plt
import DAS_DatasetGenerator as ds

# Creeer een dataset met de DataSetMooiPlotten functie in DAS:
x = ds.DataSetMooiPlotten()

# Maak een histogram met de hist functie van MatPlotLib:
# Het aantal bins en de het bereik van de x-as wordt met de hand gekozen:
plt.hist(x, bins=31, range=(-100,100))

# Genereer as labels
plt.ylabel('aantal metingen')
plt.xlabel('waardes')

#sla het histogram op als een plaatje:
#plt.savefig('B1a.A_MooiPlotten.png')

# Laat het plaatje zien
plt.show()

# Opmerking: plt.savefig moet vòòr plot.show() aangeroepen
# worden. Na plt.show() wordt het plaatje namelijk
# verwijderd uit het geheugen.


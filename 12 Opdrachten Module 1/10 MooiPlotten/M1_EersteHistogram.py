# Author: Hella Snoek and ...
# Studentnummer: 
# Date: Jan 2024
# Code for UvA/VU Data Analyse en Statistiek course

import numpy as np
import matplotlib.pyplot as plt
import DAS_DatasetGenerator as ds

# Creeer een dataset met de DataSetEersteHistogram functie in DAS:
x = ds.DataSetEersteHistogram()

# Maak een histogram met de hist functie van MatPlotLib:
# Het aantal bins en de het bereik van de x-as wordt met de hand gekozen:
plt.hist(x, bins=31, range=(-100,100))

# Genereer as labels
plt.ylabel('aantal metingen')
plt.xlabel('waardes')

#sla het histogram op als een plaatje:
#plt.savefig('M1_EersteHistogram.png')

# Laat het plaatje zien
plt.show()

# Opmerking: plt.savefig moet voor plot.show() aangeroepen
# worden. Na plt.show() wordt het plaatje namelijk
# verwijderd uit het geheugen.


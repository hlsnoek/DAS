# Author: Hella
# Date: Nov 2019
# Code for Data Analyse en Statistiek course

import numpy as np
import matplotlib.pyplot as plt
import B1_DatasetGenerator as ds

x = ds.DataSetMooiPlotten()
plt.hist(x, bins=31, range=(-100,100))
plt.ylabel('aantal metingen')
plt.xlabel('waardes')
plt.show()
#plt.savefig('B1A_MooiPlotten.png')


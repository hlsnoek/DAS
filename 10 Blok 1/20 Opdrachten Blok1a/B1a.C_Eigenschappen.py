# Author: Hella Snoek en ...
# Studentnummer: 
# Date: Dec 2019
# Code for UvA/VU Data Analyse en Statistiek course

import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import random
import math as math
import DAS_DatasetGenerator as ds

def berekenEigenschappen(dataset) :
    # Bereken hier de eigenschappen
    # tip voor het vinden van de mediaan:
    #      De mediaan bevindt zich precies op helf van een gesorteerde list. ;)
    return avg, median, var, std, skew

dg = ds.genereerDistributieDG(500) 
mean, median, var, std, skew = berekenEigenschappen(dg)
print(mean, median, var, std,skew)


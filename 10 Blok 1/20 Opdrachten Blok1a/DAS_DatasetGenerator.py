# Author: Hella Snoek
# Date: Nov 2019
# Code for Data Analyse en Statistiek course

from random import seed
from random import random
import os
import math
import numpy as np

#Vul hier je studentnummer in
student_nummer = 9999

def checkSD() :
    if  student_nummer<10000 :
        print('\n ********************************************************************************************\n \n !!!!!!!! Je moet nog je student_nummer aanpassen in de B1_DatasetGenerator.py file !!!!!!!!\n \n********************************************************************************************\n \n')
        os._exit(1)
        

def DataSetMooiPlotten() :
    checkSD()
    mu = student_nummer%10
    sigma = ((student_nummer)%100)/10 + 1
    np.random.seed(1)
    x1 = np.random.normal(mu, sigma, size = 1000)
    x2 = np.random.normal(mu+2*sigma,sigma/2, size=300)
    x = np.append(x1,x2)
    return x

def DataSetGroteAantallen(s=1) :
    checkSD()
    mu = student_nummer%100
    sigma = (student_nummer%100)/10 + 1
    np.random.seed(s)
    set_gauss = np.random.normal(mu,sigma,size = 80)
    return set_gauss
    

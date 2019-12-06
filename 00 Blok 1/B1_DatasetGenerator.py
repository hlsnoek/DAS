# Author: Hella
# Date: Nov 2019
# Code for Data Analyse en Statistiek course

from random import seed
from random import random
import os
import math
import numpy as np

#Vul hier je studentnummer in
student_number = 9999

def checkSD() :
    if  student_number<10000 :
        print('\n ********************************************************************************************\n \n !!!!!!!! Je moet nog je student_nummer aanpassen in de B1_DatasetGenerator.py file !!!!!!!!\n \n********************************************************************************************\n \n')
        os._exit(1)
        

def DataSetMooiPlotten() :
#    checkSD()
    mu = student_number%10
    sigma = ((student_number+1)%100)/10
    np.random.seed(1)
    x1 = np.random.normal(mu, sigma, size = 1000)
    x2 = np.random.normal(mu+2*sigma,sigma/2, size=300)
    x = np.append(x1,x2)
    return x




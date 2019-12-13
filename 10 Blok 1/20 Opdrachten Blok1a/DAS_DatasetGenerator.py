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
random_getal = 9378

def checkSD() :
    if  student_nummer<10000 :
        print('\n ********************************************************************************************')
        print('\n !!!!!!!! Je moet nog je student_nummer aanpassen in de B1_DatasetGenerator.py file !!!!!!!!')
        print('********************************************************************************************\n \n')
        os._exit(1)
    else :
        random_getal = student_nummer
      
        
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
    
def BerekenExponent(dikte, d_half,I_0) :
    #    I_d = I_0 * (0.5)^{dikte/dikte_half}
    I_d = I_0 * (0.5)**(dikte/d_half)
    return I_d

def DataSetHalfwaardeDikte(s=1) :
    checkSD()
    I_0 = random_getal%100 + 100
    d_half = (random_getal%100)/1000 + 1.5
    print(d_half)
    np.random.seed(s)
    lood_dikte = 0.3 #(cm)
    metingen = []
    diktes = []
    for i in range(0,16) :
        diktes.append(lood_dikte*i)
        mu = BerekenExponent(lood_dikte*i, d_half,I_0)
        meting_i = np.random.poisson(mu)
        metingen.append(meting_i)
    return metingen,diktes

def DataSetHalfwaardeDikteVariatie(s=1,lood_dikte=0.3,N=15,meettijd=120) :
    checkSD()
    I_0 = (random_getal%100 + 100) * meettijd/120.
    d_half = (random_getal%100)/1000 + 1.5
    print(d_half)
    np.random.seed(s)
    metingen = []
    diktes = []
    for i in range(0,N+1) :
        diktes.append(lood_dikte*i)
        mu = BerekenExponent(lood_dikte*i, d_half,I_0)
        meting_i = np.random.poisson(mu)
        metingen.append(meting_i)
    return metingen,diktes

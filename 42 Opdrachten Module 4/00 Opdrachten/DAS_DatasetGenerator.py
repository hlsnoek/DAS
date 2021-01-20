# Author: Hella Snoek
# Date: Dec 2020
# Code for Data Analyse en Statistiek course

from random import seed
import random
import os
import math as m
import numpy as np

#Vul hier je studentnummer in
student_nummer = 9999
random_getal = 9378

def checkSD() :
    if  student_nummer<10000 :
        print('\n ********************************************************************************************')
        print('\n !!!!!!!! Je moet nog je student_nummer aanpassen in de DAS_DatasetGenerator.py file !!!!!!!!')
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

def genereerDistributieDG(n=500) :
    checkSD()
    mu = student_nummer%10 
    sigma = (student_nummer%100)/100 + 1
    np.random.seed(1)
    set_gauss = np.random.normal(mu,sigma,size = n)
    return set_gauss

def genereerDistributieDP(n=500) :
    checkSD()
    mu = student_nummer%10+1 
    np.random.seed(1)
    set_pois = np.random.poisson(mu,size = n)
    return set_pois


def DataSetGroteAantallen(s=1) :
    checkSD()
    mu = student_nummer%100 + 100
    sigma = (student_nummer%100)/10. + 1
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
    d_half = (random_getal%100)/1000. + 1.5
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


def DataSetHalfwaardeDikteVariatie(s=1,dtrue=-1,lood_dikte=0.3,meettijd=120,N=16) :
    checkSD()
    I_0 = (random_getal%100 + 100) * meettijd/120.
    if dtrue==-1 :
        d_half = ((random_getal%100)/1000. + 1.5)
    else : d_half = dtrue
    np.random.seed(s)
    metingen = []
    diktes = []
    for i in range(0,N+1) :
        diktes.append(lood_dikte*i)
        mu = BerekenExponent(lood_dikte*i, d_half,I_0)
        meting_i = np.random.poisson(mu)
        metingen.append(meting_i)
    return metingen,diktes,d_half

def datasetVogeltjes() :
    span_km = (25.5+22.5)/2
    span_km_s = (25.5-22.5)/2
    span_km_v = m.pow((span_km_s),2)

    m_km = (14+22)/2 
    m_km_s = (22-14)/2
    m_km_v = m.pow((m_km_s),2)

    span_pm = (20+17)/2
    span_pm_s = (20-17)/2
    span_pm_v = m.pow(span_pm_s,2)

    m_pm = (12+15)/2
    m_pm_s = (15-12)/2
    m_pm_v = m.pow(m_pm_s,2)

    np.random.seed(1)
    
    mu_km = [span_km, m_km]
    cov_km = [[span_km_v,0.3*span_km_s*m_km_s],[0.3*span_km_s*m_km_s,m_km_v]]
    span_km,m_km = np.random.multivariate_normal(mu_km,cov_km,30000).T

    mu_pm = [span_pm, m_pm]
    cov_pm = [[span_pm_v,0.3*span_pm_s*m_pm_s],[0.3*span_pm_s*m_pm_s,m_pm_v]]
    span_pm,m_pm = np.random.multivariate_normal(mu_pm,cov_pm,30000).T
    return m_km,span_km, m_pm, span_pm

def meetMassaMeesje() :
    return (10,11)

def meetLengteMeesje() :
    return (21,22)

def GroteAantallenStdGenerator() :
    checkSD()
    N = [1,2,5,10,60]
    sigma = (student_nummer%100)/10. + 1
    print(sigma)
    std = [np.random.normal(sigma/np.sqrt(ni),sigma/np.sqrt(ni)/np.sqrt(200)) for ni in N]
    std_err = [s/np.sqrt(200) for s in std]
    return 1/np.sqrt(N),std,std_err

def GroteAantallenStdTrue() :
    return (student_nummer%100)/10. + 1

def GroteAantallenFitSetGenerator() :
    checkSD()
    N = [1,2,5,10,60]
    sigma = (student_nummer%100)/10. + 1
    std = [np.random.normal(sigma/np.sqrt(ni),sigma/np.sqrt(ni)/np.sqrt(200)) for ni in N]
    std_err = [(std[0])/np.sqrt(200) for s in range(0,len(std))]
    return 1/np.sqrt(N),std,std_err
    
def onbekendeFunctie(x) :
    f = 40+5*m.sin((0.5*x)+5)
    return f

def OnbekendeFunctieGenerator() :
    checkSD()
    np.random.seed(1)
    x = np.arange(0,10,1)
    y = [np.random.poisson(onbekendeFunctie(xi)) for xi in x]
    yerr = np.sqrt(y)
    return x,y,yerr

def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*m.pi*var)**.5
    num = m.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def DeeltjesDataset() :
    checkSD()
    np.random.seed(1)
    mu = 100+student_nummer%100
    x = np.arange(80,220,5)
    y1 = np.random.poisson(400* (0.5)**(x/100))
    y2 = [np.random.poisson(150*5*normpdf(xi,mu,5)) for xi in x]
    return x, y1+y2, np.sqrt(y1+y2)

def SpiekenM0() :
    checkSD()
    return 100+student_nummer%100

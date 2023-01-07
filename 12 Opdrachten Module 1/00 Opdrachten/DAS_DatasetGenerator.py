# Author: Hella Snoek
# Date: Jan 2023
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
    global random_getal
    if  student_nummer<10000 :
        print('\n ********************************************************************************************')
        print('\n !!!!!!!! Je moet nog je student_nummer aanpassen in de DAS_DatasetGenerator.py file !!!!!!!!')
        print('********************************************************************************************\n \n')
        os._exit(1)
    else :
        random_getal = student_nummer
      
        
def DataSetMooiPlotten() :
    checkSD()
    mu = random_getal%10
    sigma = ((random_getal)%100)/10 + 1
    np.random.seed(1)
    x1 = np.random.normal(mu, sigma, size = 1000)
    x2 = np.random.normal(mu+2*sigma,sigma/2, size=300)
    x = np.append(x1,x2)
    return x

def genereerDistributieDG(n=500) :
    checkSD()
    mu = random_getal%10 
    sigma = (random_getal%100)/100 + 1
    np.random.seed(1)
    set_gauss = np.random.normal(mu,sigma,size = n)
    return set_gauss

def genereerDistributieDP(n=500) :
    checkSD()
    mu = random_getal%10+1 
    np.random.seed(1)
    set_pois = np.random.poisson(mu,size = n)
    return set_pois


def DataSetGroteAantallen(s=1) :
    checkSD()
    mu = random_getal%100 + 100
    sigma = (random_getal%100)/10. + 1
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

def datasetVogels() :
    span_br = (155+195)/2
    span_br_s = (195-155)/2
    span_br_v = m.pow((span_br_s),2)

    m_br = (1020+2080)/2 
    m_br_s = (2080-1020)/3.5
    m_br_v = m.pow((m_br_s),2)

    span_pr = (120+152)/2
    span_pr_s = (152-120)/2
    span_pr_v = m.pow(span_pr_s,2)

    m_pr = (500+1350)/2
    m_pr_s = (1350-500)/3.5
    m_pr_v = m.pow(m_pr_s,2)

    np.random.seed(1)
    
    mu_br = [span_br, m_br]
    cov_br = [[span_br_v,0.65*span_br_s*m_br_s],[0.65*span_br_s*m_br_s,m_br_v]]
    span_br,m_br = np.random.multivariate_normal(mu_br,cov_br,5000).T

    mu_pr = [span_pr, m_pr]
    cov_pr = [[span_pr_v,0.5*span_pr_s*m_pr_s],[0.5*span_pr_s*m_pr_s,m_pr_v]]
    span_pr,m_pr = np.random.multivariate_normal(mu_pr,cov_pr,5000).T
    return m_br,span_br, m_pr, span_pr

def meetMassaReiger() :
    return (1300,1350)

def meetLengteReiger() :
    return (130,145)

def GroteAantallenStdGenerator() :
    checkSD()
    N = [1,2,5,10,60]
    np.random.seed(1)
    sigma = (random_getal%100)/10. + 1
    std = [np.random.normal(sigma/np.sqrt(ni),sigma/np.sqrt(ni)/np.sqrt(200)) for ni in N]
    std_err = [s/np.sqrt(200) for s in std]
    return 1/np.sqrt(N),std,std_err

def GroteAantallenStdTrue() :
    return (random_getal%100)/10. + 1

def GroteAantallenFitSetGenerator() :
    checkSD()
    N = [1,2,5,10,60]
    np.random.seed(1)
    sigma = (random_getal%100)/10. + 1
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
    mu = 100+random_getal%100
    x = np.arange(80,220,5)
    y1 = np.random.poisson(400* (0.5)**(x/100))
    y2 = [np.random.poisson(150*5*normpdf(xi,mu,5)) for xi in x]
    return x, y1+y2, np.sqrt(y1+y2)

def SpiekenM0() :
    checkSD()
    return 100+random_getal%100

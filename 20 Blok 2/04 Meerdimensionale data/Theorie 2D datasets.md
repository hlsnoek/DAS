# Multidimensionale data

1. Ordered TOC
{:toc}

Het komt vaak voor dat we datasets hebben waarbij we meerdere variabelen tegelijkertijd hebben gemeten. Bijvoorbeeld als een steekproef doen onder de bevolking waarbij we allerlei gegevens tegelijkertijd opvragen zoals leeftijd, inkomen, gezinssamenstelling etc. Ook in natuurkundige experimenten komen multidimensionele datasets veel voor. 

Voor elke variabelen kunnen we het gemiddelde en de standaard deviatie meten met behulp van de formules die we in ['Basisbegrippen'](/blok-1/theorie-basisbegrippen) hebben geïntroduceerd. Echter we kunnen nu ook kijken naar hoe en of de waarde van een variable afhangt van een andere variabel in de dataset. Dit noemen we correlatie. Ook kunnen we bereken of een spreiding in een variable afhangt van de waarde van een andere variabele. We noemen die co-variantie. Hieronder introduceren we eerst co-variantie, daaronder komt correlatie aan bod.


## Variantie en covariantie

De variantie geeft zoals eerder besproken (onder ['Basisbegrippen'](/blok-1/theorie-basisbegrippen)) een maat voor
de spreiding van een dataset aan. Bij een 2D dataset waarbij een variabele wordt aangegeven op de $$x$$-as en een andere
variabelen op de $$y$$-as wordt de mate van spreiding o.a. aangegeven met de *covariantie*.

De covariantie bij een 2D dataset geeft aan in welke mate de data verspreid is over het twee dimensionale vlak.

Voor twee variabelen $$x$$ en $$y$$ wordt de covariantie aangeduid met $$cov(x,y)$$ en gegeven door:

$$cov(x,y) = E((x-E_x)(y-E_y))$$

Hier staat $$E$$ voor de *verwachtingswaarde*. De verwachtingswaarde voor
$$x$$ en $$y$$ worden respectievelijk aangegeven met $$E_x$$ en $$E_y$$. De formule geeft dus aan dat de covariantie gelijk is aan de verwachtingswaarde van het verschil tussen de waarde van de variabele $$x$$ en de verwachtingswaarde van $$x$$ vermenigvuldigd met het verschil tussen de variabele $$y$$ en de verwachtingswaarde van $$y$$.

Als voor waardes $$x$$ die bovengemiddeld zijn, overwegend samen gaan met relatief hoge waardes van $$y$$, dan hebben we te maken met een positieve 
waarde voor de covariantie. Als de waarden voor relatief hoge waardes van $$x$$ de waardes van $$y$$ voornamelijk onder de verwachtingswaarde liggen, dan is de covariantie ook negatief.

De covariantie geeft dus aan in hoeverre waarden van de ene variabele toenemen/afnemen bij toenemende waarden van de andere variabele. De co-variantie is een heel nuttige maat maar lastig te interpreteren vanwege de dimensies die, net als bij de variantie, niet dezelfde zijn als de variabelen zelf. Eenvoudiger is om naar de correlatie co-efficient te kijken. 



## Correlatie 

De correlatiecoëfficiënt $$\rho$$ is gedefinieerd als:

$$\rho_{x,y} = \frac{cov_{x,y}}{\sigma_x \sigma_y}$$  

Hierbij is $$cov_{x,y}$$ de covariantie tussen variabele $$x$$ en variabele $$y$$, en zijn $$\sigma_x$$ en $$\sigma_y$$ de standaardafwijkingen van variabele $$x$$ en $$y$$ respectievelijk.

Als er geen correlatie is tussen de twee variabelen, dan is
correlatiecoëfficiënt gelijk aan nul. Is de correlatiecoëfficiënt tussen de twee variabelen gelijk aan $$1$$ of aan $$-1$$ dan zijn de twee
variabelen maximaal afhankelijk. In het geval van een correlatiecoëfficiënt gelijk aan $$1$$ is dit een positief lineair verband, in het geval van een correlatiecoëfficiënt gelijk aan $$-1$$ is dit een lineair verband met negatieve helling. 

Hieronder zijn een aantal 2D datasets weergegeven met verschillende correlatiecoëfficiënten:

Dataset met een correlatiecoëfficiënt $$\rho_{x,y} = 0 $$:

<p align="center">![](Plot1_Correlatie_0.png){:width="60%"}</p>

Dataset met een correlatiecoëfficiënt $$\rho_{x,y} = 1 $$:

<p align="center">![](Plot1_Correlatie1.png){:width="60%"}</p>

Dataset met een correlatiecoëfficiënt $$\rho_{x,y} = -1 $$:

<p align="center">![](Plot1_Correlatie_min1.png){:width="60%"}</p>

Datasets met een correlatiecoëfficiënt $$\rho_{x,y} = -0.8$$ en $$\rho_{x,y} = 0.8$$:

<p align="center">![](Plot1_Correlatie_min0punt8.png){:width="35%"}![higgs](Plot1_Correlatie_0punt8.png){:width="35%"}</p>

Datasets met een correlatiecoëfficiënt $$\rho_{x,y} = -0.3$$ en $$\rho_{x,y} = 0.3$$:

<p align="center">![](Plot1_Correlatie_min0punt3.png){:width="35%"}![higgs](Plot1_Correlatie_0punt3.png){:width="35%"}</p>


Hoe dichter de correlatiecoëfficiënt bij een waarde van $$1$$ of $$-1$$ zit des te groteris de afhankelijkheid van de variabelen. Hoe te dichter de correlatiecoëfficiënt bij nul zit des te kleiner is de correlatie tussen de variabelen.

Er zijn meerdere 'spelletjes' op internet waarbij je kunt oefenen met het herkennen ne raden van de correlatiecoëfficiënt
van twee variabelen. Kijk bijvoorbeeld eens bij [Geogebra-Correlatie game](https://www.geogebra.org/m/KE6JfuF9) of 
[Guess the correlation](http://guessthecorrelation.com/)












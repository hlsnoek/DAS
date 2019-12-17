## B1a.C Eigenschappen van distributies **

In deze opdracht gaan we kijken naar de [eigenschappen](XX link) van distributies en deze veranderen als een [translatie](xx link) of [vermenigvuldiging](xx link) toepast. We kijken naar de normaal en poisson distributies. <br>

#### Normale distributie
Je krijgt een Gaussische dataset $$dg(x)$$ met 500 punten. <br>

 			ds.genereerDistributieDG(500) 

> 1. Download het bestand [B1a.C_Eigenschappen.py](B1a.C_Eigenschappen.py) zorg dat deze in dezelfde folder staat as het **DAS_DatasetGenerator.py** bestand. <br>
> Schrijf nu een functie die de volgende punten uitrekent voor deze 
> dataset:<br> 
>
>	* het gemiddelde
> 	* de mediaan
> 	* de variantie
> 	* de standaard deviate
> 	* de skewness
>
> **NB:** Het is de bedoeling dat je de formules zelf programmeert. Je mag geen gebruik maken van standaard pakketen van python die dit doen.
>
> 2. Wat verwacht je als je een dataset met 2 maal zoveel waardes (1000) krijgt? Probeer dit nu uit. Klopt het resultaat met je verwachting?

We gaan nu kijken naar het effect van een translatie van de dataset.

> 1. Genereer een nieuwe dataset en manipuleer de waardes in de dataset met de volgende translatie: <br>
> $$ x' = x + 2$$<br>
> 2. Plot nu de originele en de getransleerde dataset over elkaar heen.
> 
> 3. Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Nu gaan we kijken naar het effect van een multiplicatie van x.

> 1. Neem nu de originele dataset en manipuleer de waardes met de volgende multiplicatie: <br>
>  $$ x' = 2x$$
> 2. Plot nu de gemultipliceerde dataset toe aan aan je plot zodat je de originele, de translatie en multiplicatie in 1 figuur ziet. 
> 
> 3. Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

#### Poisson
We gaan nu kijken wat het effect is van translatie en multiplicatie op een poisson distributie.

> 1. Genereer een dataset $$dp$$ met 500 punten: <br>
> 
> 			ds.genereerdistributieDP(500)
> 

We kijken eerst weer naar de effecten van een translatie: 

> 1. Genereer een nieuwe dataset en manipuleer de waardes in de dataset met de volgende translatie: <br>
> $$ x' = x + 2$$<br>
> 2. Plot nu de originele en de getransleerde dataset over elkaar heen.
> 
> 3. Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Nu gaan we kijken naar het effect van een multiplicatie van x.

> 1. Neem nu de originele dataset en manipuleer de waardes met de volgende multiplicatie: <br>
>  $$ x' = 2x$$
> 2. Plot nu de gemultipliceerde dataset toe aan aan je plot zodat je de originele, de translatie en multiplicatie in 1 figuur ziet. 
> 
> 3. Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Tot slot: 

> Voeg al je resultaten en je code toe aan het inlevertemplate.

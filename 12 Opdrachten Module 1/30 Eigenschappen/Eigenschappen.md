## M1.3 - Eigenschappen van distributies **

In deze opdracht gaan we kijken naar de [eigenschappen](/module-1/basisbegrippen) van distributies en deze veranderen als een translatie of vermenigvuldiging toepast. We kijken naar de Normaal en poisson distributies. <br>

#### Normale distributie
Je krijgt een Gaussische dataset $$\text{dg}(x)$$ met 500 punten. <br>

 			dg = ds.genereerDistributieDG(500) 

Download het bestand [M1.3_Eigenschappen.py](M1.3_Eigenschappen.py) zorg dat deze in dezelfde folder staat as het **DAS_DatasetGenerator.py** bestand. <br>

> * Schrijf nu een functie die de volgende punten uitrekent voor deze dataset:
> 	* het gemiddelde
> 	* de mediaan
> 	* de variantie
> 	* de standaard deviatie
>
> * Wat verwacht je dat er gebeurd met deze variabelen als je een dataset met 2 maal zoveel waardes (1000) krijgt? Quantificeer je resultaat. Probeer dit nu uit. Klopt het resultaat met je verwachting?<br> 
> 
> **NB:** Het is de bedoeling dat je de formules zelf programmeert. Je mag geen gebruik maken van standaard functies van python die dit direct voor je teruggeven. Uiteraard mag je wel gebruiken maken van functies als *len()* en *sort()*.

We gaan nu kijken naar het effect van een translatie van de dataset.

> * Genereer een nieuwe dataset en manipuleer de waardes in de dataset met de volgende translatie: <br>
> $$ x' = x + 2$$<br>
> * Plot nu de originele en de getransleerde dataset over elkaar heen.
> 
> * Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Nu gaan we kijken naar het effect van een multiplicatie van x.

> * Neem nu de originele dataset en manipuleer de waardes met de volgende multiplicatie: <br>
>  $$ x' = 2x$$
> * Plot nu de gemultipliceerde dataset toe aan aan je plot zodat je de originele, de translatie en multiplicatie in 1 figuur ziet. 
> 
> * Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen. Presenteer je resultaten in een tabel op het inlevertemplate. 

#### Poisson
We gaan nu kijken wat het effect is van translatie en multiplicatie op een poisson distributie.

> * Genereer een dataset $$dp$$ met 500 punten: <br>
> 
> 			dp = ds.genereerDistributieDP(500)
> 
> * Bepaal dezelfde eigenschappen van deze distributie als dat je voor de Normale distributie hebt gedaan.
> * Wat verwacht je als je een dataset met 2 maal zoveel waardes (1000) krijgt? Quantificeer je resultaat. Probeer dit nu uit. Klopt het resultaat met je verwachting?<br> 

We kijken eerst weer naar de effecten van een translatie: 

> * Genereer een nieuwe dataset en manipuleer de waardes in de dataset met de volgende translatie: <br>
> $$ x' = x + 2$$<br>
> * Plot nu de originele en de getransleerde dataset over elkaar heen.
> 
> * Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Nu gaan we kijken naar het effect van een multiplicatie van x.

> * Neem nu de originele dataset en manipuleer de waardes met de volgende multiplicatie: <br>
>  $$ x' = 2x$$
> * Plot nu de gemultipliceerde dataset toe aan aan je plot zodat je de originele, de translatie en multiplicatie in 1 figuur ziet. 
> 
> * Welke van de eigenschappen verwacht je dat er veranderen? Controleer dit door voor de originele en getransleerde dataset alle variabelen uit te rekenen.

Tot slot: 

> Voeg al je resultaten en je code toe aan je inlever document.

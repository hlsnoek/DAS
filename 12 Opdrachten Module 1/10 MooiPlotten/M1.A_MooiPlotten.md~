
## Opdracht M1.A - Mooi Plotten *

We gaan in deze opdracht een histogram maken van een gegeven dataset. <br>
Je krijgt hiervoor een python programmaatje dat je moet aanpassen. <br>
We gaan ervan uit dat je Anaconda en Visual Studio Code (VSC) hebt geïnstalleerd. <br>
Zo niet zie dan [hier](/informatie/installatie) de instructies.<br>


>Installeer de volgende twee bestanden naar een werkfolder op je computer:<br>
 [M1.A_MooiPlotten.py](M1.A_MooiPlotten.py)
 en [DAS_DatasetGenerator.py](DAS_DatasetGenerator.py).
 Open de bestanden in het VSCode programma.

In het *M1.A_MooiPlotten.py* wordt eerst een dataset aangemaakt met de volgende regel:

	x = ds.DataSetMooiPlotten()

Helemaal boven in de code vind je de regel:

	import DAS_DatasetGenerator as ds	

en zo weet je dat *DataSetMooiPlotten()* een functie is die in *DAS_DatasetGenerator.py* is gedefinieerd.
Om dit bestand te kunnen runnen moet je eerst je studentnummer invoeren in dit bestand.

> Open *DAS_DatasetGenerator.py*, vind de student_nummer variabele en  voer hier je studentnummer in. Nu kun je het bestand *M1.A_MooiPlotten.py* runnen. Kijk goed naar je output.

Je hebt nu je eerste histogram gemaakt van jouw eigen dataset *x*. Een histogram is een manier om data te presenteren. Er bestaan 1-dimensionale, 2- en 3- dimensionale histogrammen. Lees [hier](/module-1/data-visualiseren) meer over histogrammen. 

We gaan nu het histogram zo maken dat de dataset *x* ook goed 'leesbaar' is. Vooralsnog is van het histogram niet heel duidelijk hoe de distributie van *x* eruit ziet. De bedoeling is dat als we naar het histogram kijken, we meteen een goed idee krijgen van de distributie van *x*. 

De volgende regel code vind je in *M1.A_MooiPlotten.py*:

	plt.hist(x, bins=31, range=(-100,100))

Dit is de regel code waar het histogram wordt aangemaakt. 
Als je helemaal boven in de code kijkt zie je de volgende regel:

	import matplotlib.pyplot as plt

De hist functie wordt dus gedefinieerd in de matplotlib library. Dat is handig om te weten als je meer over deze library te weten wilt komen. Je kan bijvoorbeeld veel vinden over de verschillende plot mogelijkheden door op "matplotlib" en "hist" te zoeken op het web.


Je ziet dat behalve de dataset *x* dat er ook twee opties worden meegegeven (bins en range). De range geeft aan welk bereik de x-as van het histogram heeft. De andere variabele, bins, geeft aan in hoeveel delen deze x-as is opgedeeld. <br>
Deze twee opties kun je eventueel weglaten. In dat geval zoekt python zelf, met behulp van een algoritme een range en aantal bins uit. Je zult zien dat dat niet altijd optimaal werkt. 

> Probeer nu de default binning van de hist functie uit door de *bins* en *range* opties weg te laten.

Ook in dit geval is de representatie van de dataset niet optimaal. We gaan dus de range en de binning zelf optimaliseren. De bedoeling is dat het histogram goed interpreteerbaar wordt. Door te fijne binning (veel bins in een kleine range) wordt de dataset heel grillig, het wordt dan lastig om de distributie te herkenen en trends goed te kunnen zien. Hetzelfde gebeurt als de binning te grof is. Er bestaat meestal niet een enkele goede instelling maar een gebied waarin het goed uitpakt. 

> Pas nu de binning en de range aan zodat de distributie van *x* goed zichtbaar is. Let hierbij goed op of de binning niet te grof of te fijn is. 
Valt er iets op aan de distributie?
<br> **TIP**: Het is makkelijker om eerst de range goed af te stellen en dan pas de binning waarde te veranderen. Als je meer controle wilt hebben over waar de assen beginnen en eindigen kun je gebruik maken van de **plt.xlim(min,max)** functie. 

Als je een goede binning en range combinatie hebt gevonden waarin de kenmerken van de distributie goed zichtbaar zijn, is het goed om nog een keer te kijken naar de leesbaarheid van de *x*-as. Het is prettig als de bins een eenvoudig te lezen fractie hebben van de streepjes op de *x*-as. Dus als je een range hebt van 2 tot 12, is het onhandig om die in 13 stukjes op te delen. Prettiger is bijvoorbeeld 2, 4, 5 of 10. Dat is het histogram eenvoudiger leesbaar. Misschien heb jij wel veel meer bins nodig, of een grotere range.

> Pas als laatste nog de binning aan zodat ook de bin-breedtes eenvoudig zijn af te lezen - maar zorg dat de kenmerken van de distributie van *x* ook goed zichtbaar blijven. 

**TIP**: Als je het lastig vindt om te begrijpen wat 'kenmerken' zijn van de distributie is het het handigste om even te spelen met de waardes en goed naar de data te kijken. Het is nooit voorspelbaar hoe een dataset eruit ziet (en dus wat de belangrijke kenmerken zijn). Typisch wil je wel weten hoe breed de verdeling is, waar hij begint en waar hij ophoudt. Ook als deze bijvoorbeeld asymmetrisch is, is het wel belangrijk dat dat zichtbaar is in het histogram.

Als je tevreden bent met het resultaat kun je het histogram opslaan door de laatste regel code te activeren: 

	plt.savefig('M1.A_MooiPlotten.png')   

Je resultaten moet je inleveren via ANS en worden beoordeeld. Kijk [hier](/informatie/inleveropdrachten) voor de deadlines van de inleveropdrachten. 

> Kopieer nu je **histogram** en je **code** in het document. <br>
Is je iets opgevallen aan de distributie? - Schrijf dit dan ook op.

**Let op!** Je mag dus niet de automatische binning gebruiken van matplotlib.<br>
Je moet expliciet de bin en range opties gebruiken in je code.



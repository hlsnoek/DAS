## M1.1 - Mooi Plotten *
<!--REF\label{/opdrachten-module-1/mooiplotten}-->

We beginnen dit vak met een eenvoudige opdracht. We gaan in deze opdracht een histogram goed leesbaar maken. Lees eerst het stuk je over [Data visualiseren](/module-1/data-visualiseren), daar vind je ook de richtlijnen waaraan een goed histogram voldoet.

<!--COMMENT\iffalse-->
Je krijgt hiervoor een python programmaatje dat je moet aanpassen.  
We gaan ervan uit dat je Anaconda en Visual Studio Code (VSC) hebt geïnstalleerd. Zo niet zie dan [hier](/informatie/installatie) de instructies.

De dikgedrukte vragen die je in deze opdracht vindt moet je uiteindelijke ook invullen op het [inlevertemplate](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/00%20Opdrachten/InlevertemplateModule1.docx). De rest van de opdracht moet je uitvoeren om de vragen correct te kunnen beantwoorden dus sla de rest niet zomaar over! In deze opdracht zijn er twee dikgedrukte vragen en staan ze helemaal onderaan. In andere opdrachten vind je ze vaak tussendoor.

<!--COMMENT\fi-->

> Installeer de volgende twee bestanden naar een werkfolder op je computer [M1.1_MooiPlotten.py](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/10%20MooiPlotten/M1.1_MooiPlotten.py) en [DAS_DatasetGenerator.py](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/00%20Opdrachten/DAS_DatasetGenerator.py).

Open de bestanden in het VSCode programma en lees de code. We zullen hieronder wat uitleg over de code geven. 

In `M1.1_MooiPlotten.py` wordt eerst een dataset aangemaakt met de volgende regel:

	x = ds.DataSetMooiPlotten()

Helemaal boven in de code vind je de regel:

	import DAS_DatasetGenerator as ds	

en zo weet je dat **`DataSetMooiPlotten()`** een functie is die in **`DAS_DatasetGenerator.py`** is gedefinieerd.
Om dit bestand te kunnen runnen moet je eerst je studentnummer invoeren in de DAS_DatasetGerator.

> Open het bestand `DAS_DatasetGenerator.py`, vind de **`student_nummer`** variabele in regel 12 en voer hier je studentnummer in. 


Nu kun je het bestand `M1.1_MooiPlotten.py` runnen. Kijk goed naar je output.

Je hebt nu je eerste histogram gemaakt van jouw eigen dataset *x*. Een histogram is een manier om data te presenteren. Er bestaan 1-dimensionale, 2- en 3- dimensionale histogrammen. Lees [hier](/module-1/data-visualiseren) meer over histogrammen. 

We gaan nu het histogram zo maken dat de dataset *x* ook goed 'leesbaar' is. Vooralsnog is van het histogram niet heel duidelijk hoe de distributie van *x* eruit ziet. De bedoeling is dat als we naar het histogram kijken, we meteen een goed idee krijgen van de distributie van *x*. 

>Voor we iets gaan veranderen in  `M1.1_MooiPlotten.py`, voer eerst je naam en je studentnummer in de eerste regels van dat bestand. 

Je moet de code uiteindelijk ook inleveren. We gebruiken deze bij het nakijken om, als er een fout is gemaakt in de opdracht te kunnen bekijken waar die vandaan komt. Het is natuurlijk ook de bedoeling dat de resultaten die je inlevert overeenkomen met de resultaten uit je programmaatje. Daar kijken we ook naar.

In `M1.1_MooiPlotten.py` vind je de volgende regel code:

	plt.hist(x, bins=31, range=(-100,100))

Dit is de regel code waar het histogram wordt aangemaakt. 
Als je helemaal boven in de code kijkt zie je de volgende regel:

	import matplotlib.pyplot as plt

De **`hist`** functie wordt dus gedefinieerd in de **`matplotlib`** library. Dat is handig om te weten als je meer over deze library te weten wilt komen. Je kan bijvoorbeeld veel vinden over de verschillende plot mogelijkheden door op "matplotlib" en "hist" te zoeken op het web.


Je ziet dat behalve de dataset *x* er ook twee opties worden meegegeven (**`bins`** en **`range`**). De range geeft aan welk bereik de x-as van het histogram heeft. De andere variabele, bins, geeft aan in hoeveel delen deze x-as is opgedeeld.  
Deze twee opties kun je eventueel weglaten. In dat geval zoekt python zelf, met behulp van een algoritme een range en aantal bins uit. Je zult zien dat dat niet altijd optimaal werkt. 

> Probeer nu de default binning van de hist functie uit door de **`bins`** en **`range`** opties weg te laten. Kijk goed naar de waardes op de x-as en waar de kolommen precies starten en ophouden. 

Ook in dit geval is de representatie van de dataset niet optimaal. We gaan dus de range en de binning zelf optimaliseren. De bedoeling is dat het histogram goed interpreteerbaar wordt. Door te fijne binning (veel bins in een kleine range) wordt de dataset heel grillig, het wordt dan lastig om de distributie te herkennen en trends goed te kunnen zien. Hetzelfde gebeurt als de binning te grof is. Er bestaat meestal niet een enkele goede instelling maar een gebied waarin het goed uitpakt. 

> Pas nu de binning en de range aan zodat de distributie van *x* goed zichtbaar is. Let hierbij goed op of de binning niet te grof of te fijn is. 

Het is makkelijker om eerst de range goed af te stellen en dan pas de binning waarde te veranderen. Als je meer controle wilt hebben over waar de assen beginnen en eindigen kun je gebruik maken van de **`plt.xlim(min,max)`** functie. 

> Voeg de **`plt.xlim(min,max)`** functie toe aan je code (voor het **`show`** commando) en kies geschikte waardes. Stem hierna nogmaals de binning af. 

Als je een goede binning en range combinatie hebt gevonden waarin de kenmerken van de distributie goed zichtbaar zijn, is het goed om nog een keer te kijken naar de leesbaarheid van de *x*-as. Het is prettig als de bins een eenvoudig te lezen fractie hebben van de streepjes op de *x*-as. Dus als je een range hebt van 2 tot 12, is het onhandig om die in 13 stukjes op te delen. Prettiger is bijvoorbeeld 2, 4, 5 of 10. Dat is het histogram eenvoudiger leesbaar. Misschien heb jij wel veel meer bins nodig, of een grotere range.

> Pas als laatste nog de binning aan zodat ook de bin-breedtes eenvoudig zijn af te lezen - maar zorg dat de kenmerken van de distributie van *x* ook goed zichtbaar blijven. 

**TIP**: Als je het lastig vindt om te begrijpen wat 'kenmerken' zijn van de distributie is het het handigste om even te spelen met de waardes en goed naar de data te kijken. Het is nooit voorspelbaar hoe een dataset eruitziet (en dus wat de belangrijke kenmerken zijn). Typisch wil je wel weten hoe breed de verdeling is, waar hij begint en waar hij ophoudt. Ook als deze bijvoorbeeld asymmetrisch is, is het wel belangrijk dat dat zichtbaar is in het histogram.

Als je tevreden bent met het resultaat kun je het histogram opslaan door de laatste regel code te activeren: 

	plt.savefig('M1.1_MooiPlotten.png')   

> Open nu het [inlevertemplate](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/00%20Opdrachten/InlevertemplateModule1.docx) voor Module 1 en beantwoord de volgende twee vragen. 
> 
> **M1.1a)  Plaats hier je histogram.**    <br><br>
>   
> **M1.1b) Valt je iets op aan de data? Probeer het te omschrijven.**

Als je alle andere opdrachten voor module 1 ook hebt gemaakt kun je de opdrachten en code inleveren via de ANS website. Bij de laatste opgave voor module 1 vind je hier meer informatie over. Zorg in elk geval dat je de code die je hier hebt gemaakt bewaard.

**Let op!** Je mag dus niet de automatische binning gebruiken van **`matplotlib`**; Je moet expliciet de **`bin`** en **`range`** opties gebruiken in je code.



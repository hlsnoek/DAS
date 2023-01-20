## M1.1 - Kansdichtheid distributies **
<!--REF\label{/opdrachten-module-1/distributies}-->

We gaan in deze opgave kijken naar kansdichtheid distributie. 
Lees eerst [hier](/module-1/verdelingsfuncties) meer over kansdichtheidsdistributies. Er zijn een paar belangrijke en bekende distributies. We gaan in deze opgave aan de slag met de <a href="/module-1/verdelingsfuncties#Poisson">poisson</a>  en  <a href="/module-1/verdelingsfuncties#Uniform">uniforme</a>  distributies.

De dikgedrukte vragen die je in deze opdracht vindt moet je uiteindelijke ook invullen op het [inlevertemplate](https://das.proglab.nl/course/12%20Opdrachten%20Module%201/00%20Opdrachten/InlevertemplateModule1.docx). De rest van de opdracht moet je uitvoeren om de vragen correct te kunnen beantwoorden dus sla de rest niet zomaar over! In deze opdracht zijn er twee dikgedrukte vragen en staan ze helemaal onderaan. In andere opdrachten vind je ze vaak tussendoor.


### Poisson distributie

> **MM1.1a) Reken (met de hand) de volgende Poisson kansen uit: $$P(k=1, \lambda=4)$$, $$P(k=2, \lambda =4)$$ en $$P(k=3, \lambda=4)$$. Kijk goed wat $$\lambda$$ en $$k$$ eigenlijk betekenen en wat de verwachtingswaarde is en wat de geobserveerde waarde is. Schrijf niet alleen het antwoord op maar begin bij de formule en werk het dan uit. Let ook op de regels van de notatie. Bekijk hiervoor het stukje over significantie in het hoofdstuk [notatie](/module-1/notatie).**

De Poisson distributie is één van de belangrijkste distributies. We zullen hem vaak tegen gaan komen.
We gaan nu Poisson distributies met python grafisch weergeven. Download het bestand [M1.1_Distributies.py](https://das.proglab.nl/course/12%20Opdrachten%20Module%201/20%20Distributies/M1.1_Distributies.py).


> Maak eerst een functie die de Poisson kans uitrekent. De bedoeling is dat je de functie $$k$$ en $$\lambda$$ meegeeft en deze de Poisson kans teruggeeft. In het bestand vind je al een lege functie die je kunt invullen.  

 **TIP** De macht, de exponentieel en de faculteit die in de formule voorkomen kun je makkelijk uitrekenen met het **`math`** pakket in python. 
 
	import math as math
 		
	math.pow(lamda,k)  ## dit geeft lamda^k  
	math.exp(-lamda)   ## geeft e^{-lamda}   
	math.factorial(k)  ## geeft k!  
 
 <!--comment: lamda hierboven niet veranderen in lambda!!-->
 
> - Reken nu de kansen $$P(k=1,\lambda=4)$$, $$P(k=2,\lambda =4)$$ en $$P(k=3,\lambda=4)$$, uit met je python functie. Komt het overeen met de waardes die je eerder met de hand berekende? Check het resultaat.
>
> - Maak vervolgens een Poisson-kansdichtheidsdistributie voor $$\lambda = 5$$. Doe dit door eerst een lijst aan te maken met $$x$$ waardes tussen 1 en 40 (met stapjes van 1) en vervolgens voor elk punt de kans uit te rekenen met de functie en deze op te slaan in een lijst. Maak vervolgens een grafiek met de resultaten. Zorg dat je grafiek er netjes uitziet. Ziet de grafiek eruit zoals je had verwacht? 
> 
> - **M1.1b) Maak nu een grafiek waarin je de Poisson distributies voor $$\lambda = 2, 5, 10$$ en $$20$$ laat zien. Maak 1 grafiek met de 4 resultaten. Zorg dat je de grafiek leesbaar maakt, bekijk hiervoor de richtlijnen in het hoofdstuk [data visualisatie](/module-1/data-visualiseren).** <br><br>
>
> - **M1.1c) Lees af in je grafiek hoe groot de kans is om een waarde van 4 te vinden voor de vier verschillende verwachtingswaarden. NB je kan het natuurlijk ook uitrekenen met je functie.**



### Uniforme distributie
We gaan nu kijken naar de uniforme distributie en simuleren een experiment dobbelstenen gooien. We gaan ervan uit dat we een zuivere dobbelsteen hebben die precies gelijke kansen heeft om op een willekeurige vlak terecht te komen.

Beantwoord de volgende vragen:  

> - **M1.1d) Als je een dobbelsteen eenmaal gooit, wat is dan de kans dat je een 1 gooit?   
En wat is de kans dat je een 4 of lager gooit?**<br><br>
>
> - **M1.1e) Stel dat je 10 keer met de dobbelsteen gooit. Wat is dan het verwachte aantal keren dat je 3 gooit?**<br><br>
>
> - **M1.1f) Als je dit experiment doet en je gooit wel 10 keer achter mekaar een 3, kun je daaruit dan concluderen dat je een niet eerlijke dobbelsteen hebt? Beredeneer je antwoord.**
<!-- Voor 2023: Beredeneer je antwoord-->

We gaan dit experiment nu simuleren. Om stochastische (ook wel toevallige of random) getallen te genereren maken we gebruik van de random nummer generator in het **`numpy`** pakket. Er zijn verschillende manieren om een dataset te maken die het experiment simuleert. In elk geval heb je de volgende pakketten nodig: 

	import numpy as np
	import random
	from random import seed

<!-- For 2024: remove the line from random import seed, also in .py file -->

Zet nu de **`seed`** van de random nummer generator op 1. Dit kan je zien als het startpunt waarvandaan het algoritme begint. Zo is de simulatie herhaalbaar onder steeds dezelfde condities. Dat wil zeggen dat wanneer het programma opnieuw runt, elke keer dezelfde random getallen worden gegenereerd



	random.seed(1)   # dit zet de seed in de random generator op 1.

Er zijn verschillende functies die je kan gebruiken. Kijk eens naar de **`uniform()`** en de **`randint()`** functies van [random](https://docs.python.org/3/library/random.html) en bedenk een manier om je simulatie te schrijven. 



> - Genereer nu een dataset waarin je simuleert dat je 30 keer met een dobbelsteen gooit.  <br>
**TIP** Als je het nodig hebt: gebruik **`(int)`** om naar een natuurlijk getal af te ronden. Controleer dat je alle getallen in de set {1,2,3,4,5,6} kunt maken. <br><br>  
> - **M1.1g) Plot de waarden in je dataset in een histogram. Kijk naar de code in de Intro opgave om te zien hoe je een histogram maakt. Let goed op de binning en range van je histogram. Als deze niet in orde zijn krijg je de verkeerde indruk van de dataset. Controleer je histogram desnoods door je dataset uit te printen en met de hand te tellen of je de juiste hoeveelheid in de juiste bin hebt. Kijk goed naar de richtlijnen en maak je histogram helemaal netjes.** <br><br>
>
> - **M1.1h)  Komt de distributie overeen met je verwachting? Motiveer dit.**<br><br>
>
> - **M1.1i)  Waarschijnlijk komt niet elke mogelijke uitkomst evenveel keer voor in je dataset. Hoe verwacht je dat de uitkomsten verdeeld zijn? Als je het experiment opnieuw zou doen, wat is dan de kans dat je maar 1 keer een 6 zult gooien. Gebruik hiervoor de <a href="/module-1/verdelingsfuncties#Poisson">Poisson kans</a> (deze kans moet je berekenen en kun je niet aflezen uit je histogram).**

Verzamel je antwoorden op het template voor module 1.

**Je moet straks de code ook inleveren**. We gebruiken deze bij het nakijken om, als er een fout is gemaakt in de opdracht te kunnen bekijken waar die vandaan komt. Het is natuurlijk ook de bedoeling dat de resultaten die je inlevert overeenkomen met de resultaten uit je programmaatje. Daar kijken we ook naar.


Als je alle andere opdrachten voor module 1 ook hebt gemaakt kun je de opdrachten en code inleveren via de ANS website. Bij de laatste opgave voor module 1 vind je hier meer informatie over. 
## B1a.B Kansdichtheidsdistributies **

We gaan in deze opgave kijken naar kansdichtheid distributies. Lees [hier](XX link maken) meer over kansdichtheid distributies. Er zijn een paar belangrijke, en bekende, distributies. We gaan in deze opgave aan de slag met de [poisson](XX link maken) en [uniforme](XX link maken) distributies.


###Poisson distributie

> Reken (met de hand) de volgende poisson kansen uit: $$P(k=1, \lambda=3)$$, $$P(k=2, \lambda =3)$$ en $$P(k=3, \lambda=3)$$. Kijk goed wat $$\lambda$$ en $$k$$ eigenlijk betekenen. Wat is de verwachtingswaarde en wat is de geobserveerde waarde?

We gaan nu poisson distributies met python grafisch weergeven. Download het bestand [B1a.B_Distributies.py](B1a.B_Distributies.py). De poisson distributie is één van de belangrijke distributies. We zullen hem vaak tegen gaan komen.

> 1. Maak een functie die de poisson kans uitrekent. De bedoeling is dat je de functie $$k$$ en $$\lambda$$ meegeeft en deze de poisson kans teruggeeft. In het bestand vindt je al een lege functie die je kunt invullen.<br> 
> **TIP** De macht, de expontieel en de faculteit die in de formule voorkomen kun je makkelijk uitrekenen met het math pakket in python. 
> 
> 		import math as math
> 		
> 		math.pow(lambda,k) ##lambdadit geeft lambda^k
> 		math.exp(-lambda)  ## geeft e^lambda
> 		math.factorial(k) ## geeft k!
> 
> 2. Reken nu de kansen $$P(k=1,\lambda=3)$$, $$P(k=2,\lambda =3)$$ en $$P(k=3,\lambda=3)$$, uit met je python functie. Komt het overeen? Check het resultaat.
>
> 3. Maak vervolgens een Poisson-kansdichtheidsdistributie voor $$\lambda = 5$$. Doe dit door eerst een lijst aan te maken met $$x$$ waardes tussen 1 en 40 (met stapjes van 1) en vervolgens voor elk punt de kans uit te rekenen met de functie en deze op te slaan in een lijst. Maak vervolgens een grafiek met de resultaten. Zorg dat je grafiek er netjes uitziet. Ziet de grafiek eruit zoals je had verwacht? 
> 
> 4. Herhaal dit nu en plot (over elkaar in 1 grafiek) de poisson distributies voor $$\lambda = 2, 5, 10$$ en $$20$$. 
>
> 5. Lees af in je grafiek hoe groot de kans is om een waarde van 4 te vinden voor de vier verschillende verwachtingswaarden. NB je kan het natuurlijk ook uitrekenen met je functie.



###Uniforme distributie
We gaan nu kijken naar de uniforme distributie en simuleren een experiment dobbelstenen gooien. We gaan er vanuit dat we een zuivere dobbelsteen hebben die precies gelijke kansen heeft om op een willekeurige vlak terecht te komen.

> 1. Als je een dobbelsteen 1x gooit, wat is dan de kans dat je een 3 gooit?
> En wat is de kans dat je een 2 of lager gooit?
>
> 2. Stel dat je 30 keer met de dobbelsteen gooit. Wat is dan het verwachte aantal keren dat je 3 gooit? 
> 3. Als je dit experiment doet en je gooit wel 10 keer een 3, kun je dan concluderen dat je een niet eerlijke dobbelsteen hebt?

We gaan dit experiment nu simuleren. Om stochastische (ook wel toevallige of random) getallen te genereren maken we gebruik van het numpy pakket. 

	import numpy as np
	from random import random
	from random import seed
	np.random.seed(1)                 # dit zet de seed in de randomgenerator op 1.
	getal = np.random.uniform()       # genereer een random getal tussen 0 en 1
	getallen = np.random.uniform(0,6,30) # genereer 30 getallen tussen 0 en 6

> 1. Genereer nu een dataset waarin je simuleert dat je 30 keer met een dobbelsteen gooit. <br>
> **TIP** gebruik **(int)** om naar een natuurlijk getal af te ronden. Controleer dat je alle getallen in de set {1,2,3,4,5,6} kunt maken. 
>  
> 2. Plot de waarden in je dataset in een histogram. Kijk naar de code in opgave B1a.A om te zien hoe je een histogram maakt. <br>
> Let goed op de binning en range van je histogram. Als deze niet in orde zijn krijg je de verkeerde indruk van de dataset. Controleer je histogram desnoods door je dataset uit te printen en met de hand te tellen of je de juiste hoeveelheid entries hebt in de juiste bin.
> 
> 3. Komt de distributie overeen met je verwachting?
>
> 3.  Waarschijnlijk komt niet elke mogelijke uitkomst evenveel keer voor in je dataset. Hoe verwacht je dat de uitkomsten verdeeld zijn? Als je het experiment opnieuw zou doen, wat is dan de kans dat je maar 1 keer een 6 zult gooien (deze kans moet je berekenen en kun je niet aflezen uit je histogram). 
>
> 4. Verzamel al je antwoorden en vul deze in op je inlever template.

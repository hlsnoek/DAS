## B1a.B Kansdichtheidsdistributies **

We gaan in deze opgave kijken naar kansdichtheid distributies. Lees [hier](XX link maken) meer over kansdichtheid distributies. Er zijn een paar belangrijke, en bekende, distributies. We gaan in deze opgave aan de slag met de [poisson](XX link maken) en [uniforme](XX link maken) distributies.


###Poisson distributie

> Reken (met de hand) de volgende poisson kansen uit: $$P(\lambda=3, k=1)$$, $$P(\lambda =3, k=2)$$ en $$P(\lambda=3, k=3)$$. Kijk goed wat $$\lambda$$ en $$k$$ eigenlijk betekenen. Wat is de verwachtingswaarde en wat is de geobserveerde waarde?

We gaan nu poisson distributies met python grafisch weergeven. Download het bestand [B1a.B_Distributies.py](B1a.B_Distributies.py). De poisson distributie is één van de belangrijke distributies. We zullen hem vaak tegen komen.

> 1. Maak een functie die de poisson kans uitrekent. De bedoeling is dat je de functie $$\lamda$$ en $$k$$ meegeeft en deze de poisson kans teruggeeft. In het bestand vindt je al een lege functie die je kunt invullen.<br> 
> **TIP** De macht, de expontieel en de faculteit die in de formule voorkomen kun je makkelijk uitrekenen met het math pakket in python. 
> 
> 		import math as math
> 		
> 		math.pow(lamda,k) ##dit geeft lamda^k
> 		math.exp(-lamda)  ## geeft e^lamda
> 		math.factorial(k) ## geeft k!
 

> 2. Reken nu de kansen $$P(\lamda=3, k=1)$$, $$P(\lamda =3, k=2)$$ en $$P(\lamda=3, k=3)$$, uit met je python functie. Komt het overeen? Check het resultaat.

> 3. Maak vervolgens een Poisson-kansdichtheidsdistributie voor $$\lamda = 5$$. Doe dit door eerst een lijst aan te maken met $$x$$ waardes tussen 1 en 50 (met stapjes van 1) en vervolgens voor elk punt de kans uit te rekenen met de functie. Maak vervolgens een grafiek met de resultaten. Zorg dat je grafiek er netjes uitziet. Ziet de grafiek eruit zoals je had verwacht? 

 
> 4. Herhaal dit nu en plot (over elkaar in 1 grafiek) de poisson distributies voor $$\lamda = 2, 5, 10$ en $$20$$.

> 5. Lees af in je grafiek hoe groot de kans is om een waarde van 4 te vinden voor de vier verschillende verwachtingswaarden. NB je kan het natuurlijk ook uitrekenen met je functie.

###Uniforme distributie
We gaan nu kijken naar de uniforme distributie en simuleren een experiment dobbelstenen gooien. We gaan er vanuit dat we een zuivere dobbelsteen hebben die precies gelijke kansen heeft om op een willekeurige vlak terecht te komen.

> 1. Wat is de kans dat je een 3 gooit met de dobbelsteen?

> 2. Stel dat je 30 keer met de dobbelsteen gooit. Wat is dan het verwachte aantal keren dat je 3 gooit?

We gaan dit experiment nu simuleren. Om stochastische (toevallige of random) getallen te genereren maken we gebruik van het numpy pakket. 

	import numpy as np
	from random import random
	from random import seed
	np.random.seed(1)                 # dit zet de seed in de randomgenerator op 1.
	getal = np.random.uniform()       # genereer een random getal tussen 0 en 1
	getal = np.random.uniform(0,6,30) # genereer 30 getallen tussen 0 en 6

> 1. Genereer nu een dataset waarin je simuleert dat je 30 keer met een dobbelsteen gooit. <br>
> **TIP** gebruik **(int)** om naar een natuurlijk getal af te ronden.
>  
> 2. Plot de waarden in je dataset in een histogram. Zorg dat je histogram de juiste binning en range heeft. Komt dit overeen met je verwachting?

> 3.  Waarschijnlijk komt niet elke mogelijk uitkomst evenveel keren voor in je dataset. Hoe verwacht je dat de uitkomsten verdeeld zijn? Wat is de kans dat je maar 1 keer een 6 hebt gegooid in jouw experiment (deze kans moet je berekenen en kun je niet aflezen uit je histogram). 

> 4. Verzamel al je antwoorden en vul deze in op je inlever template.

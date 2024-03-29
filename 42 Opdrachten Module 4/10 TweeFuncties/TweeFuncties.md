## M4.1 Twee Functies *
<!--REF\label{/opdrachten-module-4/}-->

We krijgen een dataset en we weten niet precies welke functie moet fitten aan de data. Er zijn twee theorieën. De eerste zegt dat er een lineair verband zou moeten bestaan. De tweede dat de meetwaardes Normaal verdeeld horen te zijn. We gaan de twee functies fitten aan de data en proberen te achterhalen welke van de twee functies het beste fit. 

Download eerst een nieuwe versie van de [DAS_DatasetGenerator.py](DAS_DatasetGenerator.py). Vergeet niet je studentnummer weer in te vullen.

Met het volgende statement kun je nu de onbekende dataset opvragen: 

	x, y, yerr = ds.OnbekendeFunctieGenerator()
	
Je krijgt 3 lists terug: x en y zijn de respectievelijke waardes voor x en y, yerr is de onzekerheid op de punten van y.

De twee functies die je wilt fitten worden gegeven door: 

$${\displaystyle f(x;a,b) = a\cdot x + b}$$

en 

$${\displaystyle g(x;N,\mu,\sigma) = N\cdot \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}}$$


> * Gebruik dezelfde fit methode als in opdracht M3.2 en fit beide functies aan de dataset. 
> * Maak een plotje waarin je de data laat zien en de twee gefitte functies $$f$$ en $$g$$. 
> * Kun je iets zeggen over hoe goed $$f$$ fit. Wat is hier aan de hand?
> * Kun je iets zeggen over hoe goed $$g$$ fit. Wat is hier aan de hand?
> * Vergelijk de twee gefitte functies door naar de $$\chi^2$$ per vrijheidsgraad te kijken en door de AIC waarde te berekenen. Wat kun je hieruit concluderen?
> * Voer je resultaten in op het inlevertemplate.
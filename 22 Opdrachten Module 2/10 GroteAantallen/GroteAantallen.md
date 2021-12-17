## Opdracht M2.1 Grote Aantallen II \*\*
<!--REF\label{/opdrachten-module-2/groteaantallen}-->

We gaan in deze opdracht verder kijken naar de ton met kogels uit opgave M1.4. 
In die opgave begonnen we met een ton met 80 kogels en berekenden we  het gemiddelde, $$g_n = \bar{m_n}$$ over de eerste $$n$$ kogels van de set. Zo kregen we de distributie van $$g_n$$ versus $$n$$.
***Voordat je met deze opdracht begint, controleer eerst even in ANS of je dit goed hebt gedaan en corrigeer eventueel je fouten.*** 

We gaan nu naar meerdere tonnen kijken, steeds met 80 kogels en uit dezelfde fabriek. 
Voor elke ton berekenen we de waardes van $$g_n$$ opnieuw. Dit doen we om het effect van de grootte van een steekproef bekijken. Eerst nemen we een steekproef van 10 kogels uit elke ton en gaan we daar het gemiddelde van bepalen. Daarna vergroten we de steekproef en kijken we hoe het gemiddelde verandert. Hierbij zijn we vooral benieuwd hoe groot de steekproef moet zijn om dicht bij het populatiegemiddelde te komen. 

We gaan er in deze opgave stap voor stap doorheen.

 
> - Maak eerst 100 verschillende datasets. Elke dataset is een ton met 80 kogels. Dit kan je doen door steeds een andere *seed* mee te geven aan de dataset generator: 
>	
>		datasets = [ds.DataSetGroteAantallen(i) for i in range(0,100)]
>
> De seed zorgt ervoor dat de datasets verschillend zijn, het is als het ware het startpunt van de random nummer generator. Als je steeds dezelfde seed meegeeft krijg je steeds dezelfde random dataset. (Probeer maar eens.) 

We hebben hier gebruik gemaakt van een *list comprehension*. Dat is een verkorte manier van het toepassen van een *for* statement waarbij het resultaat direct de gewenste lijst oplevert zonder dat de commando's *extend* of *append* nodig zijn. Als je hier meer over wilt weten dan vind je op het internet veel voorbeelden, bijvoorbeeld [hier](https://www.w3schools.com/python/python_lists_comprehension.asp). 

Je hebt nu een **`list`** die **`datasets`** heet met 100 items. Elke item in **`datasets`** is op zichzelf een lijst met 80 meetwaardes.
		
> - **M2.1a) Maak nu eerst een histogram van *alle eerste* elementen, $$m_1$$, van de 100 datasets. Zorg dat je histogram er netjes uitziet.** <br>
> Tip: Kijk eens of je hier een *list comprehension* voor kunt gebruiken. Welke index heeft het eerste element van een lijst in python?
><br><br>
> - **M2.1b) Wat is het gemiddelde, $$g_1$$, en de standaardafwijking $$s_1$$ van dit histogram? Denk bij het noteren aan de eenheden en de juiste notatie!** Kijk naar je histogram uit M2.1a en controleer of je resultaat overeen komt met je verwachting.
 
 
We nemen nu uit elke ton een steekproef van 10 kogels. We berekenen eerst het gemiddelde $$g_{10}$$ per steekproef, daarna bepalen we het gemiddelde van het gemiddelde. 


> - **M2.1c) Bereken voor elk van de 100 datasets het gemiddelde over de eerste 10 metingen en laat de distributie van deze gemiddeldes $$g_{10}$$ zien in een histogram.**<br> 
> Tip: Denk hierbij aan de functie die je al voor M1.4 hebt geschreven.

Je ziet nu duidelijk dat niet elke steekproef hetzelfde gemiddelde oplevert. Er is een bepaalde spreiding van de gemiddeldes $$g_{10}$$ die we hebben berekend. De distributie van gemiddeldes heeft dus zelf ook weer een gemiddelde en een spreiding. 

> - **M2.1d) Bereken van deze distributie het gemiddelde $$\overline{g_{10}}$$, dit is het gemiddelde van de gemiddeldes $$g_{10}$$. Bereken ook de standaardafwijking van de gemiddeldes: $$s_{g_{10}}$$.**

De spreiding van de berekende gemiddeldes kun je in dit geval zien als een maat voor de meetonzekerheid. Immers, we zien dat de berekende grootheid ($$g_{10}$$) niet altijd hetzelfde resultaat geeft. Het berekende resultaat *varieert*. Als mate van de meetonzekerheid nemen we de standaardafwijking van de distributie. 

We gaan dit nu herhalen voor met verschillende groottes van de steekproef $$n$$. 

> Maak een functie die voor een steekproefgrootte $$n$$ de standaardafwijking van de gemiddeldes $$g_n$$ terug geeft. Bereken hiervoor in de functie voor elk van de 100 datasets het gemiddelde over de eerste $$n$$ metingen. 
>
> Roep nu de functie aan voor de volgende waardes van $$n$$: 1, 5, 10, 20, 30, 40, 50, 60, 70, 80. Controleer of de punten voor $$n=1$$ en $$n=10$$ dezelfde resultaten opleveren als dat je net had. <br><br>
>
> - **M2.1e) Maak nu een grafiek waarin je de berekende standaardafwijking $$s_{g_n}$$ uitzet tegen de grootte van de steekproef, $$n$$.** <br><br>
> 
>  
> - **M2.1f) Maak een nieuwe grafiek waarin je de berekende $$s_{g_n}$$ uitzet tegen $$1/\sqrt{n}$$.**<br><br>
> 
>  
> - **M2.1g) Kun je iets zeggen over de grafieken? Beschrijf wat je ziet en probeer daar een conclusie uit te trekken.**


Wat we hebben gedaan in deze opdracht is illustreren wat er gebeurd als we een steeds grotere steekproef nemen. 




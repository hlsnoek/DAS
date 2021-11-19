## Opdracht M2.1 Grote Aantallen II \*\*
<!--REF\label{/opdrachten-module-2/groteaantallen}-->

We gaan verder kijken naar de ton met kogels uit opgave M1.4. 
In dit opgave begonnen we met een ton met 80 kogels en berekenden we  het gemiddelde, $$g_n = \bar{m_n}$$ over de eerste $$n$$ kogels van de set. Zo kregen we de distributie van $$g_n$$ versus $$n$$, net als in opgave M1.4.  
Voordat je verder gaat, controleer eerst even in ANS of je dit goed hebt gedaan en corrigeer eventueel je fouten. 

We gaan nu naar meerdere tonnen kijken, steeds met 80 kogels en uit dezelfde fabriek. 
We gaan steeds de waardes van $$g_n$$ opnieuw berekenen, voor elke ton weer. Als we alle gemiddelde waardes $$g_n$$ van één ton hebben berekend, dan beginnen we weer opnieuw met een nieuwe ton met 80 kogels. Dit herhalen we 100 keer.  
We gaan er in deze opgave stap voor stap doorheen.

 
> - Maak eerst 100 verschillende datasets. Elke dataset is een ton met 80 kogels. Dit kan je doen door steeds een andere seed mee te geven aan de datasetgenerator: 
>	
>		datasets = [ds.DataSetGroteAantallen(i) for i in range(0,100)]

Je hebt nu een **`list`** die **`datasets`** heet met 100 items. Elke item is een dataset met elk 80 meetwaardes.
		
 
> - **M2.1a) Maak nu eerst een histogram van *alle eerste* elementen, $$m_1$$, van de 100 datasets. Zorg dat je histogram er netjes uitziet.** 
> 
> 
> - **M2.1b) Wat is het gemiddelde, $$g_1$$, en de standaardafwijking $$s_1$$ van dit histogram? Denk bij het noteren aan de eenheden en de juiste notatie!** 
 
We gaan nu experimenten vergelijken waarin we steeds het gemiddelde over de eerste 10 metingen $$(g_{10})$$ hebben berekend. 

> - **M2.1c) Bereken voor elk van de 100 datasets het gemiddelde over de eerste 10 metingen en laat de distributie van deze gemiddeldes $$g_{10}$$ zien in een histogram.** 
>
>
> - **M2.1d) Bereken van deze distributie het gemiddelde $$\bar{g_{10}}$$, dit is het gemiddelde van de gemiddeldes $$g_{10}$$. Bereken ook de standaardafwijking van de gemiddeldes $$s_{g_{10}}$$ (de standaardafwijking van de gemiddeldes $$g_{10}$$).**

We gaan dit nu herhalen voor met verschillende groottes van de steekproef $$n$$. Maak een functie die de standaardafwijking $$s_{g_n}$$ van de 100 berekende gemiddeldes $$g_n$$ die berekend zijn over de eerste $$n$$ punten terug geeft.

Roep nu de functie aan voor de volgende waardes van $$n$$: 1, 5, 10, 20, 30, 40, 50, 60, 70, 80. Controleer of de punten voor $$n=1$$ en $$n=10$$ dezelfde resultaten opleveren als dat je net had. 

> - **M2.1e) Maak nu een grafiek waarin je de berekende standaardafwijking $$s_{g_n}$$ uitzet tegen de grootte van de steekproeven, $$n$$.** 
> 
>  
> - **M2.1f) Maak een nieuwe grafiek waarin je de berekende $$s_{g_n}$$ uitzet tegen $$1/\sqrt{n}$$.**
> 
>  
> - **M2.1g) Kun je iets zeggen over de grafieken? Beschrijf wat je ziet en probeer daar een conclusie uit te trekken.**


Wat we hebben gedaan in deze opdracht is illustreren wat er gebeurd als we een steeds grotere steekproef nemen. 




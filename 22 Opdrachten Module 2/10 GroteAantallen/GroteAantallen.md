## Opdracht M2.1 Grote Aantallen II \*\*
We gaan verder kijken naar de ton met kogels uit opgave M1.4. 

We namen een set van 80 kogels. We berekenen uit deze set van 80 kogels het gemiddelde, $$g_n = \bar{m_n}$$ over de eerste $$n$$ kogels van deze set. Zo krijgen we een distributie van $$g_n$$ versus $$n$$, net als in opgave M1.4.
Maar nu gaan we dit steeds opnieuw herhalen. Als we alle waardes van $$g_n$$ hebben berekend, dan beginnen we weer opnieuw met een nieuwe set met 80 kogels. Dit herhalen we 100 keer. 
We gaan er in deze opgave stap voor stap doorheen.

 
> Maak eerst 100 verschillende datasets. Dit kan je doen door steeds een andere seed mee te geven aan de datasetgenerator: 
>	
>		datasets = [ds.DataSetGroteAantallen(i) for i in range(0,100)]

Je hebt nu een **`list`** die **`datasets`** heet met 100 items. Elke item is een dataset met elk 80 meetwaardes.
		
 
> **M2.1a) Maak nu eerst een histogram van *alle eerste* elementen van de 100 datasets. Zorg dat je histogram er netjes uitziet.** <br><br>
> 
> **M2.1b) Wat is het gemiddelde, $$g_1$$, en de standaarddeviatie $$s_1$$ van dit histogram?** 
 
We gaan nu experimenten vergelijken waarin we steeds het gemiddelde over de eerste 10 metingen ($$g_10$) hebben berekend. 

> **M2.1c) Bereken voor elk van de 100 datasets het gemiddelde over de eerste 10 metingen en laat de distributie van deze gemiddeldes $$g_{10}$$ zien in een histogram.** <br><br>
>
> **M2.1d) Bereken van deze distributie het gemiddelde $$\barg_{g_{10}}$$ (het gemiddelde van de gemiddeldes $$\bar{g_{10}}$$) en de standaarddeviatie $$\s_{\bar{g_{10}}}$$ (de standaarddeviatie van de gemiddeldes $$s_{10}$$).**

We gaan dit nu herhalen voor met verschillende groottes van $$n$$. Maak een functie die de standaard deviatie $$s_{g_n}$$ van de 100 berekende gemiddeldes $$g_n$$ die berekend zijn over de eerste $$n$$ punten terug geeft.

Roep nu de functie aan voor de volgende waardes van $$n$$: 1, 5, 10, 20, 30, 40, 50, 60. 

> * Maak een grafiek waarin je de berekende standaard deviaties $$s_{g_n}$$over de distributies van $$g_n$$ uitzet tegen de grootte van $$n$$. 
> * Plot ook de berekende $$s_{g_n}$$ versus $$1/\sqrt{n}$$.
> * Wat valt je op aan de trend in de grafiek?







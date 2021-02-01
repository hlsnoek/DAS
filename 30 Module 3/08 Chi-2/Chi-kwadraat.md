
## De $$\chi^2$$ distributie

1. Ordered TOC
{:toc}

De $$\chi^2$$ distributie is een maat voor het verschil tussen de voorspelde waardes en het kwadraat van het verschil. Als de functie $$f$$ de data goed beschrijft zal de $$\chi^2$$ klein zijn. Als de $$\chi^2$$ dus groot blijft na het optimaliseren van de parameters van $$f$$ dan is er duidelijk iets misgegaan. Het kan zijn dat de functie $$f$$ de datapunten niet goed *kan* beschrijven, maar het kan ook zijn dat als je minimalisatie uitvoert met een computer deze het minimum niet goed heeft weten te vinden. 
Als daarentegen de $$\chi^2$$ heel klein is gaat er ook iets mis. Waarschijnlijk heb je de onzekerheden op de datapunten heel erg overschat. 
Hoe groot je verwacht dat de waarde van $$\chi^2$$ is na het optimaliseren van de kleinste kwadraten methode kun je bepalen. We gaan hieronder daar verder op in.

We hebben gezien in het hoofdstuk over de kleinste kwadraten methode, dat de $$\chi^2$$ gedefinieerd is als het kwadratische gewogen verschil tussen de meetwaardes en de voorspelde waardes: <br>

$${\displaystyle  \chi^2 = \sum^N_{i=1} \left( \frac{y_i-f(x_i;\hat{a},\hat{b},..)}{\sigma_i} \right)^2.}$$ 

Let op dat we hier de geoptimaliseerde parameters $$\hat{a}$$ van de functie hebben ingevuld. Deze waarde voor $$\chi^2$$ is dus al geminimaliseerd voor de paramaters van $$f$$.

De $$\chi^2$$ verdeling is een kansdichtheidsverdeling, en voldoet dus ook aan de voorwaardes hiervan. De functie ziet er als volgt uit: <br>

$${\displaystyle P(\chi^2;df) = \frac{2^{-df/2}}{\Gamma (df/2)} \chi^{n-2} e^{-\chi^2/2}.}$$

De $$\Gamma$$ in de noemer is een speciale wiskundige functie. Deze zal pas in jullie tweede jaar volledig worden uitgelegd. Op dit moment kun je hem simpelweg interpreteren als een functie waar een normalisatie term uitkomt. Het is best een gekke functie, voorbeelden van uitkomsten: $$\Gamma(1/2) = \sqrt{\pi}$$, $$\Gamma(1) = 1$$ en $$\Gamma(3/2) = 1/2 \sqrt{\pi}$$.
Als je al meer wilt weten over de $$\Gamma$$-functie dan kun je daar bijvoorbeeld [hier](https://nl.wikipedia.org/wiki/Gammafunctie) meer over lezen. 

Zoals je ziet hangt de $$\chi^2$$ kans ook af van een parameter $$df$$, dit is het aantal meetpunten, $$n$$, gereduceerd met het aantal parameters van de functie $$f$$. We noemen $$df$$ het aantal *vrijheidsgraden*. 

> **Voorbeeld** Stel we hebben 10 meetwaardes en we gebruiken de kleinste kwadraten methode om 2 parameters van een functie $$f$$ te optimaliseren. We hebben dan $$df=10-2=8$$ vrijheidsgraden.

Hier<!--FIG in figuur \ref{fig:ChiSquareDistributie}--> zie je hoe de $$\chi^2$$ eruit ziet voor verschillende waardes van $$df$$. <br> 

![De $$\chi^2$$ verdeling.](ChiSquareDistributie.png){:width="80%"}<br>

De $$\chi^2$$ distributie heeft een gemiddelde $$\mu = df$$ en een variantie van $$var = 2df$$. We verwachten dus een $$\chi^2$$ van ongeveer **1 per vrijheidsgraad**  te vinden. Als de $$\chi^2$$ per vrijheidsgraad veel afwijkt van 1 dan is het waarschijnlijk dat er een probleem is met de fit. Het kan zijn dat de functie de relatie tussen de datapunten niet goed beschrijft, of dat er iets mis is met de onzekerheden op de datapunten.



## Akaike Informatie Criterium
Stel dat je een dataset hebt waarvan je niet zeker weet door welke functie deze wordt beschreven. Je probeert twee functies uit, $$f_1$$ en $$f_2$$. En je minimaliseert voor beide functies de $$\chi^2$$, deze zijn dan $$\chi^2_1$$ en $$\chi^2_2$$. Als algemene vuistvuistregelregel geldt dat de functie met de kleinste geminimaliseerde $$\chi^2/df$$ het beste de data beschrijft. Als in dat geval de betreffende $$\chi^2/df$$ dicht bij 1 ligt werkt deze vuistregel goed. 

> **Voorbeeld 1** Stel dat we een dataset hebben met 10 gemeten waardes. We proberen twee functies uit: <br>
> $$f_1(x;a,b) = a\cdot x +b$$ en $$f_2(x;a) = a\cdot x$$<br>
> Als geminimaliseerde $$\chi^2$$ voor de twee functies vinden we: $$\chi^2_1 = 4.0$$ en $$\chi^2_2 = 13.0$$. <br>
> De $$\chi^2$$ per vrijheidsgraad is voor de twee functies: <br>
> $$\chi^2_1/\text{vrijheidsgraad} = 4.0/(10-2) = 0.5$$ en<br> 
> $$\chi^2_2/\text{vrijheidsgraad} = 13.0/(10-1) = 1.44$$.<br>
> Op basis van de vuistregel zou je functie $$f_1$$ kiezen. 
>
> **Voorbeeld 2** Stel dat we een dataset hebben met 10 gemeten waardes. We proberen twee functies uit: <br>
> $$f_1(x;a,b) = a\cdot x +b$$ en $$f_2(x;a) = a\cdot x$$<br>
> Als geminimaliseerde $$\chi^2$$ voor de twee functies vinden we: $$\chi^2_1 = 6.0$$ en $$\chi^2_2 = 9.0$$. <br>
> De $$\chi^2$$ per vrijheidsgraad is voor de twee functies: <br>
> $$\chi^2_1/\text{vrijheidsgraad} = 6.0/(10-2) = 0.75$$ en<br> 
> $$\chi^2_2/\text{vrijheidsgraad} = 9.0/(10-1) = 1.0$$.<br>
> Op basis van de vuistregel zou je functie $$f_1$$ kiezen. 

Als deze echter veel kleiner is dan 1 dan kun je betwijfelen of de bijbehorende functie wel echt de beste is. 
Beter is om dan het Akaike Informatie Criterium kun je gebruiken om uit te vinden welke functie het beste aan een dataset fit. Stel dat je een dataset hebt waarbij je $$n$$ meetwaardes hebt die je beschreven hebt met een functie met $$p$$ vrije parameters met een geminimaliseerde $$\chi^2$$. Dan heeft het Akaike Informatie Criterium de volgende waarde: 

$${\displaystyle AIC  = \chi^2 + 2p + \frac{2p(p+1)}{n-p-1}.}$$

Als we deze $$AIC$$ berekenen voor beide functies dan is de functie met de laagste $$AIC$$ de meest optimale.


> **Voorbeeld 1** Stel dat we een dataset hebben met 10 gemeten waardes. We proberen twee functies uit: <br>
> $$f_1(x;a,b) = a\cdot x +b$$ en $$f_2(x;a) = a\cdot x$$<br>
> Als geminimaliseerde $$\chi^2$$ voor de twee functies vinden we: $$\chi^2_1 = 4.0$$ en $$\chi^2_2 = 13.0$$. <br>
> De AIC waarde voor de twee functies zijn nu: <br>
> $$AIC_1 = 4.0 + 4 + 12/7 = 9.7 $$<br>
> $$AIC_2 = 13.0 + 2 + 4/8 = 15.5 $$<br>
> Op basis van het Akaike Informatie criterium zou je functie $$f_1$$ kiezen. 
>
> **Voorbeeld 2** Stel dat we een dataset hebben met 10 gemeten waardes. We proberen twee functies uit: <br>
> $$f_1(x;a,b) = a\cdot x +b$$ en $$f_2(x;a) = a\cdot x$$<br>
> Als geminimaliseerde $$\chi^2$$ voor de twee functies vinden we: $$\chi^2_1 = 6.0$$ en $$\chi^2_2 = 9.0$$. <br>
> De $$\chi^2$$ per vrijheidsgraad is voor de twee functies: <br>
> $$AIC_1 = 6.0 + 4 + 12/7 = 11.8 $$<br>
> $$AIC_2 = 9.0 + 2 + 4/8 = 11.5 $$<br>
> Op basis van de vuistregel zou je functie $$f_2$$ kiezen. 


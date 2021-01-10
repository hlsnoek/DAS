#Wet van Grote Aantallen

In opgave M1.4 hebben we gezien hoe de spreiding van een gemeten gemiddelde van 
metingen steeds kleiner wordt als we meer data gebruiken om het gemiddelde te bepalen. 
Dit is een belangrijke observatie. Het geeft aan dat hoe meer data we hebben, hoe nauwkeuriger we ons resultaat weten. Je voelt misschien al aan dat dit niet altijd op gaat. Wanneer dit wel en wanneer dit niet opgaat zullen we hier bespreken. 

We bespreken hier twee regels, of wetten, de $$\sqrt{n}$$-wet en de wet van grote aantallen. De eerste wet zegt dat we een gemiddelde, onder bepaalde voorwaarden, steeds beter kennen als we meer datapunten meenemen. De tweede wet zegt dat het gemiddelde van de steekproef langzaam zal convergeren naar het gemiddelde van de populatie.

## De $$\sqrt{n}$$-wet
We kijken naar twee onafhankelijke stochasten, $$X$$ en $$Y$$. De verwachtingswaarde van $$X+Y$$ is gelijk aan:

$$\displaystyle{ E(X+Y)= E(X)+E(Y) }$$ 

Als $$X$$ en $$Y$$ onafhankelijk zijn dan geldt ook:

$$\displaystyle{Var(X+Y)= Var(X)+Var(Y)}$$

Het ziet er misschien ingewikkeld uit, maar het enige wat we doen is een nieuwe variabele definiëren die de som is van twee variabelen. De variantie op de som vinden we via de gewone fouten propagatie [regels](/module-2/foutenpropagatie). 

Stel nu dat we dit uitbreiden. En we nemen de som van $$N$$ onafhankelijk stochasten, $$X_1,X_2,...,X_N$$  die elk dezelfde onderliggende verdeling kennen. Dat wil zeggen dat ze allemaal dezelfde verwachtingswaarde en dezelfde variantie hebben. 

NB. De verwachtingswaarde is niet gelijk aan de gemeten waarde. Kijk voor dit verschil nog eens naar [basisbegrippen](/module-1/basisbegrippen) in module 1. Als je terugdenkt aan de opgave van de kogels is de verwachtingswaarde van de massa van een kogel gelijk aan de gemiddelde massa van alle kogels. Als we een willekeurige kogel uit de ton pakken, dan is de gemiddelde massa van de kogels in de ton, de *verwachting* die we hebben van de massa van de kogel die we pakken.   De verwachtingswaarde is dus hier het gemiddelde.

De variantie is de spreiding op de massa distributie. Als je een willekeurige kogel uit de ton pakt is de kans heel klein dat de massa precies gelijk is aan de verwachtingswaarde van de massa. De variantie geeft aan in welk gebied van waardes we verwachten de massa van de kogel te vinden.


De formule voor de som kunnen we nu schrijven als:

$$\displaystyle{ Som_N = X_1 + X_2 + ... + X_N.}$$ 

En het gemiddelde kunnen we schrijven als:

$$\displaystyle { E(<{X_1 ... X_N}>) = \frac{Som_n}{N}.}$$

Als de verwachtingswaarde van een enkele stochast $$E(X_i)$$ gelijk is aan het gemiddelde $$\mu$$ en de variantie gelijk is aan $$Var(X_i) = \sigma^2$$, dan geldt nu voor de verwachtingswaarde van de som:  

$$\displaystyle{ E(S_N)= \mu N} $$

en voor het gemiddelde:

$$\displaystyle{E(<{X_1 ... X_N}>) = \mu.}$$  

En dan geldt voor de variantie  

$$\displaystyle{ Var(S_N) = N \sigma^2 } $$ 

en 

$$\displaystyle{ Var(<{X_1 ... X_N}>) = \frac{\sigma^2}{N}.}$$

Dit betekent dat **de standaarddeviatie van de som van de stochasten** gelijk is aan $$\sigma \cdot \sqrt{N}$$.  
De standaarddeviatie van het gemiddelde is dan gelijk aan:  

$$\displaystyle{\text{standaard deviatie op het gemiddelde is: }\frac{\sigma \cdot \sqrt{N}}{N} = \frac{\sigma}{\sqrt{N}}}.$$

Dit betekent dus dat als we het gemiddelde van de massa van N aantal kogels nemen waarbij de kogels een Normale distributie hebben met een gemiddelde $$\mu$$ en een standaarddeviatie van $$\sigma$$, de onzekerheid op de bepaalde gemiddelde massa gelijk is aan $$\sigma/\sqrt{N}$$.  
Hoe meer kogels we wegen en meenemen in ons gemiddelde, hoe nauwkeuriger we dit gemiddelde kennen. 



## De wet van Grote Aantallen
Intuïtief voelen we aan dat hoe meer metingen we doen, hoe meer informatie we hebben, en hoe nauwkeuriger ons resultaat is. 

De **wet van grote aantallen** zegt dat het berekende steekproef gemiddelde, $$<{X}>$$, van een distributie met een eindige variantie, convergeert naar het populatie gemiddelde $$\mu$$ voor steeds grote steekproeven:<br>
<center>$${\displaystyle lim_{N \to \infty} P( | \lt X \gt - \mu| \gt \epsilon) = 0 } $$</center>

Ofwel de kans dat het steekproef gemiddelde meer afwijkt van het populatie gemiddelde dan een heel klein getal convergeert naar 0 voor oneindig grote steekproeven. 
Voor eindige populaties is dit natuurlijk zeker waar. Maar denk hier ook aan  oneindig grote, of nagenoeg oneindig grote populaties, zoals bijvoorbeeld als je de gemiddelde massa van het electron wilt bepalen. 

**Tip:** In deze [video](https://www.youtube.com/watch?v=MntX3zWNWec) wordt de wet van grote aantallen nogmaals duidelijk uitgelegd. 

Als je de wet goed leest zie je dat er een voorwaarde aan vast zit. Namelijk dat de variantie van de stochast eindig moet zijn, en dat dus de verwachtingswaarde van de stochast bepaald is. Er bestaan distributies, zoals de [Cauchy](https://nl.wikipedia.org/wiki/Cauchy-verdeling) of de [Landau](https://en.wikipedia.org/wiki/Landau_distribution) distributie waarvoor dit dus niet geldt. Deze distributies hebben oneindig lange staarten. Hieronder zie je hoe de Cauchy distributie eruit ziet.

![](CauchyDistributie.png){:width="80%"} 

Wiskundig kan de wet van de grote aantallen dus weleens voor problemen zorgen. In Natuurkundige experimenten zijn verdelingen uiteindelijk vaak beknot door bijvoorbeeld de eindigheid van energie. Voor Natuurkundige experimenten gaat de wet van grote aantallen dus vaak wel op.

Overigens noemen we deze wet van grote aantallen de *zwakke* wet van grote aantallen, er bestaat ook een *sterke* wet. We gaan hier niet in op de kleine verschillen tussen deze twee wetten, online kun je er eventueel genoeg over vinden.
 





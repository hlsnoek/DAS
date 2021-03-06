# Extra kans rekenregels

In [module 1](/module-1/kanstheorie) hebben we de complement, de en-regel en de of-regel geleerd voor het rekenen met kansen. Aan deze regels waren enkele voorwaarden verbonden. 

De of-regel geldt alleen als de metingen A en B wederzijds uitsluitend zijn. Dat betekent dat een meting A niet kan voorkomen als B gemeten is. 

> Een voorbeeld van kansen die niet wederzijds uitsluitend zijn is, als we weer kijken naar een set kaarten waar A bijvoorbeeld de kleur rood is en B het getal 4. Er bestaan rode kaarten met getal vier en in dit geval mogen we de kansen dus niet optellen. <br>
> $$P(\text{rood of 4}) \neq P(\text{rood}) + P(4)$$

We breiden de regels hier verder uit en gaan kijken naar het combineren van kansen die niet wederzijds uitsluitend zijn. We kijken ook naar het begrip conditionele kans en introduceren Bayes theorema die gebruikt kan worden om informatie van kansen om te rekenen. 


## De of regel wanneer A en B niet wederzijds uitsluitend zijn:
In het geval A en B niet wederzijds uitsluitend zijn dan:<br>
$$P(\text{A en B}) \equiv P(A \cap B) >0.$$
De kans dat A of B gemeten wordt is dan:

$$P(\text{A of B}) = P(A) + P(B) - P(\text{A en B}).$$

> Voorbeeld: De kans dat een kaart rood is en een vier heeft is 2/52. De kans dat een kaart rood is of een vier is nu gelijk aan P(1/2) + P(4/52) - P(2/52) = 28/52.

De term $$(\text{A en B})$$ noemen we ook wel de doorsnede, of intersectie, van A en B. Het is het overlappende deel van elementen in de verzameling. Hier<!--FIG , in Fig. \ref{fig:180px-Venn0001.svg},--> zie je het uitgebeeld in een Venn diagram. De doorsnede wordt ook wel genoteerd met $$A \cap B$$. <br>
![Doorsnede van A en B (bron wikipedia)](180px-Venn0001.svg.png){:width="60%"}


De vereniging van $$A$$ en $$B$$ wordt genoteerd met $$A \cup B$$ en is de verzameling van alle elementen van A en B. Hier<!--FIG , in Fig. \ref{fig:180px-Venn0111.svg}--> het Venn diagram voor de verzameling.<br>
![Doorsnede van A en B (bron wikipedia)](180px-Venn0111.svg.png){:width="60%"}


En zo kun je ook het complement van A laten zien<!--FIG , zie in Fig. \ref{fig:180px-Venn1010.svg}-->. <br>
![Complement van A (bron wikipedia)](180px-Venn1010.svg.png){:width="60%"}


## Conditionele kans
Een conditionele kans wordt geschreven als $$P(A \mid B)$$ en kun je lezen als "Wat is de kans op meting A gegeven dat B is gemeten.". Let op dat $$P(A \mid B)\neq P(B \mid A)$$! Een sprekend voorbeeld hiervan is de volgende. De kans dat een persoon zwanger is gegeven dat de persoon een vrouw is, $$P(\text{zwanger} \mid \text{vrouw})$$, is niet gelijk aan de kans dat iemand een vrouw is gegeven dat de persoon zwanger is, $$P(\text{vrouw} \mid \text{zwanger})$$. De laatste kans is duidelijk gelijk aan 1, als je zwanger bent ben je zeker een vrouw. De eerste kans is een stuk kleiner!

De conditionele kans kunnen we berekenen met: <br>

$$\displaystyle{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}.$$

De noemer in deze vergelijking, $$P(B)$$, noemen we ook wel een normalisatie  term. De kans $$P(A \cap B)$$ moet genormaliseerd worden naar de kans $$P(B)$$, immers het is al een gegeven dat $$B$$ waar is. 

Visueel is dit wellicht het meest eenvoudige om te zien. Als het gegeven is dat de uitkomst in het deelgebied B ligt, dan is de kans dat het ook de waarde A bezit gelijk aan het oppervlak van de overlap tussen A en B gedeeld door het oppervlak van B. Immers dat het B is weten we al, dus we moeten alle kansen normaliseren naar B. 


## Bayes theorema
Met behulp van de conditionele kans formule kunnen we nu Bayes theorema afleiden. <br>
Het combineren van de formules van $$P(A \mid B)$$ en $$P(B \mid A)$$:

$$P(A \cap B) \equiv P(B \cap A) =  P(B \mid A) \cdot P(A) = P(A \mid B) \cdot P(B)$$ 

geeft:

$$\displaystyle P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}$$

Dit theorema maakt het mogelijk om nieuwe informatie toe te voegen aan de kennis van de kans. In [module 1](/module-1/kanstheorie) hebben we het kort over Bayesiaanse kans definitie gehad. Dit theorema staat centraal in Bayesiaanse kans. Het is wel belangrijk om te weten dat deze wiskundige vergelijking ook opgaat in de Frequentist benadering van kans.  

Bekijk ook even het kennisclipje over Extra Kansrekenregels op Canvas!
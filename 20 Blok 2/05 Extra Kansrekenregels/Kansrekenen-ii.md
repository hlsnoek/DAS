#Extra kans rekenregels

In [blok 1](/blok-1/kanstheorie) hebben we de complement, de en-regel en de of-regel geleerd voor het rekenen met kansen. Aan deze regels waren enkele voorwaarden verbonden. 

De of-regel geldt alleen als de metingen A en B wederzijds exclusief zijn. Dat betekent dat een meting A niet kan voorkomen als B gemeten is. 


> Een voorbeeld van kansen die niet wederzijds exclusief zijn is, als we weer kijken naar een set kaarten waar A bijvoorbeeld de kleur rood is en B het getal 4. Er bestaan rode kaarten met getal vier en in dit geval mogen we de kansen dus niet optellen. <br>
> <center> $$P(\text{rood of 4}) \neq P(\text{rood}) + P(4)$$</center>

###De of regel wanneer A en B niet wederzijds exclusief zijn:
In het geval A en B niet wederzijds exclusief zijn dan:<br>
<center>$$P(\text{A and B}) \equiv P(A \cup B) = P(A) + P(B) >0.$$</center><br>
De kans dat A of B gemeten wordt is dan:
<center>$$P(\text{A of B}) = P(A) + P(B) - P(\text{A en B}).$$</center>

> Voorbeeld: De kans dat een kaart rood is en een vier heeft is 2/52. De kans dat een kaart rood is of een vier is nu gelijk aan P(1/2) + P(4/52) - P(2/52) = 28/52.

De term $$(\text{A en B})$$ noemen we ook wel de doorsnede, of intersectie, van A en B. Het is het overlappende deel van elementen in de verzameling. Hieronder zie je het uitgebeeld in een Venn diagram. De doorsnede wordt ook wel genoteerd met $$$A \cap B$. <br>
![](180px-Venn0001.svg.png "doorsnede van A en B (bron wikipedia)")
*"doorsnede van A en B (bron wikipedia)"*

De vereniging van $$A$$ en $$B$$ wordt genoteerd met $$A \cup B$$ en is de verzameling van alle elementen van A en B. Hieronder het Venn diagram voor de verzameling.<br>
![](180px-Venn0111.svg.png "vereniging van A en B (bron wikipedia)")
*"vereniging van A en B (bron wikipedia)"*

En zo kun je ook het complement van A laten zien: <br>
![](180px-Venn1010.svg.png "complement van A (bron wikipedia)")
*"complement van A (bron wikipedia)"*

### Conditionele kans
Een conditionele kans wordt geschreven als $$P(A|B)$$ en kun je lezen als "Wat is de kans op meting A gegeven dat B is gemeten.". De conditionele kans kunnen we berekenen met: <br>
<center> $$\displaystyle{\frac{P(A \cap B)}{P(B)}}.$$</center><br>
De noemer in deze vergelijking, $$P(B)$$, noemen we ook wel een normalisatie  term. De kans $$P(A \cap B)$$ moet genormaliseerd worden naar de kans $$P(B)$$, immers het is al een gegeven dat $$B$$ waar is. 

### Bayes theorema
Met behulp van de conditionele kans formule kunnen we nu Bayes theorema afleiden. <br>
<center>$$\displaystyle P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$</center><br>
Dit theorema maakt het mogelijk om nieuwe informatie toe te voegen aan de kennis van de kans. In [blok 1](/blok-1/kanstheorie) hebben we het kort over Bayesiaanse kans definitie gehad. Dit theorema staat centraal in Bayesiaanse kans. Het is wel belangrijk om te weten dat deze wiskundige vergelijking ook opgaat in de Frequentist benadering van kans.  
#Extra kans rekenregels

In [blok 1](/blok-1/kanstheorie) hebben we de complement, de en-regel en de of-regel geleerd voor het rekenen met kansen. Aan deze regels waren enkele voorwaardes verbonden. 

De of-regel geldt alleen als de metingen A B wederzijds exclusief zijn. Dat betekend dat een meting A niet kan voorkomen als B gemeten is. 


> Een voorbeeld van kansen die niet wederzijds exclusief zijn is als we weer kijken naar een set kaarten waar A bijvoorbeeld de kleur rood is en B het getal 4. Er bestaan rode kaarten met getal vier en in dit geval mogen we de kansen dus niet optellen. <br>
> <center> $$P(\textfm{rood of 4}) \neq P(\textfm{rood}) + P(4)$$</center>

###De of regel wanneer A en B niet wederzijds exclusief zijn:
In het geval A en B niet wederzijds exclusief zijn dan:<br>
<center>$$P(\textfm{A and B}) \equiv P(A \cup B) = P(A) + P(B) >0.$$</center><br>
De kans dat A of B gemeten wordt is dan:
<center>$$P(\textfm{A of B}) = P(A) + P(B) - P(\textmf{A en B}).$$</center>

> Voorbeeld: De kans dat een kaart rood is en een vier heeft is 2/52. De kans dat een kaart rood is of een vier is nu gelijk aan P(1/2) + P(4/52) - P(2/52) = 28/52.

De term $$(\textfm{A en B})$$ noemen we ook wel de doorsnede, of intersectie, van A en B. Het is het overlappende deel van elementen in de verzameling. Hieronder zie je het uitgebeeld in een Venn diagram. De doorsnede wordt ook wel genoteerd met $$$A \cap B$. 
![](1024px-Venn_A_intersect_B.svg.png "doorsnede van A en B (bron wikipedia)"){:width = "35%"}

De vereniging van $$A$$ en $$B$$ wordt genoteerd met $$A \cup B$$ en is de verzameling van alle elementen van A en B. Hieronder het Venn diagram voor de verzameling.
![](Venn_A_union_B.png "vereniging van A en B (bron wikipedia)"){:width = "35%"}


en de of-regel gelden voor *onafhankelijke* In dit hoofdstuk zullen we nog een 
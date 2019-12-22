## Kanstheorie

Een kans is een waarde tussen de $$0$$ en de $$1$$ die aangeeft hoe waarschijnlijk een gebeurtenis is.
Een kans van $$0$$ geeft aan dat iets *niet kan* gebeuren en een kans van $$1$$ geeft aan dat iets *altijd* gebeurt. Een kans van $$\frac{1}{2}$$ geeft aan dat iets naar verwachting de helft van de tijd zal gebeuren.

De kans op een *gebeurtenis* $$P(\text{gebeurtenis})$$ wordt gegeven door het aantal mogelijkheden waarbij de gebeurtenis kan optreden gedeeld door het totaal aantal mogelijkheden:

$$P(\text{gebeurtenis}) = \frac{\text{Aantal mogelijkheden waarbij de gebeurtenis optreedt}}{\text{Het totale aantal mogelijkheden}}$$ 

De kansen op alle mogelijke uitkomsten bij elkaar opgeteld zijn gelijk aan 1.

Als er $$n$$ mogelijke uitkomsten zijn, die allemaal even waarschijnlijk zijn dan is de kans op elke uitkomst gelijk aan 

$$P(\text{gebeurtenis}) = \frac{1}{n}$$

Stel we gooien met een zes zijdige dobbelsteen (afgekort tot D6). De kans om bijvoorbeeld 4 te gooien is gelijk aan:

$$P(\text{we gooien 4 met een D6}) = \frac{\text{Aantal mogelijkheden waarbij de gebeurtenis optreedt}}{\text{Het totale aantal mogelijkheden}} \frac{1}{6}$$


## Kansrekening - start

In dit onderdeel maken we een start met de kansrekening.

<>### De EN-regel, de OF-regel en de complementregel

### Rekenregels
De EN-regel en de OF-regel vertellen ons hoe we met gecombineerde kansen moeten omgaan. 

#### EN-regel
Als we de kans willen weten dat gebeurtenis A plaatsvindt en gebeurtenis B, dan moeten we de kans op gebeurtenis A vermenigvuldigen met de kans op gebeurtenis B, dit heet de EN-regel:

$$P(A\text{ en }B) = P(A)\cdot P(B)$$

Hierbij zijn A en B onafhankelijke gebeurtenissen.
Als we bijvoorbeeld willen weten wat de kans is op het gooien van 2 en 4 met twee dobbelstenen dan is deze gelijk aan:

$$P(\text{we gooien }2\text{ en }4) = P(2\text{ gooien}\cdot P(4\text{ gooien})) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$$

#### OF-regel

We kunnen ons ook afvragen wat de kans is dat we met één dobbelsteen 2 of 4 gooien. Hierbij krijgen we te maken met de OF-regel. We willen namelijk weten wat de kans is op gebeurtenis A of gebeurtenis B. Deze kans is gelijk aan de kans op gebeurtenis A plus de kans op gebeurtenis B:

$$P(A\text{ of }B) = P(A) + P(B)$$

Hierbij zijn A en B gebeurtenissen die elkaar uitsluiten.
In het geval van de dobbelsteen waarbij we willen weten wat de kans is om 2 of 4 te gooien wordt dit:

$$P(\text{we gooien }2\text{ of }4) = P(2\text{ gooien} + P(4\text{ gooien})) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}$$

#### Complementregel

Stel we willen de kans weten dat we met een dobbelsteen $$1$$, $$2$$, $$3$$, $$4$$ of $$5$$ gooien en geen $$6$$. 
Dan kunnen we natuurlijk de kans $$P(1\text{ of }2\text{ of }3\text{ of }4\text{ of }5)$$ bepalen. Omdat dit nog vrij weinig gebeurtenissen zijn is dit nog te doen. Maar in vele gevallen is dit niet zo handig om te doen omdat het heel veel tijd kan kosten.

Omdat alle kansen bij elkaar opgeteld gelijk zijn aan $$1$$ is de kans op een gebeurtenis A ook gelijk aan:

$$P(A)=1-P(\text{niet }A)$$

Dit wordt de complementregel genoemd. 

Bij bovenstaand voorbeeld is de kans $$P(1\text{ of }2\text{ of }3\text{ of }4\text{ of }5)$$ dus ook gelijk aan:

$$P(1\text{ of }2\text{ of }3\text{ of }4\text{ of }5) = 1-P(\text{niet }1,\text{niet }2,\text{niet }3,\text{niet }4,\text{niet }5) = 1-P(6\text{ gooien}) = 1-\frac{1}{6} = \frac{5}{6}$$


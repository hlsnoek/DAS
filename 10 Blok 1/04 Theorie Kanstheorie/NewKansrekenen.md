## Kanstheorie


Een kans is een getal tussen de $$0$$ en de $$1$$ die aangeeft hoe waarschijnlijk het is dat een bepaalde gebeurtenis zal plaatsvinden.

Een kans van $$1$$ zegt dat het **zeker** zal gebeuren en een kans van $$0$$ dat het **zeker niet** zal gebeuren. Een kans van $$\frac{1}{2}$$ geeft aan dat in $$50\%$$ van de gevallen de gebeurtenis zal plaatsvinden.

Als voorbeeld nemen kijken we naar een dobbelsteen. 
Wat is de kans dat je een $$4$$ gooit als je de dobbelsteen 1 keer gooit? 

Voor een normale dobbelsteen kunnen deze kans uitrekenen met behulp van de volgende formule: 

$$P(\text{uitkomst is }4) = \frac{\text{aantal uitkomsten met een 4}}{\text{Het totale aantal uitkomsten.}} = \frac{1}{6}$$ 

Dit is de kans voor een normale eerlijke dobbelsteen. Met eerlijk bedoelen we hier dat de dobbelsteen niet gemanipuleerd is en dat elk vlak van de dobbelsteen evenveel kans heeft om boven te eindigen. 

Stel nu dat we een speciale eerlijke dobbelsteen zouden hebben met de volgende vlakken: {1,2,2,3,4,4}. De kans om nu een $$4$$ te gooien is groter dan met een normale eerlijke dobbelsteen, namelijk: 

$$P(\text{uitkomst is }4) = \frac{\text{aantal uitkomsten met een 4}}{\text{Totale aantal uitkomsten}} = \frac{2}{6}$$. 

En stel nu dat we een normale dobbelsteen hebben die gemanipuleerd is? Dan zal de kans om een 4 te gooien anders zijn. Een goede manier om dan de kans te bepalen is met behulp van de $$Frequentist$$ formule: 

$$P(4) = lim_{n \to \infty} \frac{uitkomst is 4}{totaal aantal worpen}$$.

De frequentist kans is een goede manier om kansen te berekenen. Het kent echter twee grote beperkingen. De eerste is dat we eigenlijk nooit een oneindig aantal metingen kunnen doen. Dit is goed te benaderen door gewoon een heel groot aantal metingen te doen. De tweede beperking is dat niet alle experimenten herhaalbaar zijn. 


### Frequentist versus Bayesiaanse methode
Het zal je daarom niet verbazen dat er nog een andere methode bestaat die wel werkt voor experimenten die niet herhaalbaar zijn of een beperkte statistiek. Deze manier noemen we ook wel de Bayesiaanse (spreek uit: Beej-sie-jaanse) methode (engels: Bayesian). 

De frequentist methode wordt in het algemeen als objectieve methode gezien en de Bayesiaanse methode een subjectieve manier. Het geeft aan wat je denkt dat de waarschijnlijkheid is. Dat klinkt misschien niet erg wetenschappelijk maar in de praktijk is dit misschien wel de meest gebruikte methode. Vooral omdat je hem ook kan gebruiken als het experiment niet herhaalbaar is. 

Een voorbeeld. In een wielerronde staat een bergklassieker op het programma van vandaag. De wedstrijd is nog niet gestart. Er staan twee sterke renners,  Lauda en Onana, op de gedeelde eerste plaats van het klassement en de voorsprong met de derde wielrenner is meer dan 20 minuten. Het lijkt dus waarschijnlijk dat aan het einde van de dag Lauda of Onana op de eerste plaats in het klassement staat. Op bergetappes wint Onana 9 van de 10 keer met een flinke voorsprong van Lauda. Wie denk je dat er wint? 

We kunnen het experiment natuurlijk niet herhalen maar het lijkt zeer waarschijnlijk dat Onana aan het einde van de dag op nummer 1 zal eindigen. 

Hier maken we gebruik van de subjectieve methode van Bayes. Om het te quantificeren kunnen we misschien zelfs wel zeggen dat de kans 0.9 is.

Maar nu zitten we aan ontbijt en we zien dat Onana geen hap door zijn keel krijgt. Hij is duidelijk erg ziet. Lauda daarentegen ziet er fris en sterk uit. 

Hoe waarschijnlijk denk je nu dat het is dat Onana zal winnen?

Het lijkt nu toch een stuk minder waarschijnlijk dat Onana zal winnen. In elk geval heeft het een lagere waarschijnlijkheid dan de 0.9 waarmee wee eerste werkten.Misschien heb je zelfs wel informatie uit het verleden waaruit je weet hoeveel langzamer renners zijn als ze er zo ziek uitzien als Onanan. Wat voor impact dat heeft op hun performance. Dan zouden we ons kans van 0.9 kunnen 'updaten' met de nieuwe informatie. Dat is typisch een Bayesiaanse methode om kansen uit te rekenen.

Wat heel belangrijk is voor beide methodes, is om altijd heel precies te vermelden wat de voorwaardes zijn geweest waaronder de kans is uitgerekend. 

Beide methodes worden dus gebruikt, maar de Bayesiaanse methode, of zelfs een hybride methode vindt vooral zijn toepassing in heel complexe modellen en voorspellingen. In dit college zullen we vooral werken met de frequentist methode.


###

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


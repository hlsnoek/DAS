# Kanstheorie
<!--REF\label{/module-1/kanstheorie}-->
1. Ordered TOC
{:toc}

In dit hoofdstuk leren we over kanstheorie en kansdichtheidsfuncties. Kanstheorie
speelt een belangrijke rol in het begrijpen en bepalen van meetonzekerheden. 
Zoals in het hoofdstuk over [meetonzekerheden](/module-1/meetonzekerheid) is uitgelegd kunnen meetonzekerheden verschillende oorzaken hebben. Bij elk van die oorzaken hoort een bepaalde waarschijnlijkheidsverdeling en deze zijn verbonden aan kansprocessen. 

Vaak willen we metingen gebruiken om voorspellingen te doen of hypotheses te toetsen. Als we hiervoor een bepaalde
serie meetgegevens willen gebruiken, dan is het belangrijk om te weten wat de
meetonzekerheden zijn. Deze kunnen we vervolgens gebruiken om te kijken hoe goed ze passen bij een bepaald voorspeld patroon of hoe goed ze een theorie bevestigen of juist weerleggen. 

Om die stap later te kunnen maken, moeten we eerst meer leren over kanstheorie en hierna over kansdichtheidsfuncties. In dit hoofdstuk maken we daar een begin mee. 

          

## Definitie van Kans

Waarschijnlijk is iedereen wel bekend met het concept van kans. We gebruiken het vaak. 
Wat is de kans dat het regent? Wat is de kans om de loterij te winnen? 

Wiskundig is een kans gedefinieerd als een getal tussen de 0 en de 1 dat aangeeft hoe waarschijnlijk het is dat een bepaalde gebeurtenis zal plaatsvinden.
Een kans van 1 zegt dat het **zeker** zal gebeuren en een kans van 0 dat het **zeker niet** zal gebeuren. Een kans van 0.5 geeft aan dat in 50% van de gevallen de gebeurtenis zal plaatsvinden.



>  **Voorbeeld** We kijken naar een dobbelsteen. 
Wat is de kans dat je een 4 gooit als je de dobbelsteen 1 keer gooit? 
Voor een normale dobbelsteen kunnen we deze kans uitrekenen met behulp van de volgende formule: <br>
><br>
> $${\displaystyle P(\text{uitkomst is }4) = {\displaystyle \frac{\text{aantal uitkomsten met een 4}}{\text{totaal aantal uitkomsten}} = \frac{1}{6}.}}$$ 
>

Dit is de kans voor een normale eerlijke dobbelsteen. Met eerlijk bedoelen we hier dat de dobbelsteen niet gemanipuleerd is en dat elk vlak van de dobbelsteen evenveel kans heeft om boven te eindigen. 

Stel nu dat we een speciale, maar wel eerlijke, dobbelsteen zouden hebben met de volgende vlakken: {1,2,2,3,4,4}. De mogelijke uitkomsten bij een dobbelsteenworp zijn nu: {1,2,3,4}. Dit noemen we ook de **uitkomstenverzameling** waarbij alle elementen uniek zijn, en dus maar 1 keer voorkomt. 

De kans om nu een 4 te gooien is groter dan met een normale eerlijke dobbelsteen. Dit werken we uit in het volgende voorbeeld.

> **Voorbeeld** Als we de kans nu berekenen voor de speciale dobbelsteen met vlakken {1,2,2,3,4,4} dan is de kans om vier te gooien: 
> <br>
> $${ \displaystyle P(\text{uitkomst is }4) = \frac{\text{aantal uitkomsten met een 4}}{\text{totale aantal uitkomsten}} = \frac{2}{6}.}$$ 
>

En stel nu dat we een normale dobbelsteen hebben die gemanipuleerd is? Dan zal de kans om een 4 te gooien anders zijn. Een goede manier om dan de kans te bepalen is met behulp van de **Frequentist** formule. 
De algemene formule voor de **Frequentist definitie** van kans is: <br><br>

$${\displaystyle P(\text{uitkomst A}) = \lim_{n \to \infty} \frac{\text{aantal uitkomsten A}}{n}.}$$

Waarbij we het aantal malen dat we uitkomst A krijgen uit ons experiment delen door het totaal aantal metingen, $$n$$, dat we hebben verricht. 

In het geval van de dobbelsteen wordt deze formule dan: 

$$\displaystyle{P(4) = lim_{n \to \infty} \frac{\text{uitkomst is 4}}{\text{totaal aantal worpen}}.}$$

Hoe vaker we de dobbelsteen gooien des te nauwkeuriger kunnen we de kans dat we een 4 gooien, bepalen.


De Frequentist definitie voor kans is een goede manier om kansen te berekenen. Het kent echter twee grote beperkingen. De eerste is dat we eigenlijk nooit een oneindig aantal metingen kunnen doen. Dit is goed te benaderen door gewoon een heel groot aantal metingen te doen. De tweede beperking is dat niet alle experimenten herhaalbaar zijn. 


### Frequentist versus Bayesiaanse methode
Het zal je dan misschien niet verbazen dat er nog een andere methode bestaat die wel werkt voor experimenten die niet herhaalbaar zijn of een beperkte statistiek hebben. Deze manier noemen we ook wel de Bayesiaanse (spreek uit: Beej-sie-jaanse) methode (Engels: Bayesian). 

De frequentist methode wordt in het algemeen als objectieve methode gezien en de Bayesiaanse methode een subjectieve manier. Het geeft aan wat je denkt dat de waarschijnlijkheid is. Dat klinkt misschien niet erg wetenschappelijk maar in de praktijk is dit misschien wel de meest gebruikte methode. Vooral omdat je hem ook kan gebruiken als het experiment niet herhaalbaar is. De bayesiaanse methode zegt eigenlijk dat je nooit helemaal zeker kunt stellen wat de grootte van een kans is. Dat voelt misschien wat gek, maar het enige wat het zegt is dat ook bij een berekende kanswaarde er een mate van onzekerheid is. Ook daar is er sprake van een 'meetonzekerheid'.


> **Een voorbeeld** In een wielerronde staat een bergklassieker op het programma van vandaag. De wedstrijd is nog niet gestart. Er staan twee sterke renners,  Verstappen en Onana, op de gedeelde eerste plaats van het klassement en de voorsprong met de derde wielrenner is meer dan 20 minuten. Het lijkt dus waarschijnlijk dat aan het einde van de dag Verstappen of Onana op de eerste plaats in het klassement zal staan. Op bergetappes wint Onana 9 van de 10 keer met een flinke voorsprong van Verstappen. Wie denk je dat er vandaag wint? <br><br>
>
> We kunnen het experiment natuurlijk niet herhalen maar het lijkt zeer waarschijnlijk dat Onana aan het einde van de dag op nummer 1 zal eindigen. 
Hier maken we gebruik van de subjectieve methode van Bayes. Om het te kwantificeren kunnen we misschien zelfs wel zeggen dat de kans 0.9 is.<br><br>
>
> Maar nu zitten we aan het ontbijt en we zien dat Onana geen hap door zijn keel krijgt. Hij is duidelijk erg ziek. Verstappen daarentegen ziet er fris en sterk uit. <br>
Hoe waarschijnlijk denk je nu dat het is dat Onana zal winnen?
><br><br> 
> Het lijkt nu toch een stuk minder waarschijnlijk dat Onana zal winnen. Misschien schat je nu de kansen lager in dan de 0.9 waarmee je begon. Misschien heb je zelfs wel informatie uit het verleden waaruit je weet hoeveel langzamer renners zijn als ze er zo ziek uitzien als Onana. Wat voor impact dat heeft op hun performance. Dan zouden we ons kans van 0.9 kunnen 'updaten' met de nieuwe informatie. Dat is typisch een Bayesiaanse methode om kansen uit te rekenen.

Beide methodes worden dus gebruikt, maar de Bayesiaanse methode, of zelfs een hybride methode vindt vooral zijn toepassing in heel complexe modellen en voorspellingen. In dit vak zullen we echter vooral werken met de frequentist methode.
Wat in elk geval belangrijk is, is om altijd heel precies te vermelden wat de voorwaardes zijn geweest waaronder de kans is uitgerekend. Ook bij de frequentist methode!




## Rekenen met kansen

Er zijn een paar basisregels waar kansen aan voldoen. 

1. **Behoud van kans:** <a name =BehoudKans></a>
Een gebeurtenis, $$A$$, kan plaatsvinden, of het kan niet plaatsvinden. De kans is behouden en dat betekent dat: <br>
$$ P(A) + P(\text{niet A}) = 1$$<br>

2. **Complementregel:** <a name="ComplementRegel"></a>
Een direct gevolg hiervan is dat $$P(\text{niet A})$$ het complement is van $$P(A)$$ ofwel:<br>
$$ P(\text{niet A}) = 1 - P(A) .$$<br>
3. Als de uitkomst $$B$$ *bestaat* dan geldt: <br> 
$$0 < P(B) \leq 1.$$<br>
Een kans moet dus altijd groter zijn dan nul voor alle elementen in de uitkomstenverzameling. 
3. **De *of* Regel**:  <a name="OfRegel"></a> 
Als de uitkomsten $$A$$ en $$B$$ *wederzijds uitsluitend* zijn, ofwel als $$A$$ plaatsvindt, dan kan $$B$$ nooit plaats vinden, dan geldt:<br>
$$P(A\text{ of }B) \equiv P(A \cup B) = P(A) + P(B).$$<br>
We mogen in dit geval de kansen dus optellen.
4. **De *en* regel**: <a name="EnRegel"></a>
Als de uitkomsten $$A$$ en $$B$$ onafhankelijk zijn, dus als je $$A$$ een uitkomst is dan zegt dat niets over de kans op $$B$$, dan geldt: <br>
$$P(A\text{ en }B) = P(A) \cdot P(B).$$<br>


We gaan voor elk van deze regels een voorbeeld geven. We kijken hiervoor naar een kaartendek.
De uitkomstenverzameling van een kaartendek is: <br><br>
{<span style="color:red">1♥,2♥,3♥,4♥,5♥,6♥,7♥,8♥,9♥,H♥,D♥,K♥,A♥,<br>
1♦,2♦,3♦,4♦,5♦,6♦,7♦,8♦,9♦,H♦,D♦,K♦,A♦,</span><br>
1♠,2♠,3♠,4♠,5♠,6♠,7♠,8♠,9♠,H♠,D♠,K♠,A♠,<br>
1♣,2♣,3♣,4♣,5♣,6♣,7♣,8♣,9♣,H♣,D♣,K♣,A♣}<br><br>
Dit zijn in totaal 52 kaarten verdeeld over 2 kleuren: rood en zwart. We trekken in de volgende voorbeelden steeds 1 kaart.

> **Voorbeeld 1 - behoud van kans/complement regel:** <br>
>
> - De kans om een harten 5 uit een dek kaarten te trekken is precies: P(<span style="color:red">5♥</span>)= $$\frac{1}{52}$$. <br>
> - De kans om een *andere kaart dan een harten 5* te trekken is gelijk aan: 1-P(<span style="color:red">5♥</span>) = $$1-\frac{1}{52} = \frac{51}{52}.$$<br>
> - De kans om een rode kaart te trekken is precies $$\frac{26}{52} = \frac{1}{2}$$ en is precies gelijk aan de kans om een zwarte kaart te trekken $$(1 - \frac{1}{2} = \frac{1}{2}).$$


> **Voorbeeld 2 - groter dan nul:** <br>
>
> - Voor elke kaart in het dek is er een kans dat je hem trekt. 


> **Voorbeeld 3 - de of-regel:** <br>
>
> - De kans dat je een 3 of een 5 trekt is gelijk aan P(3)+P(5) = $$\frac{1}{13}+\frac{1}{13} = \frac{2}{13}.$$ <br>
> - De kans dat je een 3 of een rode kaart trekt kunnen we niet zomaar optellen. Er bestaan ook rode kaarten met een 3. 


> **Voorbeeld 4 - de en-regel:** <br>
>
> - De kans dat je een 3 trekt die ook een rode kaart is kunnen we uitrekenen met: <br>
> $$\displaystyle{P(\text{rood en }3) = P(\text{rood}) \cdot P(3) =  1/2 \cdot 4/52 = 2/52.}$$<br>
> Er zijn maar twee rode 3 kaarten in het dek, dus dat klopt. Er zijn evenveel rode drie kaarten als zwarte drie kaarten en daarom mag je ze in dit geval vermenigvuldigen. De uitkomsten zijn onafhankelijk. <br>
> - De kans dat je een 9♥ en een A♣ trekt. Deze kansen zijn niet onafhankelijk. Als je een 9♥ trekt, zegt dat al direct iets over de kans dat deze kaart ook een A♣ is (die is namelijk gereduceerd tot 0). Hier kunnen we de en-regel dus niet toepassen.


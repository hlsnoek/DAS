# Basisbegrippen in de statistiek

1. Ordered TOC
{:toc}

## Introductie 

Statistische data analyse is een belangrijk onderdeel in vele werkvelden.
Als wetenschapper zul je later hoogstwaarschijnlijk te maken krijgen met het verzamelen van data bij het onderzoek dat je uitvoert.
Deze data wordt dan verzameld om een antwoord te vinden op een onderzoeksvraag of hypothese.
Maar wanneer kun je zeggen dat een hypothese ook juist is?
En wanneer heb je eigenlijk genoeg data verzameld?
Andere wetenschappers moeten overtuigd zijn van de conclusies die jij uit jouw onderzoek trekt.

Alle kennis die we tot nu toe hebben over de Natuurkunde is tot stand gekomen met het uitvoeren van experimenten en het analyseren van de uitkomsten.
Voor het bestuderen van Natuurkundige en Sterrenkundige theori\"en is geen kennis nodig van statistiek en data analyse technieken.
Voor het uitvoeren van de wetenschap, het vinden van bewijzen voor nieuwe theori\"en is kennis hiervan echter essentieel. 


Denk bijvoorbeeld eens terug aan het moment waarop aan de wereld kenbaar werd gemaakt dat, met grote waarschijnlijkheid, het Higgs deeltje was gevonden (ATLAS en CMS teams op CERN in 2012). In 1964 is het bestaan van dit deeltje al voorspeld om de massa van de elementaire deeltjes zoals elektronen, muonen en quarks te kunnen verklaren (deze voorspelling is trouwens niet alleen door Peter Higgs gedaan maar ook (iets) eerder al door Robert Brout en François Englert).

Het Higgs deeltje is niet te zien met het menselijk oog, dus je kunt het alleen vinden door de eventuele sporen die het deeltje achterlaat (botsingen met andere deeltjes). Om deze sporen te kunnen vinden en hier een patroon in te ontdekken, is het nodig om heel veel data te verzamelen. De bulk data wordt in eerste instantie verzameld in grote tabellen. Het is echter lastig om hier patronen in te vinden, de data moet verwerkt worden tot een visuele weergave. Hieronder staat de visueel weergegeven data, waaruit is geconcludeerd dat het Higgs deeltje met grote waarschijnlijkheid bestaat (Bron: ATLAS Collaboration / Physics Letters B 716 (2012) 1–29, [Link](https://doi.org/10.1016/j.physletb.2012.08.020)):


<p align="center">![higgs1](Higgs_figuur_fig1.PNG){:height="400px"}&emsp;![higgs2](Higgs_figuur_fig2.PNG){:height="400px"}</p>


Het visueel weergeven van de data alleen is niet genoeg, de data moet ook vergeleken worden met de achtergrondenergie (linker figuur) of met een model (rechter figuur). Daarnaast kun je niet zoveel met de figuur als er geen uitleg wordt gegeven, daarom wordt in het onderschrift en het artikel zelf, toegelicht wat er te zien is in de figuren. Dan zijn de vragen 'wat zien we?' en 'ten opzichte van wat zien we dat dan?' beantwoord, maar nu moet de vraag nog beantwoord worden of het waargenomen verschil in energie (het piekje) wel groot genoeg is om te kunnen spreken van een nieuw deeltje. Is het niet gewoon de achtergrondenergie die waargenomen is? Om deze vragen te kunnen beantwoorden is de data statistisch geanalyseerd. De uiteindelijke conclusie was dat er bijna 100% (namelijk 99.999997%) zekerheid gezegd kan worden dat als er een nieuw boson was gevonden die veel van de eigenschappen heeft zoals die voor het Higgs boson waren voorspeld.
Of beter als het Higgs boson niet zou bestaan, is de kans 1 in 3.5 miljoen dat we metingen zouden vinden zoals we ze hebben gezien.
Dat klinkt heel omslachtig, maar het is belangrijk in de wetenschap om heel precies te formuleren wat je eigenlijk hebt gedaan.


In deze cursus zullen we gaan kijken naar statistische data-analyse.

Deze week beginnen we met een aantal basisbegrippen in de statistiek. We gaan kijken naar het gemiddelde, variantie, de standaardafwijking, en coëfficiënt van variantie. Daarnaast bekijken we het verschil tussen een grafiek, een staafdiagram en een histogram en plotten we deze in Python voor verschillende datasets.


## Datasets beschrijven

Het verzamelen van data zelf is niet genoeg. Als we de data hebben moeten we deze kunnen beschrijven aan anderen. Stel we hebben een dataset met de temperatuur op elk van de 37 meetpunten van het KNMI in Nederland in de afgelopen twintig jaar.  Het is dan niet zo inzichtelijk om dit aan medewetenschappers te presenteren d.m.v. een enorme tabel (elke 10 minuten wordt een meting gedaan door de weerstations) met de mededeling 'dit was de temperatuur in de afgelopen twintig jaar'. 
Een dataset heeft verschillende eigenschappen, zo zouden we bijvoorbeeld iets kunnen zeggen over het midden van de dataset, de waarden die de temperatuur minimaal en maximaal aanneemt, en hoe ver elke temperatuur van het midden af zit.

In de secties hieronder behandelen we verscheidene begrippen.


### Populatie versus steekproef
---

Een *populatie* bestaat uit alle personen/dieren/objecten binnen de groep waarin we geïnteresseerd zijn. Dit zouden bijvoorbeeld *alle* mensen in Nederland kunnen zijn tussen de 30 en 40 jaar, of *alle* lieveheersbeestjes die in Noorwegen leven. Nu is het zo dat het vaak lastig is om van *alle* personen/dieren/objecten (hierna uniform aangeduid met 'elementen') in een groep data te verzamelen. Het kost bijvoorbeeld erg veel tijd (en geld) om data te verzamelen over alle personen tussen de 30 en 40 jaar in Nederland (of om alle lieveheersbeestjes in Noorwegen te vangen). Het is dan veel makkelijker om data over een deel van deze groep te verzamelen en om zo iets te zeggen over de gehele doelgroep. Zo zouden we bijvoorbeeld data kunnen verzamelen van een random selectie van 200 personen in Nederland tussen de 30 en 40 jaar. Dit wordt een *steekproef* genoemd, de deelgroep wordt in het Engels vaak aangeduid met een *sample*. Een steekproef is dus een gedeelte van de populatie.


### Het gemiddelde
---

Het gemiddelde van een dataset geeft een maat voor het centrum van de waarden die de dataset aanneemt. We onderscheiden het populatiegemiddelde en het steekproefgemiddelde.

#### Populatiegemiddelde

Als we metingen kunnen doen voor een gehele populatie, en we bepalen het gemiddelde, dan spreken we van het *populatiegemiddelde*. Het populatiegemiddelde wordt vaak aangegeven met het symbool $$\mu$$. Het populatiegemiddelde wordt ook wel de *verwachtingswaarde* genoemd, deze wordt aangegeven met $$E(X)$$.

Als de dataset *discreet* verdeeld is (d.w.z. dat de uitkomsten alleen 'losse' waarden aan kunnen nemen en niet alle tussenwaarden in een interval) dan wordt het populatiegemiddelde/ de verwachtingswaarde gegeven door:

$$\mu=E(X)={\displaystyle \sum_{i=1}^{N}x_{i}\,p(x_i)} $$

Hierbij is $$N$$ het aantal elementen in de populatie, $$x_i,\dots,x_n$$ zijn de uitkomsten en $$p(x_i)$$ is de kans op elke uitkomst. Een Poissonverdeling is een voorbeeld van een discrete verdeling (komen we later nog op terug), maar ook het gooien van kop of munt levert een discrete verdeling op.
Is de kans op elke uitkomst gelijk dan wordt het populatiegemiddelde, bij een discrete verdeling, gegeven door:

$$\mu=E(X)= \frac{1}{N}{\displaystyle \sum_{i=1}^{N}x_{i}}$$

De kans op elke uitkomst is dan immers gelijk aan $$\frac{1}{N}$$.

Als de dataset *continu* is (d.w.z. dat alle waarden in een interval aangenomen kunnen worden; dit is bijvoorbeeld het geval bij metingen die decimale waarden opleveren) dan heeft deze verdeling een kansdichtheidsfunctie $$f(x)$$. Deze kansdichtheidsfunctie geeft aan welke kans er is op de waarden in de verdeling. Het verschil met de discrete verdeling is dat het bij een continue verdeling niet mogelijk is om de kans op *precies* een waarde $$a$$ binnen de verdeling te bepalen. Hierbij kun je bijvoorbeeld denken aan de verdeling van de lengte van alle mensen in Nederland. De kans om iemand te vinden met een lengte van *precies* 1 meter en 85 centimeter, is gelijk aan nul. Zelfs als een persoon hier dicht bij zit qua lengte zal er altijd een verschil zitten in de orde van millimeters, micrometers, nanometers, etc.   
Bij een continue verdeling kan wel de kans bepaald worden dat een waarde in een interval zit. Het populatiegemiddelde/ de verwachtingswaarde wordt daarom gegeven door de integraal over de waarden $$x$$ in de continue verdeling vermenigvuldigd met de kansdichtheidsfunctie $$f(x)$$:

$$\mu=E(X)={\displaystyle \int_{-\infty}^{\infty}x\,f(x)\,dx} $$

Een normale verdeling (komen we later op terug) is een voorbeeld van een continue verdeling, ook het meten van de tijd die het duurt voordat je aan de beurt bent bij de kassa levert een continue verdeling op.

#### Steekproefgemiddelde

Het is vaak onmogelijk om metingen te doen van een gehele populatie. Daarom wordt er vaak een steekproef gedaan waarbij er aselect (willekeurig) elementen uit de gewenste doelgroep worden gekozen. Uiteindelijk wordt deze steekproef dan gebruikt om iets te kunnen zeggen over de gehele populatie. Hierbij is het echter wel opletten, want de steekproef moet een representatieve doorsnede zijn van de hele populatie. De steekproef moet groot genoeg zijn en de elementen van de steekproef moeten aselect gekozen worden. Je kunt je voorstellen dat als we de lengte van drie mensen in Nederland meten, we nog niet zoveel kunnen zeggen over de lengte van de gehele populatie die bestaat uit alle mensen in Nederland. Als we de lengte van 1000 mensen zouden meten dan krijgen we al een beter beeld van de verdeling van lichaamslengte in Nederland, en kiezen we 100000 mensen dan krijgen we een nog veel beter beeld van de verdeling.

Het steekproefgemiddelde $$\overline{x}$$ van een dataset is de som van de waarden $$x_1,\dots,x_n$$ in de set gedeeld door het aantal datapunten $$n$$:

$$\overline{x}=\frac{1}{n}{\displaystyle \sum_{i=1}^{n}x_{i}}$$

Het steekproefgemiddelde wordt zo vaak gebruikt dat dit veelal wordt aangeduid als 'het gemiddelde'. Je ziet dat het steekproefgemiddelde erg lijkt op de uitdrukking voor het populatiegemiddelde van een discrete verdeling. Het verschil is dat het steeksproefgemiddelde niet gelijk is aan de verwachtingswaarde van de populatie. Het is wel zo dat, hoe beter de steekproef overeenkomt met de populatie, des te dichter komt het steekproefgemiddelde bij de verwachtingswaarde van de populatie. Dit geldt zowel voor steekproeven met een discrete als een continue verdeling. Met behulp van een goed uitgevoerde steekproef kan het statistische gedrag van een populatie dus benaderd worden.


### De mediaan
---

De mediaan is een maat voor het midden van de elementen in een dataset of verdeling. Hierbij is de data van lage naar hoge waarde gesorteerd.

#### Populatiemediaan

Als we data verzamelen voor een gehele populatie dan is de mediaan $$m$$ de waarde die hoort bij het punt waarop de kans om een element te vinden met een waarde $$x\leq m$$, gelijk is aan 50%. In andere woorden wil dit zeggen, dat de helft van de populatie voldoet aan de voorwaarde $$x \leq m$$. Als bijvoorbeeld de helft van de Nederlanders een lengte heeft kleiner of gelijk aan 1 meter en 85 centimeter, dan is deze 1.85 meter de mediaan $$m$$ van de populatie.  

Voor een symmetrische distributie (zoals een normale verdeling), is de mediaan gelijk aan het populatiegemiddelde $$\mu$$.


#### Steekproefmediaan

Als we alle datapunten in een dataset sorteren van lage naar hoge waarde, dan is de mediaan de waarde van het element in het midden van de set. Is er sprake van een oneven aantal elementen dan is de mediaan de gemiddelde waarde van de twee elementen in het midden van de set.

Neem bijvoorbeeld de volgende datapunten: 

$$10,11,12,13,14$$ 

De data is al gesorteerd van laag naar hoog, en het derde element is in dit geval het middelste element. Het derde element heeft de waarde $$12$$. De mediaan van deze set is dus gelijk aan $$12$$.
Hebben we een set met een even aantal datapunten, bijvoorbeeld

$$ 8,9,10,11,12,13,14,15$$ 

dan zitten het 4e en het 5e element in het midden. De mediaan is nu gelijk aan de gemiddelde waarde van deze elementen. De elementen hebben waarde $$11$$ en $$12$$, wat betekent dat de mediaan gelijk is aan $$\frac{11+12}{2} = 11.5$$.

Voor symmetrische datasets zijn het gemiddelde en de mediaan gelijk aan elkaar.

### De modus
---

#### Steekproefmodus

De modus van een dataset is de waarde die met de grootste frequentie in de dataset voorkomt. Hebben we bijvoorbeeld de dataset 

$$2,2,3,4,7,7,7,9$$ 

dan komen de 3, de 4 en de 9 elk één keer voor, het getal 2 komt twee keer voor en het getal 7 komt drie keer voor. Het meest voorkomende getal is dus de 7 en dit is de modus van de dataset. Als een dataset één modus heeft dan wordt deze *unimodaal* genoemd.

Het komt ook voor dat er twee of meer getallen zijn die even vaak voorkomen. Een dataset met twee getallen als modus wordt ook wel *bimodaal* genoemd, een dataset met meer dan twee getallen als modus wordt *multimodaal* genoemd.

Een voorbeeld van een bimodale dataset is:

$$1,2,3,3,4,4,4,5,6,11,11,11,15$$

zowel het getal 4 als het getal 11 komen drie keer voor in de set. De set is dus bimodaal met modus 4 en modus 11.


#### Populatiemodus

Voor een continue verdeling met dichtheidsfunctie $$f(x)$$ is de modus gedefinieerd als de waarde die met de grootste frequentie in de verdeling voorkomt. Dit houdt in dat het de waarde is die hoort bij het maximum van de dichtheidsfunctie $$f(x)$$. Een voorbeeld van een verdeling (een normale verdeling) met één modus is weergegeven in het figuur hieronder:


<p align="center">![higgs](Basisbegr_Normaleverd_Modus.png){:width="30%"}</p>


Bij een verdeling die beschreven kan worden met een dichtheidsfunctie is het ook mogelijk om meerdere waarden te hebben die een modus zijn. Elk van de waarden waarvoor de dichtheid lokaal maximaal is wordt in principe als een modus gezien. Hierbij hoeven de pieken dus niet gelijk van hoogte te zijn. Bij verdelingen geldt dezelfde naamgeving als bij de steekproefmodus. Heeft de verdeling één lokaal maximum dan is deze *unimodaal*, als er twee lokale maxima zijn dan is de verdeling *bimodaal*, en als er meer lokale maxima zijn dan is deze *multimodaal*. Hieronder is een voorbeeld gegeven van een bimodale en multimodale verdeling.


<p align="center">![higgs](Basisbegr_Normaleverd_BiModaal.png){:width="30%"}&emsp;&emsp;![higgs](Basisbegr_Normaleverd_MultiModaal.png){:width="30%"}</p>


### Spreiding van data
---

De spreiding geeft een beeld van de mate waarin datapunten in een set verspreid zijn. Er zijn verschillende maten om de spreiding van een dataset mee aan te geven. Hieronder zullen we de range, variantie, coëfficiënt van variantie en de standaardafwijking bespreken. 

#### Range (spreidingsbreedte)

De range is de afstand tussen de hoogste en de laagste waarde in een dataset. Hebben we bijvoorbeeld de dataset

$$50,70,72,76,76,80,120$$

dan is de range van deze dataset gelijk aan $$120-50=70$$.

De range geeft dus aan hoe breed de dataset in totaliteit is. De range is niet altijd een handige maat voor de spreiding van een dataset. Zo zouden we bijvoorbeeld de volgende dataset kunnen hebben:

$$1,2,3,4,5,5,5,6,6,6,7,7,10$$

De range is in dit geval $$10-1=9$$. Maar stel dat we een foutieve meting doen (of we maken een typefout in het overnemen van de data), en we hebben de volgende dataset:  

$$1,2,3,4,5,5,5,6,6,6,7,7,10,30$$

De range wordt nu $$30-1=29$$. Dus onder invloed van één foutief datapunt geeft de range nu een veel grotere mate van spreiding aan. 

#### Variantie

De variantie geeft aan in welke mate de data verspreid is rondom het gemiddelde van de dataset. Dit geeft met name ook een maat voor de spreiding van de datapunten onderling. Hoe groter de variantie des te groter is de spreiding tussen de afzonderlijke punten. 

De variantie kan aangegeven worden met $$\sigma^2$$, met $$s^2$$ of met \(Var(X)\). Deze notaties worden doorgaans gebruikt voor de populatievariantie, steekproefvariantie en de variantie van een kansverdeling respectievelijk.

Voor een *populatie* wordt de variantie gegeven door:

$$\sigma^2 = \displaystyle \frac{\displaystyle \sum_{i=1}^{N}(x_i - \mu)^2}{N}$$

De variantie is dus de som van het verschil tussen elk punt en het gemiddelde in het kwadraat, gedeeld door de populatiegrootte $$N$$. 

Voor een *steekproef* is de formule van de variantie vrijwel gelijk aan de formule bij een populatie. Nu gebruiken we echter het steekproefgemiddelde $$\overline{x}$$, en we delen niet door het aantal datapunten $$n$$ maar door $$n-1$$. Delen door $$n-1$$ wordt de *unbiased variance* genoemd. Bij een steekrpoef geeft dit een accurater resultaat dan delen door het aantal termen $$n$$ (deze kun je ook tegenkomen en wordt de *biased variance* genoemd). De 'unbiased' variantie voor een steekproef wordt gegeven door:

$$s^2 = \displaystyle \frac{\displaystyle \sum_{i=1}^{n}(x_i - \overline{x})^2}{n-1}$$

#### Standaardafwijking

Net zoals de variantie geeft de standaardafwijking geeft aan in welke mate de data verspreid is rondom het gemiddelde van de dataset. Ook de standaardafwijking geeft een maat voor de spreiding van de datapunten onderling. Hoe groter de standaardafwijking des te groter is de spreiding tussen de afzonderlijke punten. 

De standaardafwijking is de positieve wortel van de variantie. Voor een populatie wordt de standaardafwijking dus gegeven door:

$$\sigma = \sqrt{\sigma^2} = \sqrt{\displaystyle \frac{\displaystyle \sum_{i=1}^{N}(x_i - \mu)^2}{N}}$$

en voor een steekproef wordt de standaard afwijking gegeven door:

$$s = \sqrt{s^2} = \sqrt{\displaystyle \frac{\displaystyle \sum_{i=1}^{n}(x_i - \overline{x})^2}{n-1}}$$

Een verschil tussen de standaardafwijking en de variantie is de eenheid. De standaardafwijking heeft dezelfde eenheid als het gemiddelde terwijl de variantie de eenheid in het kwadraat heeft. Bij het rapporteren van resultaten wordt daarom vaak de standaarddeviatie van een verdeling of steekproef gegeven in plaats van de variantie. In het werken met een dataset maakt het echter niet uit welk van de twee je gebruikt. Bij een meer wiskundige benadering kan het eenvoudiger zijn om met de variantie te werken omdat er dan geen sprake is van een wortel. 


#### Coëfficiënt van variatie

De coëfficiënt van variatie wordt ook wel de relatieve standaardafwijking genoemd. De coëfficiënt van variatie geeft, net zoals de standaardafwijking en de variantie, een maat voor de spreiding van de populatie of dataset. 

De coëfficiënt van variatie wordt gegeven door de verhouding tussen de standaardafwijking en het gemiddelde.
Voor een populatie is de coëfficiënt van variantie $$c_v$$ dan:

$$c_{v} = \frac{\sigma}{\mu}$$

Met $$\sigma$$ de standaardafwijking van de populatie en $$\mu$$ het populatiegemiddelde.

De steekproefvariatie $$\hat{c_v}$$ wordt gegeven door:

$$\hat{c_v} = \frac{s}{\overline{x}}$$

Met $$s$$ de standaardafwijking van de steekproef en $$\overline{x}$$ het steekproefgemiddelde.

Het verschil met de variantie en de standaardafwijking is dat de coëfficiënt van variatie dimensieloos is. Dit is bijvoorbeeld handig als er meerdere datasets vergeleken moeten worden die verschillende eenheden hebben. Ook als de gemiddelde waarden van verschillende datasets erg uiteen liggen is het beter om de coëfficiënt van variatie te gebruiken i.p.v. de standaardafwijking.

Een nadeel van het gebruik van de coëfficiënt van variatie is dat er gedeeld wordt door het gemiddelde. Als dit gemiddelde vlak bij nul ligt dan gaat de coëfficiënt van variatie richting oneindig. Als het gemiddelde dan een klein beetje veranderd heeft dit een groot effect op de coëfficiënt. Als het gemiddelde van een dataset dus dicht bij nul ligt dan is het beter om de standaardafwijking of de variantie te gebruiken. 


## Kansrekening - start

In dit onderdeel maken we een start met de kansrekening.

### Kansdefinitie

Een kans is een waarde tussen de $$0$$ en de $$1$$ die aangeeft hoe waarschijnlijk een gebeurtenis is.
Een kans van $$0$$ geeft aan dat iets *niet kan* gebeuren en een kans van $$1$$ geeft aan dat iets *altijd* gebeurt. Een kans van $$\frac{1}{2}$$ geeft aan dat iets naar verwachting de helft van de tijd zal gebeuren.

De kans op een *gebeurtenis* $$P(\text{gebeurtenis})$$ wordt gegeven door het aantal mogelijkheden waarbij de gebeurtenis kan optreden gedeeld door het totaal aantal mogelijkheden:

$$P(\text{gebeurtenis}) = \frac{\text{Aantal mogelijkheden waarbij de gebeurtenis optreedt}}{\text{Het totale aantal mogelijkheden}}$$ 

De kansen op alle mogelijke uitkomsten bij elkaar opgeteld zijn gelijk aan 1.

Als er $$n$$ mogelijke uitkomsten zijn, die allemaal even waarschijnlijk zijn dan is de kans op elke uitkomst gelijk aan 

$$P(\text{gebeurtenis}) = \frac{1}{n}$$

Stel we gooien met een zes zijdige dobbelsteen (afgekort tot D6). De kans om bijvoorbeeld 4 te gooien is gelijk aan:

$$P(\text{we gooien 4 met een D6}) = \frac{\text{Aantal mogelijkheden waarbij de gebeurtenis optreedt}}{\text{Het totale aantal mogelijkheden}} \frac{1}{6}$$

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





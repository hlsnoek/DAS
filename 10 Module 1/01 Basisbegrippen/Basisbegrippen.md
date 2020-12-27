# Basisbegrippen in de statistiek

1. Ordered TOC
{:toc}



## Datasets beschrijven

Als we een set metingen (data) hebben verzameld kunnen we deze op verschillende manier gebruiken. Vaak willen we bepaalde kenmerken van de dataset weten. Stel we hebben een dataset met de temperatuur op elk van de 37 meetpunten van het KNMI in Nederland in de afgelopen twintig jaar.  Het is dan niet zo inzichtelijk om dit aan medewetenschappers te presenteren d.m.v. een enorme tabel (elke 10 minuten wordt een meting gedaan door de weerstations) met de mededeling 'dit was de temperatuur in de afgelopen twintig jaar'. Uit deze dataset kun je natuurlijk een enorme hoeveelheid informatie halen. Bijvoorbeeld wat is de koudste temperatuur die in de afgelopen 20 jaar in Nederland is gemeten. Maar ook: Wat is de gemiddelde temperatuur in de maand Juli. Of: Hoeveel kouder zijn de winters in het binnenland ten opzichte van de kust regio's. 

In de secties hieronder behandelen we verschillende veelvoorkomende definities van kenmerken van data.


### Populatie en steekproef

Voordat we het gaan hebben over de kenmerken van data is het belangrijk om te kijken naar de data zelf. Waar komt die vandaan? We maken hierbij onderscheid tussen de **populatie** en een **steekproef**.

Een **populatie** bestaat uit alle personen/dieren/objecten binnen de groep waarin we geïnteresseerd zijn. Dit zouden bijvoorbeeld *alle* mensen in Nederland kunnen zijn tussen de 30 en 40 jaar, of *alle* lieveheersbeestjes die in Noorwegen leven. Nu is het zo dat het vaak lastig is om van *alle* personen/dieren/objecten (hierna uniform aangeduid met 'elementen') van een groep gegevens te verzamelen. Het kost bijvoorbeeld erg veel tijd (en geld) om data te verzamelen over alle personen tussen de 30 en 40 jaar in Nederland (of om alle lieveheersbeestjes in Noorwegen te vangen). Het is dan veel makkelijker om data over een deel van deze groep te verzamelen en om zo toch iets te kunnen zeggen over de gehele doelgroep. Zo zouden we bijvoorbeeld data kunnen verzamelen van een willekeurige selectie van 200 personen in Nederland tussen de 30 en 40 jaar. Dit wordt een *steekproef* genoemd, de deelgroep wordt in het Engels vaak aangeduid met een *sample*. Een steekproef is dus een gedeelte van de populatie.
Vaak is het trouwens zelfs helemaal niet mogelijk om de hele populatie te meten. Denk bijvoorbeeld maar eens aan de gemiddelde massa van een ster. Dan zouden we deze meting moeten verrichten voor alle sterren in het universum.

We maken onderscheid in de namen en de notatie van de kenmerken van data. Kenmerken van meetgegevens (data) van een populatie noemen we **parameters**, kenmerken van steekproeven noemen we **statistieken**. Het is belangrijk om onderscheid te maken. Als we bijvoorbeeld de gemiddelde leeftijd willen weten van alle eerstejaars Natuur- en Sterrenkunde studenten in Amsterdam dan maakt het uit of we de gegevens hebben verzameld van alle eerstejaars of dat we de gemiddelde leeftijd inschatten door de gegevens te noteren van de studenten uit je eigen werkgroep. In het eerste geval hebben we gegevens van de hele populatie en spreken we van een parameter en weten we de uitkomst exact. In het tweede geval hebben we een steekproef gedaan van een selectie van de eerstejaars, we spreken dan van een statistiek en op deze statistiek komt een onzekerheid. We hebben immers niet alle informatie van de populatie en het kan zijn dat het gemiddelde van de steekproef afwijkt van het gemiddelde van de gehele populatie. Het is dus belangrijk om je te realiseren of je de gegevens bekijkt van een steekproef of een populatie als je de resultaten interpreteert.

Als je een steekproef neemt is het belangrijk om op twee dingen goed te letten: de grootte van de steekproef en hoe representatief deze is. 
Je kunt je voorstellen dat als we de lengte van drie mensen in Nederland meten, we nog niet zoveel kunnen zeggen over de lengte van de gehele populatie die bestaat uit alle mensen in Nederland. Als we de lengte van 1000 mensen zouden meten dan krijgen we al een beter beeld van de verdeling van lichaamslengte in Nederland, en kiezen we 100000 mensen dan krijgen we een nog veel beter beeld van de verdeling. Hoe groter de steekproef, hoe nauwkeuriger de statistiek is die we willen weten.
(We zeggen dan vaak dat we *meer statistiek* hebben.)

Ook is het belangrijk hoe we de steekproef nemen. Als we bijvoorbeeld de lengte gegevens van 1000 mensen nemen dan krijgen we een vertekend beeld als we hiervoor de leden van de Nederlandse Basketbal vereniging uitnodigen, of de gegevens van 1000 kleuters hiervoor gebruiken. Je moet dus altijd goed kijken of de steekproef de je neemt wel representatief is voor de hele groep. 


## Veel gebruikte parameters en statistieken

### Het gemiddelde

Het gemiddelde van een dataset geeft een maat voor het centrum van de waarden die de dataset aanneemt. We onderscheiden het populatiegemiddelde (parameter) en het steekproefgemiddelde (statistiek). Hoe groter de steekproef hoe meer het gemiddelde van de steekproef overeenkomt met het populatiegemiddelde. 

Het gemiddelde kun je berekenen door alle waardes in de dataset te sommeren en te delen door de grootte van de dataset. We maken onderscheid in de notatie voor het gemiddelde van een steekproef en die van het populatiegemiddelde.


Het steekproef gemiddelde $$\bar{x}$$ (x-streep of in het Engels: x-bar) van een dataset is de som van de waarden $$x_1,\dots,x_n$$ in de set gedeeld door het aantal datapunten in de steekproef: $$n$$:

$$\bar{x}=\frac{1}{n}{\displaystyle \sum_{i=1}^{n}x_{i}}$$

Het steekproef gemiddelde wordt zo vaak gebruikt dat dit veelal wordt aangeduid als 'het gemiddelde'. 
Voor het gemiddelde wordt ook vaak de 'vishaak-notatie' gebruikt: $$< {x} >$$.


Het populatiegemiddelde wordt als volg genoteerd: 

$$\mu = \frac{1}{N}{\displaystyle \sum_{i=1}^{N}x_{i}}$$

Hierbij is $$N$$ het aantal elementen in de populatie, en zijn $$x_i,\dots,x_N$$ de waardes van de grootheid in de populatie. Let op dat voor de steekproefgrootte $$n$$ wordt gebruikt en voor de populatiegrootte $$N$$. Een andere veel gebruikte notatie voor het populatiegemiddelde is $$E(x)$$ waar de E van het Engelse woord *expectation* komt. Ook kun je een subscript toevoegen om aan te geven van welke grootheid je het gemiddelde berekent, bijvoorbeeld hier $$\mu_x$$.

Je ziet dat het steekproef gemiddelde erg lijkt op de uitdrukking voor het populatiegemiddelde. Het verschil is dat het steekproefgemiddelde niet persé gelijk is aan de verwachtingswaarde van de populatie. Het is wel zo dat, hoe beter de steekproef overeenkomt met de populatie, des te dichter komt het steekproef gemiddelde bij de verwachtingswaarde van de populatie. Met behulp van een goed uitgevoerde steekproef kan het statistische gedrag van een populatie dus benaderd worden.

> Stel je voor dat we de volgende steekproef hebben: $$ X = \{-5,1,14,12,0\} $$. De gemiddelde waarde voor de data is nu dus 
> 
> $$ \bar{x} = \frac{1}{5} \cdot ( -5 + 1+ 14+12+0)= \frac{1}{5} \cdot 22 = 4.4$$



### De mediaan

De mediaan is een maat voor het midden van de elementen in een gesorteerde dataset of verdeling. De mediaan is zo gedefinieerd dat je precies 50% kans hebt om een waarde te vinden die lager is dan de mediaan en 50% kans om een waarde te vinden die hoger is dan de mediaan.

Als we alle datapunten in een dataset sorteren van lage naar hoge waarde, dan is de mediaan de waarde van het element in het midden van de set. Is er sprake van een even aantal elementen dan is de mediaan de gemiddelde waarde van de twee elementen in het midden van de set.


> Stel dat we de volgende dataset hebben: $$X = \{ 13,11,10,14,12,9 \} $$. <br>
> Het eerste wat we moeten doen om de mediaan te vinden is de dataset sorteren:  $$\{9,10,11,12,13,14\}$$ . <br>
> We hebben een dataset met een even aantal datapunten, de mediaan ligt hier dus tussen twee waardes in: $$\frac{(11+12)}{2} = 11.5$$.

De mediaan en het gemiddelde *kunnen* dezelfde waarde hebben, maar dat hoeft niet zo te zijn. 
Voor het voorbeeld hierboven is dat wel het geval (reken maar na). Maar voor de dataset uit het voorbeeld voor het berekenen van het gemiddelde is dit niet zo. Kijk maar!

> We bekijken de steekproef $$ X = \{-5,1,14,12,0\} $$. Het gemiddelde was berekend op 4.4. We gaan nu kijken waar de mediaan ligt. Eerst sorteren we de dataset: $$ \{ -5,0,1,12,14\}$$. Dit is een oneven dataset en de mediaan ligt dus op de middelste waarde van de gesorteerde dataset: 1. 


Voor symmetrische datasets zijn het gemiddelde en de mediaan altijd gelijk aan elkaar, voor asymmetrische datasets is dit niet het geval. Bij een symmetrische dataset is de data precies gespiegeld rond het gemiddelde. Dit is makkelijker uit te leggen aan de hand van datadistributies. We komen hier later op terug.


### De modus

De modus van een dataset is de waarde die met de grootste frequentie in de dataset voorkomt. Hebben we bijvoorbeeld de dataset 

$$2,2,3,4,7,7,7,9$$ 

dan komen de 3, de 4 en de 9 elk één keer voor, het getal 2 komt twee keer voor en het getal 7 komt drie keer voor. Het meest voorkomende getal is dus de 7 en dit is de modus van de dataset. Als een dataset één modus heeft dan wordt deze *unimodaal* genoemd.

Het komt ook voor dat er twee of meer getallen zijn die vaker voorkomen dan andere waardes. Een dataset met twee getallen als modus wordt ook wel *bimodaal* genoemd, een dataset met meer dan twee getallen als modus wordt *multimodaal* genoemd.

Een voorbeeld van een bimodale dataset is:

$$1,2,3,3,4,4,4,5,6,11,11,11,15$$

zowel het getal 4 als het getal 11 komen drie keer voor in de set. De set is dus bimodaal met modus 4 en modus 11.

Bij sommige soorten dataverdelingen is het gebruikelijker om over de modus te praten dan over het gemiddelde of de mediaan. Een voorbeeld hiervan is de [Landau](https://en.wikipedia.org/wiki/Landau_distribution) distributie die een slecht gedefinieerd gemiddelde of mediaan kent door een lange staart in de distributie.

Voor unimodale symmetrische distributies ligt het gemiddelde, de mediaan en het gemiddelde precies op dezelfde plek. 


## Spreiding van data

De spreiding geeft een beeld van de mate waarin datapunten in een set verspreid zijn. Er zijn verschillende maten om de spreiding van een dataset mee aan te geven. Hieronder zullen we **de spreidingsbreedte ** (ook wel de *range*), **de variantie**, **coëfficiënt van variantie** en **de standaarddeviatie** (ook wel de *standaardafwijking*) bespreken. 

### Spreidingsbreedte (range)

De range is de afstand tussen de hoogste en de laagste waarde in een dataset. Hebben we bijvoorbeeld de dataset

$$50,70,72,76,76,80,120$$

dan is de range van deze dataset gelijk aan $$120-50=70$$.

De range geeft dus aan hoe breed de dataset in totaliteit is. De range is niet altijd een handige maat voor de spreiding van een dataset. Zo zouden we bijvoorbeeld de volgende dataset kunnen hebben:

$$1,2,3,4,5,5,5,6,6,6,7,7,10$$

De range is in dit geval $$10-1=9$$. Maar stel dat we een foutieve meting doen (of we maken een typefout in het overnemen van de data), en we hebben de volgende dataset:  

$$1,2,3,4,5,5,5,6,6,6,7,7,10,30$$

De range wordt nu $$30-1=29$$. Dus onder invloed van één foutief datapunt geeft de range nu een veel grotere mate van spreiding aan. 


### Standaarddeviatie en variantie

De standaarddeviatie (ook wel de standaardafwijking) geeft aan in welke mate de data verspreid is rondom het gemiddelde van de dataset. Dit geeft met name ook een maat voor de spreiding van de datapunten onderling. Hoe groter de standaarddeviatie des te groter is de spreiding tussen de afzonderlijke punten. De standaarddeviatie voor de populatie wordt aangeduid met $$\sigma$$, voor een steekproef noteren we dit met $$s$$.

De variantie, *var*, is direct gerelateerd aan de standaarddeviatie, namelijk de variantie is gelijk aan de standaarddeviatie in het kwadraat. Voor de populatie geldt dus var = $$\sigma^2$$. De variantie van een steekproef noteren we met $$s^2$$.

De variantie en standaarddeviatie van een populatie kunnen worden berekend met de volgende formule:

$$var = \sigma^2 = \displaystyle \frac{1}{N} \sum_{i=1}^{N}(x_i - \mu)^2$$

of in het geval van de steekproef: 

$$s^2 = \frac{1}{n} \sum_{i=1}^{n}(x_i - \bar{x})^2 $$

Let op dat de eenheid van de variantie het kwadraat is van de eenheid van $$x$$. In het geval dat je bijvoorbeeld lengtes van luciferstokjes hebt opgemeten, dan zullen de waardes in cm zijn genoteerd. De variantie heeft dan de eenheid cm$$^2$$. Dat kan soms best onhandig zijn, vandaar dat we vaker de standaarddeviatie gebruiken. De standaarddeviatie heeft altijd dezelfde eenheid als de originele elementen van de dataset. 


### Variatiecoëfficiënt

De variatiecoëfficiënt wordt ook wel de relatieve standaardafwijking genoemd. De coëfficiënt van variatie geeft, net zoals de standaardafwijking en de variantie, een maat voor de spreiding van de populatie of dataset. 

De variatiecoëfficiënt wordt gegeven door de verhouding tussen de standaardafwijking en het gemiddelde.
Voor een populatie is de coëfficiënt van variantie $$c_v$$ dan:

$$c_{v} = \frac{\sigma}{\mu}$$

Met $$\sigma$$ de standaardafwijking van de populatie en $$\mu$$ het populatiegemiddelde.

De steekproef variantie $$\hat{c_v}$$ wordt gegeven door:

$$\hat{c_v} = \frac{s}{\bar{x}}$$

Met $$s$$ de standaardafwijking van de steekproef en $$\bar{x}$$ het steekproef gemiddelde.

Het verschil met de variantie en de standaardafwijking is dat de variatiecoëfficiënt dimensieloos is. Dit is bijvoorbeeld handig als er meerdere datasets vergeleken moeten worden die verschillende eenheden hebben. Ook als de gemiddelde waarden van verschillende datasets erg uiteen liggen is het beter om de variatiecoëfficiënt te gebruiken i.p.v. de standaardafwijking.

Een nadeel van het gebruik van de variatiecoëfficiënt is dat er gedeeld wordt door het gemiddelde. Als dit gemiddelde een heel kleine waarde heeft, dicht bij nul, dan is de variatiecoëfficiënt slecht gedefinieerd.


## Samenvatting


| kenmerk | populatie (*parameter*)| steekproef (*statistiek*) | 
|----|----|----|
| grootte |  $$N$$ | $$n$$ |
| gemiddelde | $$\mu = \frac{1}{N} \sum_i^N x_i$$ | $$\bar{x} = \frac{1}{n} \sum_i^n x_i$$ |
| standaarddeviatie | $$\sigma = \frac{1}{N} \sum_i^N (x_i - \mu)^2$$ | $$s = \frac{1}{n} \sum_i^n (x_i - \bar{x})^2$$ | 
| variantie | $$ var = \sqrt{\sigma} $$ | $$s^2$$ |
|variatiecoëfficiënt | $$c_{v} = \frac{\sigma}{\mu}$$| $$\hat{c_v} = \frac{s}{\bar{x}}$$|


## Voorbeelden

We berekenen de eigenschappen van een aantal datasets als voorbeeld.

> We hebben de volgende dataset van een populatie: $$Y = \{285,-20,31,60,12,53,133\}$$.<br>
> De grootte N = 7. <br>
> Om de mediaan te bepalen sorteren we eerste de datapunten van klein naar groot: -20,12,31,53,60,133,285. Het is een even aantal datapunten en de mediaan ligt tussen 53 en 60 in. Dit komt dan uit op 56.5 .<br>
> De spreidingsbreedte is $$285- -20 = 305$$. <br>
> Het gemiddelde $$\mu_Y = \frac{1}{7}\cdot (285-20+31+60+12+53+133) = 79.1 $$<br>
> De standaarddeviatie is:
>  $$\sigma_Y^2 = \frac{1}{7} \cdot \left[ (285-79.1)^2 + (-20-79.1)^2 + (31-79.1)^2 + (60-79.1)^2 + \right. $$<br> 
> $$ \left. (12-79.1)^2 + (53-79.1)^2 + (133-79.1)^2 \right] = 8997.6 $$ geeft $$\sigma_Y = 94.9$$. <br>
> De variantie $$var_Y$$ = 8997.6.  <br>
> De variatiecoëfficiënt  $$c_{v} = 1.20$$.

Het tweede voorbeeld gaat over een steekproef:

> Stel we hebben een steekproef gedaan van de lengte van eerstejaars studenten. De volgende dataset is hiervoor verzameld: $$ L = \{ 1.90 $$m$$; 1.72 $$m$$; 1.61 $$m$$; 1.84 $$m$$; 1.79 $$m$$ \} $$.  <br>
> De grootte van de steekproef: $$n = 5$$. <br> 
> De spreidingsbreedte is $$1.90$$m-$$1.61$$ m $$= 39$$ cm. 
> De mediaan ligt in het midden van de gesorteerde dataset. Dit is 1.79 m. <br>
> Het gemiddelde $$\bar{L} = 1.77$$ m.<br>
> De variantie is:<br>
>  $$  s^2 = \frac{1}{5} \cdot \left[ (1.90 - 1.77)^2 + (1.72-1.77)^2 + (1.61-1.77)^2 + \right. $$<br>
          $$\left. (1.84-1.77)^2 + (1.79-1.77)^2 \right] = 0.0100 \text{m}^2 $$<br>
> De standaarddeviatie is $$ s = 0.10$$ m. <br>
> De variatiecoëfficiënt is $$\hat{c_v} = 0.0057$$.
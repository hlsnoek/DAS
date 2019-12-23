# Metingen, verdelingen, onzekerheden en significantie

1. Ordered TOC
{:toc}


Als we iets meten is dat meestal omdat we een bepaalde grootheid willen meten. Voorbeelden hiervan zijn 

* Het aantal knikkers in een pot.
* De lengte van een blokje hout. 
* De levensduur van Cesium-131.
* Het aantal sterren in een bolhoop.
* De snelheid van het licht.

We doen ook metingen om bepaalde hypothesis te ontkrachten of juist bevestigen. Maar ook als we een hypothese testen zijn er onderliggende grootheden (vaak meerdere tegelijk) die we meten en vergelijken met voorspelde waardes. 

Het is belangrijk om te begrijpen dat we meestal te maken hebben met een fout op de gemeten grootheid. Hoe groot die fout is kunnen we niet weten, wel kunnen we de meetonzekerheid in kaart proberen te brengen. Die onzekerheid kan grofweg twee oorzaken hebben. Onzekerheden die komen door de meetmethode en onzekerheden met een natuurlijke oorzaak.

##Meetfouten
De eerste oorzaak is dat we een fout maken bij de meting. Een fout betekend hier niet dat we iets verkeerds doen. Het betekend dat we met onze meting een waarde vinden die afwijkt van de echte waarde. Dit noemen we een meetfout. Helaas weten we nooit hoe groot de meetfout is, maar soms kunnen we hem wel inschatten. De meetfout hangt natuurlijk af van de meetmethode. Voorbeelden hiervan zijn: 

* **Het aantal knikkers in een pot.** Stel dat we de pot leegkieperen en we tellen ze allemaal met de hand, dan kan het zo zijn dat we een knikker kwijtraken of een telfout maken. Als we het netjes doen en we doen verschillende hertellingen is de kans groot dat we hierbij geen meetfout maken (zeker als het maar een paar knikkers zijn).


* **De lengte van een blokje hout.** 
Hier zou je bijvoorbeeld een liniaal voor kunnen gebruiken. Allereerst moeten we het blokje netjes langs de lineaal leggen. Zie hieronder een schets van de opstelling. Ligt de 0 wel echt netjes langs de rand?<br>
![](lineaal_v1.png){:width="80%"}<br><br>
Dan moeten we de waarde op de lineaal afmeten. Als we naar de bovenstaande situatie kijken dan zou het blokje 7.6 cm lang kunnen zijn. Maar het is niet helemaal goed af te lezen. Zo zou het blokje ook 7.7 cm lang kunnen zijn als we de linkerkant van het blokje aan de binnenkant van de eerste zwarte streep leggen, en het kan 7.5 cm zijn als we het blokje aan de buitenkant van de eerste zwarte streep leggen. Omdat er geen streepjes tussen de rode streepjes zijn kunnen we slechts op een mm nauwkeurig zeggen wat de lengte is van het blokje. Er is dus sprake van een meetonzekerheid. In dit geval zouden we bijvoorbeeld noteren dat het blokje een lengte heeft van $$7.6 \pm 0.1$$ cm.

* **De levensduur van Cesium-131.** Meestal meten we dit met behulp van een Geiger-Möller telbuis. Bijvoorbeeld we meten het aantal telling in 5 minuten en deze metingen herhalen we een paar keer met een tijdsinterval. Meetfouten komen door de nauwkeurigheid van de twee soorten intervallen, het meetinterval en de tussenliggende periode. Ook zullen er, hopelijk veel kleinere, onzekerheden komen doordat de telbuisen niet altijd precies hetzelfde functioneren.

* **Het aantal sterren in een bolhoop.** Het aantal sterren in een bolhoop kunnen we niet met de hand tellen zoals we met de knikkers in een pot doen. Bolhopen kunnen 100.000 of zelfs wel meer dan een miljoen sterren bevatten. De telling van het aantal sterren in een bolhoop is vaak een combinatie van meerdere methodes, die allemaal hun onnauwkeurigheden kennen.

* **De snelheid van het licht.** De lichtsnelheid kun je op verschillende manieren meten. Maar hoe je het ook meet, je zult zeer nauwkeurige tijds- en lengte metingen nodig hebben. Als je de lichtsnelheid in vacuum wilt bepalen zul je ook nog eens zeer goede conditie van je vacuum nodig hebben òf hiervoor moeten corrigeren. Er zijn vele bronnen van onnauwkeurigheid in dit experiment die je goed zult moeten controleren.

##Onzekerheden met natuurlijk oorzaak

De tweede categorie onzekerheden hebben een andere oorzaak. De grootheid zelf kan ook een spreiding kennen. Je kan hierbij denken aan toevalligheden in een productieproces maar ook door bijvoorbeeld kansprocessen in de quantummechanica. We bekijken nogmaals de voorbeelden.

* **Het aantal knikkers in een pot.** Stel dat de pot een onnemelijk aantal knikkers heeft. Dan wordt het een monnikenwerk om ze allemaal met de hand te tellen. Een goede methode zou dan zijn om de pot te wegen. Als we nu het gewicht van de pot en het gewicht van een knikker weten dan kunnen we uitrekenen hoeveel knikkers er in de pot zitten. Behalve de meetfouten die maken bij de weging kan er ook een onzekerheid komen in de meting van het aantal doordat er een spreiding is knikkergewichten. Niet ieder knikker is precies even zwaar.

* **De lengte van een blokje hout.** Stel dat we de nauwkeurigheid van de lengtemeting helemaal onder controle hebben, dan kan het nog steeds zo zijn dat het blokje zelf niet overal precies dezelfde lengte heeft. Vooral bij houten blokjes zal er zo nu en dan variaties inzitten door nerven en knoesten.

* **De levensduur van Cesium-131.** Kwantum mechanische kansprocessen spelen hier een grote rol. De kans dat een Cesium-131 vervalt binnen een bepaalde tijd is volkomen gedreven door de kwantum-mechanica (anders zouden ze natuurlijk allemaal tegelijk vervallen). Deze onzekerheid resulteert uiteindelijk in variatie in het aantal telling dat je in een van de tijdsintervallen meet. Deze onzekerheid volgt de Poisson statistiek, waar we later meer over zullen lezen.

* **Het aantal sterren in een bolhoop.** Een van de methodes om het aantal sterren te meten in een bolhoop berust op het meten van de dichtheid. Deze dichtheid neemt meestal af over de straal van de bolhoop. In de berekeningen ga je er meestal van uit dat dit homogeen afneemt. Dat wil zeggen dat op een afstand *r* van het centrum van de bolhoop overal dezelfde dichtheid voorkomt. In echt zijn er fluctuaties in de dichtheid. De fluctuaties zorgen uiteindelijk ook voor een onzekerheid in de telling.

* **De snelheid van het licht.** Ook hier spelen toevalsprocessen een rol. Als je opstelling een roterend radartje bevat, dan zijn er hoogstwaarschijnlijk variaties in de tanden van het radartje. Kijk bijvoorbeeld naar het experiment dat [hier](https://en.wikipedia.org/wiki/Fizeau%E2%80%93Foucault_apparatus) beschreven staat.


## Reduceren van meet-onnauwkeurigheden
Goed nadenken van het opzetten van een experiment is belangrijk en kan grote onnauwkeurigheden voorkomen. Nog belangrijker is het om alle onzekerheden goed in kaart te brengen. Alleen zo kun je zien wat de waarde is van een meting. 

Een voorbeeld is een keukeninstallateur die een werkblad voor een keuken moet opleveren. De installateur zal een goede meting moeten doen van de lengte van het werkblad die hij nodig heeft. Als hij een werkblad aanlevert dat uiteindelijk 2 cm te kort is is dat teveel op te vullen met een kitrandje, als hij 3 mm te lang is zal hij ook niet passen. 

Zo werkt het natuurlijk ook bij natuurkundige experimenten. Als je een meting wilt doen zul je eerst goed moeten kijken hoe nauwkeurig het resultaat moet zijn. Wil je een hypothese weerleggen die voorspelt dat een hyperfijn structuur in de spectraallijn van een atoom 1nm vergroot, dan zul je ook de gevoeligheid moeten halen om dat te kunnen meten. 

We onderscheiden meestal **systematische onzekerheid**, **statistische onzekerheid** en **theoretische onzekerheid**. 

Systematische onzekerheden hangen af van de meetopstelling en zijn niet te voorkomen, tenzij we de meetopstelling verbeteren. We kunnen bijvoorbeeld het blokje hout met een schuifmaat meten zo kunnen we de meetonzekerheid verkleinen tot een tiende van een millimeter. We kunnen zorgen dat de tanden van de radartjes heel gelijk zijn, zorgen dat de we de tijdsintervallen heel uniform bepalen en bijvoorbeeld direct aansluiten op de telbuis zodat niet met de hand hoeven te starten of te stoppen.

Statistische onzekerheden zijn reduceerbaar door meer metingen te nemen. Bijvoorbeeld kunnen we tijdens een langer interval het aantal telling meten in het levensduur van Cesium-131 experiment. De relatieve fout op de telling zal dan kleiner worden en daarmee ook de uiteindelijk onzekerheid op de levensduur meting. 

Theoretische onzekerheden kunnen voorkomen als we gebruik maken van aannames met theoretische grondslag. Als we de onzekerheden in deze aannames kunnen kwantificeren hebben we een maat voor de theoretische onzekerheid. Soms kunnen theoretische onzekerheden worden verkleind door bijvoorbeeld meer berekeningen uit te voeren. 


## Verdelingen

Je begrijpt nu dat veel metingen wel herhaalbaar zijn, maar dat je niet altijd precies dezelfde resultaten kunt verwachten. Het gevolg hiervan is dat je een verdeling, of distributie, krijgt van je meetresultaten. 
Van deze verdeling kunnen we bepaalde eigenschappen uitrekenen. Meer hierover kun je vinden onder het kopje [basisbegrippen](link XX).
Het is belangrijk om de verdelingen goed te presenteren, meer daarover kun je [hier](link XX) lezen. 


## Significantie en notatie

Voordat we nu kunnen uitleggen hoe we een meetfout noteren moeten we eerst even stilstaan bij het begrip *significantie*.

De *significantie* is de nauwkeurigheid waarmee een getal/waarde wordt weergegeven. Vaak wordt gedacht dat het aantal decimale cijfers de nauwkeurigheid aangeeft, maar dit is technisch gezien de *precisie* waarmee de (meet)waarde wordt aangegeven. De nauwkeurigheid (significantie) van een getal zegt welke cijfers in het getal er toe doen. Cijfers zonder betekenis tellen we niet mee bij de significantie.

Een aantal voorbeelden:

- Het getal $$7.134$$ heeft in totaal 4 significante cijfers, de precisie is 3.
- Het getal $$0.576$$ heeft 3 significante cijfers, de precisie is ook 3.
- $$0.001$$ heeft 1 significant cijfer, de precisie is 3.
- $$1.001$$ heeft 4 significante cijfers, de precisie is 3.
- $$2.4500$$ heeft 5 significante cijfers, de precisie is 4.

Zo zie je dat de getallen (bijna) allemaal dezelfde precisie hebben, maar een variatie aan significante cijfers. Hier kun je misschien al een patroon in ontdekken. Er zijn namelijk een aantal regels m.b.t. de nullen in een getal bij de significantie:

- Nullen aan de linkerkant doen niet mee met de significantie. Het getal $$0.0056$$ heeft bijvoorbeeld twee significante cijfers.
- Nullen aan de linkerkant voorafgegaan door een getal doen wel mee met de significantie. Het getal $$100.004$$ heeft zes significante cijfers.
- Nullen aan de rechterkant doen wel mee met de significantie. Zo heeft $$10.34000$$ zeven significante cijfers. 
- Een uitzondering op de tweede regel zijn getallen zoals $$300$$, $$4000$$, $$570$$ etc. Deze getallen zijn weergeven zonder decimalen waardoor het onduidelijk is of daadwerkelijk de waarde van $$300$$ respectievelijk $$4000$$ en $$570$$ is gemeten, of dat dit met een hogere of juist lagere precisie is gebeurd. De afspraak is dat als een getal op deze manier wordt weergegeven met nullen rechts, deze nullen niet meedoen met de nauwkeurigheid. De getallen $$300$$ en $$4000$$ hebben bijvoorbeeld allebei een significantie van 1. Het getal $$570$$ heeft twee significante cijfers. Om deze getallen met een ander aantal significante cijfers weer te geven wordt vaak de *wetenschappelijke notatie* gebruikt. Hier komen we later op terug.  

Hieronder nog een aantal voorbeelden die de significantie en precisie illustreren van diverse getallen:

| Getal | Significantie | Precisie |
| --- | --- | --- |
| 1.203 | 4 significante cijfers | 3 decimalen |
| 12.03  | 4 significante cijfers | 2 decimalen |
| 0.0121 | 3 significante cijfers | 4 decimalen |
| 300 | 1 significant cijfer | honderdtallen |
| 300. | 3 significante cijfers | honderdtallen |
| 300.0 | 4 significante cijfers | 1 decimaal |
| 310 | 2 significante cijfers | honderdtallen |
| 0.310 | 3 significante cijfers | 3 decimalen |
| 0.0027 | 2 significante cijfers | 4 decimalen |

Voor het afronden van getallen, na een bewerking, op het juiste aantal significante cijfers zijn er een aantal regels:

- Bij het vermenigvuldigen of delen van getallen krijgt het resultaat de significantie van het oorspronkelijke getal dat de laagste significantie had. 
Vermenigvuldigen we bijvoorbeeld $$2.00$$ (drie significante cijfers) met $$3.5$$ (twee significante cijfers) dan is het 
resultaat gelijk aan $$2.00 \cdot 3.5 = 7.0$$ (twee significante cijfers). 
- Bij het optellen of aftrekken van getallen heeft het resultaat niet meer cijfers achter de decimale punt 
dan het gegeven met het minste aantal cijfers achter de decimale punt. Tellen we bijvoorbeeld $$1.23$$ op bij $$0.1$$ dan is het resultaat 
$$1.23 + 0.1 = 1.3 $$. 


## Wetenschappelijke notatie

Een veel gebruikte manier om getallen en meetresultaten weer te geven is met behulp van de wetenschappelijke notatie. Bij de wetenschappelijke notatie wordt elk getal in de vorm $$a\cdot 10^n$$ opgeschreven. Hierbij is $$1<|a|<10$$ en $$n$$ een geheel getal ongelijk aan nul. 
Een voordeel van deze notatie is dat je hiermee ook hele kleine getallen en hele grote getallen op een makkelijke manier op kunt schrijven. We geven een voorbeeld:

We willen het getal $$0.000000000004563$$ opschrijven met twee significante cijfers. Nu kunnen we natuurlijk $$0.0000000000046$$ opschrijven maar als we dat vaak moeten doen kost dat veel ruimte (en werk). In de wetenschappelijke notatie ziet dit getal met twee significante cijfers er als volgt uit:

$$0.000000000004563 = 4.6\cdot 10^{-12}$$

In het algemeen geldt voor de wetenschappelijke notatie het volgende:

- Je schuift de decimale punt op zodat er een getal staat dat in absolute waarde groter is dan $$1$$ en kleiner dan $$10$$. Dit is het getal $$a$$. 
- Heb je de decimale punt hierbij $$n$$ plaatsen naar links verschoven dan vermenigvuldig je het getal $$a$$ met $$10^n$$. Heb je de decimale punt $$n$$ plaatsen naar rechts verschoven dan vermenigvuldig je $$a$$ met een factor $$10^{-n}$$.
- Daarna rond je af op het gewenste aantal significante cijfers.

Hieronder nog een aantal voorbeelden:

| Getal | Gewenste significantie | Wetenschappelijke notatie |
| --- | --- | --- |
| 0.00343 | 1 significant cijfer | $$3. \cdot 10^{-3}$$ |
| 0.00343 | 2 significante cijfers | $$3.4 \cdot 10^{-3}$$ |
| 0.00343 | 3 significante cijfers | $$3.43 \cdot 10^{-3}$$ |
| 10.7 | 2 significante cijfers | $$1.1 \cdot 10^{1}$$ |
| 255 | 2 significante cijfers | $$2.6 \cdot 10^{2}$$ |
| 34590 | 2 significante cijfers | $$3.5 \cdot 10^{4}$$ |


Tot nu toe hebben we het gehad over losstaande (meet)waarden zonder meetonzekerheden. Hieronder zullen we het begrip meetonzekerheid introduceren en ook de regels m.b.t. significantie en precisie in het geval van een waarde **met meetonzekerheid**.



## Meetonzekerheden noteren
Er zijn verschillende maten waarin een meetonzekerheid wordt aangegeven. Zo is de onzekerheid die we hierboven hebben weergegeven een zogenoemde
*absolute fout*. De absolute fout $$\Delta x$$ is de meetonzekerheid op een waarde $$x$$ zoals deze direct wordt afgelezen op de meetapparatuur. Ook een afronding die plaatsvindt in bijvoorbeeld een
computerprogramma resulteert in een absolute fout. De beste schatting van de waarde noemen we $$x_{best}$$ en de meetwaarde wordt dan aangegeven als:

$$\text{gemeten waarde van }x = x_{best} \pm \Delta x$$

Wat je ook tegen kunt komen is dat de fout tussen haakjes wordt gezet achter de decimalen waar de fout van invloed op is. Hebben we bijvoorbeeld 

$$ 1.456 \pm 0.04$$

dan kunnen we dit ook noteren als:

$$1.456(4)$$

Dit wordt met name vaak gebruikt als een meetwaarde met meetonzekerheid in de wetenschappelijke notatie wordt weergegeven. Het tussen haakjes zetten van de meetonzekerheid is dan namelijk korter dan de notatie met een plusminus. 

We kunnen in de wetenschappelijke notatie bijvoorbeeld $$4.51 \pm 0.27 \cdot 10^3 $$ schrijven. Dit kunnen we ook als $$4.51 \cdot 10^3 \pm 0.27 \cdot 10^3$$ schrijven (minder gebruikelijk). Als we de fout echter tussen haakjes zetten wordt dit een stuk korter en schrijven we:

$$4.51(27) \cdot 10^3$$

Hieronder de verschillende schrijfwijzen naast elkaar gezet in een tabel voor diverse meetwaarden met meetonzekerheden.

| Meetwaarde | Wetensch. not. met $$\pm$$ | Wetensch. not. met haakjes |
| --- | --- | --- |
| $$100.5 \pm 1.8$$  | $$1.005 \pm 0.018 \cdot 10^2$$ | $$1.005(18) \pm 10^2$$ |
| $$0.0045 \pm 0.0006$$  | $$4.5 \pm 0.6 \cdot 10^{-3}$$ | $$4.5(6) \pm 10^{-3}$$ |
| $$300.0 \pm 40$$  | $$3.0 \pm 0.4 \cdot 10^2$$ | $$3.0(4) \pm 10^2$$ |
| $$56934 \pm 160$$  | $$5.693 \pm 0.016 \cdot 10^4$$ | $$5.693(16) \pm 10^4$$ |



De zogenoemde *relatieve fout* van een meetwaarde $$x$$ wordt gegeven door de waarde van de absolute fout gedeeld door de waarde van de grootheid. Omdat we deze waarde  
niet weten wordt er vaak gedeeld door de beste schatting van de gemeten waarde:

$$\text{relatieve fout} = \frac{\Delta x}{x_{best}}$$

De relatieve fout is onder andere handig als er meetwaarden vergeleken moeten worden die in een heel andere orde van grootte zitten.
Zo zouden we bijvoorbeeld de gemeten snelheid van een vliegtuig kunnen vergelijken met de gemeten snelheid van een hardloper.
Stel de gemeten snelheid van een vliegtuig is $$v_{vliegtuig} = 803 \pm 3$$ km/h. De gemeten snelheid van een hardloper is
$$v_{hardloper} = 18.3 \pm 0.2$$ km/h. Welk van de metingen heeft met een grotere precisie plaatsgevonden?

Dit is niet direct uit de absolute fout te zien, maar wel vanuit de relatieve fout. De relatieve fout behorende bij de snelheid van het vliegtuig is 
$$\frac{3}{803} = 0.004$$. De relatieve fout behorende bij de snelheidsmeting van de hardloper is $$\frac{0.2}{18.3} = 0.01$$. Dit betekend dat
de snelheidsmeting van de hardloper met een grotere precisie heeft plaatsgevonden.

Soms werkt een relatieve fout ook juist weer niet. Bijvoorbeeld als je heel nauwkeurig een faseverschil probeert te meten tussen twee golven. Een faseverschil van bijna 0$$^\circ$$ is ook een meting en een relatieve meetfout zegt hierover bijna niets. 


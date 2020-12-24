# Metingen en onzekerheid

1. Ordered TOC
{:toc}

##Fouten en onzekerheden

Als we iets meten is dat meestal omdat we een bepaalde grootheid willen weten. Voorbeelden hiervan zijn 

* Het aantal knikkers in een pot.
* De lengte van een blokje hout. 
* De levensduur van Cesium-131.
* Het aantal sterren in een bolhoop.
* De snelheid van het licht.

We doen ook metingen om bepaalde hypothesis te ontkrachten of juist te bevestigen. Maar ook als we een hypothese testen zijn er onderliggende grootheden (vaak meerdere tegelijk) die we meten en vergelijken met voorspelde waardes. 

Het is belangrijk om te begrijpen dat we meestal te maken hebben met een fout op de gemeten grootheid. **Hoe groot die fout is kunnen we niet weten, wel kunnen we de meetonzekerheid in kaart proberen te brengen.** Die onzekerheid kan grofweg twee oorzaken hebben. Onzekerheden die komen door de meetmethode en onzekerheden met een natuurlijke oorzaak.
Technisch gezien is er dus een verschil tussen de fout en de onzekerheid van de meting. In de praktijk gebruiken we vaak het woord fout ook voor de onzekerheid. Toch is het goed om even stil te staan bij dit verschil.


###Meetfouten
De eerste oorzaak is dat we een fout maken bij de meting. Een fout betekent hier niet dat we iets verkeerds doen. Het betekent dat we met onze meting een waarde vinden die afwijkt van de echte waarde. De afwijking noemen we een meetfout. Helaas weten we nooit hoe groot de meetfout exact is, maar vaak kunnen we hem wel goed inschatten. De meetfout wordt beïnvloedt door de meetmethode. Voorbeelden hiervan zijn: 

* **Het aantal knikkers in een pot.** Stel dat we de pot leeg kieperen en we tellen ze allemaal met de hand, dan kan het zo zijn dat we een knikker kwijtraken of een telfout maken. Als we het netjes doen en we doen verschillende hertellingen is de kans groot dat we hierbij geen meetfout maken (zeker als het maar een paar knikkers zijn).


* **De lengte van een blokje hout.** 
Hier zou je bijvoorbeeld een liniaal voor kunnen gebruiken. Allereerst moeten we het blokje netjes langs de lineaal leggen. Zie hieronder een schets van de opstelling. Ligt de 0 wel echt netjes langs de rand?<br>
![](lineaal_v1.png){:width="80%"}<br>
Dan moeten we de waarde op de lineaal afmeten. Als we naar de bovenstaande situatie kijken dan zou het blokje 7.6 cm lang kunnen zijn. Maar het is niet helemaal goed af te lezen. Zo zou het blokje ook 7.7 cm lang kunnen zijn als we de linkerkant van het blokje aan de binnenkant van de eerste zwarte streep leggen, en het kan 7.5 cm zijn als we het blokje aan de buitenkant van de eerste zwarte streep leggen. Omdat er geen streepjes tussen de rode streepjes zijn kunnen we slechts op een mm nauwkeurig zeggen wat de lengte is van het blokje. Er is dus sprake van een meetonzekerheid. In dit geval zouden we bijvoorbeeld noteren dat het blokje een lengte heeft van $$7.6 \pm 0.1$$ cm.

* **De levensduur van Cesium-131.** Meestal meten we dit met behulp van een Geiger-Müller telbuis. Bijvoorbeeld we meten het aantal telling in 5 minuten en deze metingen herhalen we een paar keer met steeds een even groot tijdsinterval. Meetfouten komen door de nauwkeurigheid van de twee soorten intervallen, het meetinterval en de tussenliggende periode. Ook zullen er, hopelijk veel kleinere, onzekerheden komen doordat de telbuizen niet altijd precies hetzelfde functioneren.

* **Het aantal sterren in een bolhoop.** Het aantal sterren in een bolhoop kunnen we niet met de hand tellen zoals we met de knikkers in een pot doen. Bolhopen kunnen 100.000 of zelfs wel meer dan een miljoen sterren bevatten. De telling van het aantal sterren in een bolhoop is vaak een combinatie van meerdere methodes, die allemaal hun onnauwkeurigheden kennen.

* **De snelheid van het licht.** De lichtsnelheid kun je op verschillende manieren meten. Maar hoe je het ook meet, je zult zeer nauwkeurige tijds- en lengte metingen nodig hebben. Als je de lichtsnelheid in vacuum wilt bepalen zul je ook nog eens zeer goede conditie van je vacuum nodig hebben òf hiervoor moeten corrigeren. Er zijn vele bronnen van onnauwkeurigheid in dit experiment die je goed zult moeten controleren.

###Onzekerheden met natuurlijke oorzaak

De tweede categorie onzekerheden hebben een andere oorzaak. De grootheid zelf kan ook een spreiding kennen. Je kan hierbij denken aan toevalligheden in een productieproces maar ook door bijvoorbeeld kansprocessen in de kwantummechanica. We bekijken nogmaals de voorbeelden.

* **Het aantal knikkers in een pot.** Stel dat de pot een onneembaar aantal knikkers heeft. Dan wordt het een monnikenwerk om ze allemaal met de hand te tellen. Een goede methode zou dan zijn om de pot te wegen. Als we nu het gewicht van de pot en het gewicht van een knikker weten dan kunnen we uitrekenen hoeveel knikkers er in de pot zitten. Behalve de meetfouten die we maken bij de weging kan er ook een onzekerheid komen in de meting van het aantal, doordat er een spreiding is in knikker gewichten. Niet iedere knikker is precies even zwaar.

* **De lengte van een blokje hout.** Stel dat we de nauwkeurigheid van de lengtemeting helemaal onder controle hebben, dan kan het nog steeds zo zijn dat het blokje zelf niet overal precies dezelfde lengte heeft. Vooral bij houten blokjes zal er zo nu en dan variatie in zitten door nerven en knoesten.

* **De levensduur van Cesium-131.** Kwantum mechanische kansprocessen spelen hier een grote rol. De kans dat een Cesium-131 vervalt binnen een bepaalde tijd is volkomen gedreven door de kwantum-mechanica (anders zouden ze natuurlijk allemaal tegelijk vervallen). Deze onzekerheid resulteert uiteindelijk in een variatie in het aantal tellingen dat je in een van de tijdsintervallen meet. Deze onzekerheid volgt de Poisson statistiek, waar we later meer over zullen lezen.

* **Het aantal sterren in een bolhoop.** Een van de methodes om het aantal sterren te meten in een bolhoop berust op het meten van de dichtheid. Deze dichtheid neemt meestal af over de straal van de bolhoop. In de berekeningen ga je er meestal van uit dat dit homogeen afneemt. Dat wil zeggen dat op een afstand *r* van het centrum van de bolhoop overal dezelfde dichtheid voorkomt. In het echt zijn er fluctuaties in de dichtheid. De fluctuaties zorgen uiteindelijk ook voor een onzekerheid in de telling.

* **De snelheid van het licht.** Ook hier spelen kansprocessen een rol. Als je opstelling een roterend radartje bevat, dan zijn er hoogstwaarschijnlijk variaties in de tanden van het radartje. Kijk bijvoorbeeld naar het experiment dat [hier](https://en.wikipedia.org/wiki/Fizeau%E2%80%93Foucault_apparatus) beschreven staat.


### Reduceren van meet-onnauwkeurigheden
Goed nadenken over de opzet van een experiment is belangrijk en kan grote onnauwkeurigheden voorkomen. Nog belangrijker is het om alle onzekerheden goed in kaart te brengen. Alleen zo kun je inschatten wat de waarde is van een meting. 

Een voorbeeld is een keukeninstallateur die een werkblad voor een keuken moet opleveren. De installateur zal een goede meting moeten doen van de lengte van het werkblad die hij nodig heeft. Als hij een werkblad aanlevert dat uiteindelijk 2 cm te kort is past het blad niet, dit is niet meer op te vullen met een kit randje. Als het keukenblad 3 mm te lang is zal het natuurlijk ook niet passen.

Zo werkt het ook bij natuur- en sterrenkundige experimenten. Als je een meting wilt doen zul je eerst goed moeten kijken hoe nauwkeurig het resultaat moet zijn. Wil je een hypothese weerleggen die voorspelt dat een hyperfijnstructuur in de spectraallijn van een atoom 1 nm vergroot, dan zul je ook de nauwkeurigheid moeten bereiken om dat te kunnen meten. 

We onderscheiden **systematische onzekerheid**, **statistische onzekerheid** en **theoretische onzekerheid**. 

**Systematische onzekerheden** hangen af van de meetopstelling en zijn niet te voorkomen. We kunnen hem soms wel reduceren door de meetopstelling te verbeteren. Een enkele bron van een systematische fout is eenzijdig, dat wil zeggen dat de gemeten waarde consequent te hoog of te laag uitvalt door bijvoorbeeld calibratie fouten van de meetinstrumenten. Vaak zijn er in een experiment combinaties van systematische onzekerheden waardoor de gemeten waarde zowel te hoog als te laag kan uitvallen. 
Systematische onzekerheden zijn lastig te vinden in opstellingen en zijn vooral te voorkomen door kritisch te kijken en na te denken over de meetopstelling. Een systematische fout kunnen we bijvoorbeeld verbeteren door het blokje hout uit het voorbeeld met een schuifmaat te meten, zo kunnen we de meetonzekerheid verkleinen tot een tiende van een millimeter. We kunnen zorgen dat de tanden van de radartjes uit het voorbeeld van de meting van de lichtsnelheid heel gelijk zijn. 

**Statistische onzekerheden** zijn reduceerbaar door het experiment te herhalen. Bijvoorbeeld kunnen we tijdens een langer interval het aantal tellingen meten in het levensduur van Cesium-131 experiment. Ook kunnen we meer meetpunten verzamelen. De relatieve fout op de telling zal dan kleiner worden en daarmee ook de uiteindelijk onzekerheid op de levensduur meting. 

**Theoretische onzekerheden** kunnen voorkomen als we gebruik maken van aannames met theoretische grondslag. Als we de onzekerheden in deze aannames kunnen kwantificeren hebben we een maat voor de theoretische onzekerheid. Soms kunnen theoretische onzekerheden worden verkleind door bijvoorbeeld meer berekeningen uit te voeren. 


### Verdelingen

Je begrijpt nu dat veel metingen wel herhaalbaar zijn, maar dat je niet altijd precies dezelfde resultaten kunt verwachten. Het gevolg hiervan is dat je een verdeling of distributie krijgt van je meetresultaten. 
Van deze verdeling kunnen we bepaalde eigenschappen uitrekenen. Meer hierover kun je vinden onder het kopje [basisbegrippen](/module-1/basisbegrippen).
Het is belangrijk om de verdelingen goed te presenteren, meer daarover kun je [hier](/module-1/data-visualiseren) lezen. 



### Meetonzekerheden noteren

We kunnen de meetonzekerheden op verschillende manieren noteren. 

Het meetresultaat zelf noemen we de **centrale waarde** en de meetonzekerheid heet ook wel de **absolute fout**. We noteren dit als volgt: 

$$\text{gemeten waarde van }x = x_{\text{centraa}} \pm \Delta x$$.

Waarbij $$\Delta x$$ de meetonzekerheid is. 

Wat je ook tegen kunt komen is dat de fout tussen haakjes wordt gezet achter de decimalen waar de fout van invloed op is. Hebben we bijvoorbeeld 

$$ 1.456 \pm 0.004$$

dan kunnen we dit ook noteren als:

$$1.456(4)$$

Dit wordt met name vaak gebruikt als een meetwaarde met meetonzekerheid in de wetenschappelijke notatie wordt weergegeven. Het tussen haakjes zetten van de meetonzekerheid is dan namelijk korter dan de notatie met een plusminus. 

We kunnen in de wetenschappelijke notatie bijvoorbeeld $$(4.51 \pm 0.27) \cdot 10^3 $$ schrijven. Dit kunnen we ook als $$4.51 \cdot 10^3 \pm 0.27 \cdot 10^3$$ schrijven (minder gebruikelijk). Als we de fout echter tussen haakjes zetten wordt dit een stuk korter en schrijven we:

$$4.51(27) \cdot 10^3$$

Hieronder de verschillende schrijfwijzen naast elkaar gezet in een tabel voor diverse meetwaarden met meetonzekerheden.

| Meetwaarde | Wetensch. not. met $$\pm$$ | Wetensch. not. met haakjes |
| --- | --- | --- |
| $$100.5 \pm 1.8$$  | $$(1.005 \pm 0.018) \cdot 10^2$$ | $$1.005(18) \pm 10^2$$ |
| $$0.0045 \pm 0.0006$$  | $$(4.5 \pm 0.6) \cdot 10^{-3}$$ | $$4.5(6) \pm 10^{-3}$$ |
| $$300.0 \pm 40$$  | $$(3.0 \pm 0.4) \cdot 10^2$$ | $$3.0(4) \pm 10^2$$ |
| $$56934 \pm 160$$  | $$(5.693 \pm 0.016) \cdot 10^4$$ | $$5.693(16) \pm 10^4$$ |


Soms is het nuttig om de **relatieve fout** te gebruiken. Deze wordt gegeven door de waarde van de absolute fout te delen door de centrale waarde. 

$$\text{relatieve fout} = \frac{\Delta x}{x_{\text{centraal}}}$$

De relatieve fout is onder andere handig als er meetwaarden vergeleken moeten worden die in een heel andere orde van grootte zitten.
Zo zouden we bijvoorbeeld de gemeten snelheid van een vliegtuig kunnen vergelijken met de gemeten snelheid van een hardloper.
Stel de gemeten snelheid van een vliegtuig is $$v_{vliegtuig} = 803 \pm 3$$ km/h. De gemeten snelheid van een hardloper is
$$v_{hardloper} = 18.3 \pm 0.2$$ km/h. Welk van de metingen heeft met een grotere precisie plaatsgevonden?

Dit is niet direct uit de absolute fout te zien, maar wel vanuit de relatieve fout. De relatieve fout behorende bij de snelheid van het vliegtuig is 
$$\frac{3}{803} = 0.004$$. De relatieve fout behorende bij de snelheidsmeting van de hardloper is $$\frac{0.2}{18.3} = 0.01$$. Dit betekent dat
de snelheidsmeting van de hardloper met een grotere precisie heeft plaatsgevonden.

Soms werkt een relatieve fout ook juist weer niet. Bijvoorbeeld als je heel nauwkeurig een faseverschil probeert te meten tussen twee golven. Een faseverschil van bijna 0$$^\circ$$ is ook een meting en een relatieve meetfout zegt hierover bijna niets. 


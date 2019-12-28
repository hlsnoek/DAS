## Foutenpropagatie

Vaak kunnen we de grootheid die we willen weten niet direct meten, maar meten we observabelen die zich, via een bepaalde functie, verhouden tot de grootheid. Of zelfs meten we twee of meer variabelen die we nodig hebben om de gewilde grootheid te bepalen. 

Bijvoorbeeld als we een gemiddelde snelheid van een auto willen bepalen. Dit zouden we kunnen doen door de tijd te meten die de auto nodig heeft om een bepaald traject af te leggen. We meten dan de tijd en de lengte en die zetten we dan om in snelheid via de bekende formule $$v=\Delta l/\Delta t$$. 

Of we bepalen de massa van een elementair deeltje (in rust) en willen dit omzetten naar de energie van het deeltje via de formule $$E=mc^2$$. 

Als we de onzekerheid weten op de gemeten observabelen dan willen we deze propagaren naar de grootheid die we eigenlijk willen bepalen. Dit noemen we het propageren van fouten. Voor het propageren van fouten zijn regels die je kunt volgen. In dit hoofdstuk leren we je de basisregels voor het propageren van **ongecorreleerde** fouten. Dat wil zeggen dat als er meerder onzekerheden worden gepropageerd deze onafhankelijk zijn. Later zullen we nog de regel voor gecorreleerde fouten geven. 


### Basisregel
We beginnen met de algemene regel voor het propageren van ongecorreleerde fouten. Daarna zullen we laten zien hoe deze regel eruit ziet voor eenvoudige relaties. Deze zou je apart kunnen leren, maar je kunt ook altijd de basisregel gebruiken. Het resultaat behoort hetzelfde te zijn. 
We noteren de onzekerheid in dit hoofdstuk met $$\Delta x$$ waar we eerder ook wel $$\sigma_x$$ hebben gezien. 

Als $$q = q(x,y,z,\dots)$$ een functie is met meerdere ongecorreleerde variabelen, dan wordt de onzekerheid op $$q$$ gegeven door:

$$\Delta q = \sqrt{\left(\frac{\delta q}{\delta x}\Delta x  \right)^2+\left(\frac{\delta q}{\delta y}\Delta y\right)^2+\left(\frac{\delta q}{\delta z}\Delta z\right)^2+\dots}$$

Hierbij zijn $$\frac{\delta q}{\delta x}$$, $$\frac{\delta q}{\delta y}$$ etc. de partiële afgeleiden van $$q$$ naar de betreffende variabele.

Deze algemene regel kan eenvoudig worden uitgeschreven naar de 


----



Hieronder staat hoe de fouten propageren in het geval van het optellen, aftrekken, delen en vermenigvuldigen van gemeten waarden.
Hierbij wordt ervan uitgegaan dat de meetwaarden (en fouten) onafhankelijk zijn van elkaar.

Bij een telexperiment met $$N$$ 'counts' wordt de meetfout gegeven door 

$$\sqrt{N}$$

Als $$q = x + y + \dots$$ of $$q = x - y - \dots$$ dan:

$$\Delta q = \sqrt{\left(\Delta x\right)^2+\left(\Delta y\right)^2+\dots}$$

Als $$q = x\cdot y\cdot \cdot u \ cdot w \cdot \dots$$ of $$q = \frac{x\cdot u \cdot \dots}{y \cdot w \cdot \dots}$$ dan: 

$$\frac{\Delta q}{|q|} = \sqrt{\left(\frac{\Delta x}{x}\right)^2+\left(\frac{\Delta y}{y}\right)^2+\left(\frac{\Delta u}{u}\right)^2+\left(\frac{\Delta w}{w}\right)^2} $$

Als $$q$$ een exact veelvoud $$c$$ is van de gemeten data, dus $$q = c \cdot x$$, dan:

$$\Delta q = |c|x$$ 

Daarnaast is de relatieve fout in $$q$$ dan gelijk aan de relatieve fout in $$x$$.

Als $$q=x^n$$ dan:

$$\frac{\Delta q}{|q|} = |n| \frac{\Delta x}{|x|}$$

Als $$q=q(x)$$ een functie van $$x$$ is dan:

$$\Delta q = \left|\frac{dq}{dx}\right|\Delta x$$

Hierbij is $$\frac{dq}{dx}$$ de afgeleide van de functie naar $$x$$.



Met bovenstaande rekenregels kan de propagatie van fouten bepaald worden. 

### Afronding meetonzekerheden en meetwaarden bij foutenpropagatie

Voor het afronden van meetonzekerheden op het juiste aantal significante cijfers geldt het volgende:

- Is de meetonzekerheid kleiner dan $$3\cdot 10^n$$ met $$n\,\varepsilon\, \mathbb{Z}$$ dan wordt de meetonzekerheid afgerond op twee significante cijfers. Zo wordt de meetonzekerheid 
$$0.12367$$ afgerond op twee decimalen tot $$0.12$$. Is de meetonzekerheid gelijk aan 23.4 dan wordt dit afgerond op $$23$$.
- Is de meetonzekerheid groter of gelijk aan $$3\cdot 10^n$$ met $$n\,\varepsilon\, \mathbb{Z}$$ dan wordt  
de meetonzekerheid afgerond op één significant cijfer. Zo wordt de meetonzekerheid $$0.6321$$ bijvoorbeeld afgerond tot $$0.6$$.  

Bij foutenpropagatie bepaald de afronding van de doorberekende (absolute) fout op hoeveel decimalen het doorberekende resultaat wordt afgerond. De **significantie** van de meetonzekerheid bepaald dus de **precisie** waarmee de meetwaarde wordt weergegeven. 
Is het doorberekende resultaat (onafgerond) bijvoorbeeld $$8.956$$ en de doorberekende (onafgeronde) absolute fout is $$0.68$$ dan wordt de absolute fout afgerond tot $$0.7$$ volgens bovenstaande regels. Dit betekent dan ook dat het doorberekende resultaat wordt afgerond tot een getal met één decimaal, namelijk $$9.0$$. De doorberekende waarde met bijbehorende fout wordt dan weergegeven als $$9.0 \pm 0.7$$ of als $$9.0(7)$$.

Stel we hebben als (onafgeronde) doorberekende waarde bijvoorbeeld $$45.326$$, met de bijbehorende absolute fout $$0.123$$. Omdat de absolute fout volgens bovenstaande regels wordt afgerond op twee decimalen, noteren dit resultaat dan als $$45.33 \pm 0.12$$. 


**Voorbeeld foutenpropagatie en afronding**

Stel dat we de lengte van het blokje hebben gemeten en we lezen de volgende waarde af:

- De $$\text{lengte = l} = 7.6 \pm 0.1 \text{ cm}$$
- De $$\text{breedte = b} = 4.1 \pm 0.2 \text{ cm}$$ 
- De $$\text{hoogte = h} = 2.0 \pm 0.2 \text{ cm}$$ 

Het volume van het blokje wordt gegeven door:

$$V = l\cdot b\cdot h = 7.6 \cdot 4.1 \cdot 2.0 = 62.32 \approx 62.3 \text{ cm}^3$$

We gebruiken de regel dat als $$q = x\cdot y\cdot \dots$$ dan: 

$$\frac{\Delta q}{|q|} = \sqrt{\left(\frac{\Delta x}{x}\right)^2+\left(\frac{\Delta y}{y}\right)^2+\left(\frac{\Delta u}{u}\right)^2+\left(\frac{\Delta w}{w}\right)^2} $$

Dus:

$$\begin{aligned}\frac{\Delta V}{|V|} &= \sqrt{\left(\frac{\Delta l}{l}\right)^2+\left(\frac{\Delta b}{b}\right)^2+\left(\frac{\Delta h}{h}\right)^2} \\ 
&= \sqrt{\left(\frac{0.1}{7.6}\right)^2+\left(\frac{0.2}{4.1}\right)^2+\left(\frac{0.2}{2.0}\right)^2}\\
&= 0.01255 \dots
\end{aligned}$$

We ronden dit nog niet af, dat doen we pas als we de absolute fout hebben:

$$\begin{aligned} \Delta V &= \frac{\Delta V}{|V|} \cdot |V| \\
&= 0.01255\dots \cdot 62.32 \\
&= 0.78228 \dots \\
&\approx 0.8\end{aligned}$$

Het gemeten volume van het blokje is dus $$V = 62.3 \pm 0.8 \text{ cm}^3$$

### Foutenpropagatie bij herhaalde metingen

Zoals eerder gezegd weten we de echte exacte waarde van en grootheid nooit. Wel kunnen we deze zo goed mogelijk 
benaderen. Als een meting herhaald wordt dan krijgen we een steeds betere schatting van de waarde, maar we zullen de waarde zelf nooit
helemaal precies weten. In het geval van het blokje zou de lengte bijvoorbeeld door jouzelf en al je medestudenten gemeten kunnen worden. Iedereen leest de waarde op de liniaal
net wat anders af en daardoor verkrijgen we een collectie van meetwaarden, elk met een eigen meetonzekerheid.

Ook hierbij kan voor de foutenpropagatie de absolute fout genomen worden om tot een 
waarde met meetonzekerheid te komen. De absolute fout geeft echter een te grote waarde van de meetonzekerheid. 
Daarom wordt er bij herhaaldelijke metingen vaak gebruik gemaakt van de *standaardafwijking* als fout op de waarde. 
In de eerdere lesstof onder ['Basisbegrippen'](/blok-1/theorie-basisbegrippen) hebben we het al over de standaardafwijking gehad.
Bij de lengte van het blokje zouden we dan de gemiddelde meetwaarde bepalen en hier de standaardafwijking als meetfout bij optellen/aftrekken:

$$\text{lengte l} = l_{gemiddeld} \pm \sigma_{lengte}$$

De eerdere formules voor de foutenpropagatie zijn ook van toepassing op meetwaarden met de standaardafwijking als meetfout. Hierbij vul je de standaardafwijking in op de plekken waar de absolute fout staat.


 

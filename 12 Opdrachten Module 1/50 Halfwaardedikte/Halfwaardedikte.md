## M1.E - Halfwaardedikte I *


We voeren een experiment uit waarbij de halfwaardedikte van lood wordt bepaald bij een bepaalde gamma-bron. De bron produceert gamma straling met een onbekende, maar stabiele energie. De halfwaardedikte is precies de energie die je nodig hebt om de intensiteit van de bron te halveren. Dit is belangrijk om te weten als je bijvoorbeeld ziekenhuispersoneel wil beschermen tegen straling die bij het maken van een röntgenfoto vrijkomt.


We hebben een opstelling gemaakt waarmee we steeds per tijdsinterval van 2 minuten de hoeveelheid straling meten met een Geiger-Müller telbuis. In de opstelling kunnen we plakken lood tussen de bron en de telbuis plaatsen. De plakken lood hebben een dikte van 0.3 cm. Als we twee loodplakken plaatsen is de totale dikte dus in totaal 0.6 cm lood. De afstand tussen de bron en de telbuis is constant. De achtergrondstraling is te verwaarlozen in dit experiment, net als de onzekerheid op de dikte van de loodplakken. 

<!--XX als het nog lukt een plaatje maken-->

> Wat voor soort fout zit er op de telling van de Geiger-Müller telbuis? Beredeneer waarom dit is.

De intensiteit van de $$\gamma$$-bron, $$I(d)$$, hangt af van de dikte lood (in cm) die tussen de bron en de telbuis is geplaatst. Deze volgt de volgende vergelijking:


$$I(d) = I_0 \times \left( \frac{1}{2} \right) ^{d/d_{half}}$$

Hierbij is de intensiteit $$I$$ gelijk aan het aantal counts per seconde: 

$$I = \frac{N}{\Delta T}$$


We gaan het experiment nu simuleren. Download het bestand [M1.E_Halfwaardedikte.py](M1.E_Halfwaardedikte.py) en zorg dat deze in dezelfde folder staat als *DAS_DatasetGenerator.py*. Download ook het inlever template: [Inlevertemplate](InlevertemplateBlok1b.docx)

De volgende regel maakt de dataset aan: 

	counts,diktes = ds.DataSetHalfwaardeDikte()

Deze lijsten bevatten de meetwaardes (in counts) en de diktes lood die tussen de bron en de telbuis zijn geplaatst. We gaan eerst de distributie met foutenvlaggen plotten. <br>

> * Maak eerst een gewoon grafiek met de datapunten. Kijk eventueel in de code van opgave M1.D hoe je een grafiek moet maken. <br>
> * Maak nu een lijst aan met voor elk punt de fout op de gemeten aantal counts. Je kan nu met de volgende code de foutenvlaggen plotten.
>
>         plt.errorbar(diktes,counts, yerr=fouten, fmt = 'o', label='"data"')
>
> * Plaats de grafiek op je inlever document (gebruik het template). Is hij helemaal goed leesbaar?

We gaan nu de halfwaardedikte bepalen met de volgende methode. We kijken eerst naar het punt $$N_0$$ dus het aantal counts als er geen loodplakken zijn geplaatst. Nu zoeken we het eerste dikte, $$d$$, in de grafiek waarvoor geldt dat $$N\leq 0.5 \times N_0$$.

>  Bepaal nu met deze methode de halfwaardedikte (in cm). Dit is natuurlijk makkelijk met de hand te doen maar programmeer het ook, dat hebben we in een latere opdracht nog nodig.

Beantwoord nu de volgende vragen:

>  * Hoe groot denk je dat de onzekerheid (standaard deviatie) is op de bepaalde halfwaardedikte? Maak een inschatting. <br>
>  * Wat voor soort kansdistributie zou de onzekerheid op de halfwaardedikte beschrijven? <br>
>  * Is de methode om de halfwaardedikte te meten zuiver (Engels: unbiased), dat wil zeggen vind je niet steeds juist een te hoge of te lage waarde? Zo nee, waarom denk dat je dat dit niet zo is. Zo ja, kun je een manier bedenken om de onzuiverheid te verminderen? <br>
>  * Stel dat de halfwaardedikte veel kleiner is dan de waarde die je nu gevonden hebt. Zou dit experiment dan nog hebben gewerkt? Wanneer wordt dit een probleem? <br>
>  * Hoe zou je dit experiment willen verbeteren. Dit kunnen verbeteringen zijn aan de kant van de opstelling maar ook aan de kant van de data analyse. <br>
>  * Iemand suggereert dat het experiment ook wel sneller kan worden uitgevoerd door in plaats van 2 minuten, steed 1 minuut per keer te meten met de Geiger-Müller telbuis. Dat scheelt een hoop meettijd. Is dit een goed idee? <br>




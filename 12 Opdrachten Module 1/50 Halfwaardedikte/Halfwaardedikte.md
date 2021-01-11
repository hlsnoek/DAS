## M1.5 - Halfwaardedikte I *

<!--voor 2022: In het nakijkmodel bij 5e voeg het antwoord toe: Je hebt er goed over nagedacht, maar het antwoord is toch fout.-->

We voeren een experiment uit waarbij de halfwaardedikte van lood wordt bepaald voor een bepaalde gamma-bron. De bron produceert gamma straling met een onbekende energie. Een halfwaardedikte is gedefinieerd als precies de energie die je nodig hebt om de intensiteit van de bron te halveren. Dit is een belangrijke grootheid om te weten als je bijvoorbeeld ziekenhuispersoneel wil beschermen tegen straling die bij het maken van een röntgenfoto vrijkomt.


We hebben een opstelling gemaakt waarmee we steeds per tijdsinterval van 2 minuten de hoeveelheid straling meten met een Geiger-Müller telbuis. In de opstelling kunnen we plakken lood tussen de bron en de telbuis plaatsen. De plakken lood hebben een dikte van 0.3 cm. Als we twee loodplakken plaatsen is de totale dikte dus in totaal 0.6 cm lood. De afstand tussen de bron en de telbuis is constant. De achtergrondstraling is te verwaarlozen in dit experiment, net als de onzekerheid op de dikte van de loodplakken. 

<!--XX als het nog lukt een plaatje maken-->

> - **M1.5a) Welke kansverdeling volgt de onzekerheid op de telling van de Geiger-Müller telbuis? Als we bijvoorbeeld N counts hebben gemeten, hoe groot is dan de onzekerheid op de centrale waarde N? Beredeneer je antwoord.**

De intensiteit van de $$\gamma$$-bron, $$I(d)$$, hangt af van de dikte lood (in cm) die tussen de bron en de telbuis is geplaatst. Deze volgt de volgende vergelijking:


$$I(d) = I_0 \times \left( \frac{1}{2} \right) ^{d/d_{half}}$$

Hierbij is de intensiteit $$I$$ gelijk aan het aantal counts per seconde: 

$$I = \frac{N}{\Delta T}$$

We gaan het experiment nu simuleren. Download het bestand [M1.5_Halfwaardedikte.py](M1.5_Halfwaardedikte.py) en zorg dat deze in dezelfde folder staat als het `DAS_DatasetGenerator.py` bestand. 

De volgende regel in de code maakt de dataset aan: 

	counts,diktes = ds.DataSetHalfwaardeDikte()

Deze lijsten bevatten de meetwaardes (in counts) en de diktes lood (in cm) die tussen de bron en de telbuis zijn geplaatst. We gaan eerst de meetwaardes met foutenvlaggen in een grafiek plotten.

> Voor het plotten maak je een lijst aan met voor elk punt de onzekerheden op de gemeten aantal counts. De onzekerheden moet je dus zelf berekenen. 
 
Je kan nu met de volgende code de foutenvlaggen plotten.

         plt.errorbar(diktes,counts, yerr=fouten, fmt = 'o', label='"data"')

> - **M1.5b) Maak de grafiek met meetwaardes en foutenvlaggen. Let goed op de leesbaarheid van de grafiek, gebruik hiervoor de richtlijnen.**

We gaan nu de halfwaardedikte bepalen met de volgende methode. We kijken eerst naar het punt $$N_0$$ dus het aantal counts als er geen loodplakken zijn geplaatst. Nu zoeken we de eerste dikte, $$d$$, in de grafiek waarvoor geldt dat $$N\leq 0.5 \times N_0$$.

> - **M1.5c) Bepaal nu met de hierboven beschreven methode de halfwaardedikte (in cm). Dit is natuurlijk makkelijk met de hand te doen maar programmeer het ook, dat hebben we in een latere opdracht nog nodig.**

Beantwoord nu de volgende vragen:

> - **M1.5d) Hoe groot denk je dat de onzekerheid is op de bepaalde halfwaardedikte? Probeer dit te kwantificeren, schrijf niet alleen de geschatte waarde op maar leg ook uit hoe je tot die waarde bent gekomen.**<br><br>
>
> - **M1.5e) Wat voor soort kans distributie zou de onzekerheid op de halfwaardedikte beschrijven? Leg uit hoe je tot je antwoord komt en als je het niet weet, beredeneer dan waarom je het niet weet.**<br><br>
> 
> - **M1.5f) Is de methode om de halfwaardedikte te meten zuiver (Engels: unbiased), dat wil zeggen vind je niet steeds juist een te hoge of te lage waarde? Zo nee, waarom denk dat je dat dit niet zo is. Zo ja, kun je een manier bedenken om de onzuiverheid te verminderen?**<br><br>
>
> - **M1.5g) Stel dat de halfwaardedikte veel kleiner is dan de waarde die je nu gevonden hebt. Zou dit experiment dan nog hebben gewerkt? Wanneer wordt dit een probleem, kwantificeer je antwoord?**<br><br>
> 
> - **M1.5h) Hoe zou je dit experiment willen verbeteren. Dit kunnen verbeteringen zijn aan de kant van de opstelling maar ook aan de kant van de data analyse. Noem een verbetering voor de opstelling en een voor de data analyse.**<br><br>


Je hebt nu alle opdrachten van module 1 afgerond. Sla het ingevulde template nu op als pdf en lever deze samen met de 5 python scriptjes in. Kijk nog eens bij de [informatie](/informatie/inleveropdrachten) over de inleveropdrachten voor de link naar ANS en de deadlines.

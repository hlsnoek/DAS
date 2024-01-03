# Data visualiseren
<!--REF\label{/module-1/data-visualiseren}-->
1. Ordered TOC
{:toc}


Meetgegevens die je hebt verzameld kun je vaak ook visueel presenteren. Visualisatie is een heel krachtig middel. 

In dit deel bekijken we de verschillende manieren om data visueel te presenteren. Aan bod komen grafieken en scatterplots, staafdiagrammen en histogrammen. 
We laten ook zien hoe je deze met behulp van python kan maken.

Als je data visualiseert dan is het natuurlijk de bedoeling dat iemand anders deze makkelijk en goed kan interpreteren. Er zijn bepaalde richtlijnen voor het maken van goede, inzichtelijke plots. 

De **richtlijnen zijn geen regels**. Er zijn altijd uitzonderlijke datasets die erom vragen om af te wijken van de richtlijnen. Blijf dus altijd goed nadenken over **wat** je doet en **waarom**. 

Afhankelijk van wat voor soort metingen je hebt genomen kies je uit een grafiek, een scatterplot, een staafdiagram of een histogram. Elk van deze data visualisatie methodes worden hieronder besproken. 

## Grafieken & Scatterplots

Grafieken en scatterplots zijn twee vormen van een diagram die veel op elkaar lijken. 
Bij beide vormen geef je datapunten weer die steeds twee waardes kennen, bijvoorbeeld de massa en lengte. Scatterplots gebruik je voor een waarde van de ene grootheid meerdere waardes voor kunnen komen van de andere grootheid. In het voorbeeld van lengte en massa zouden er bijvoorbeeld voor een gegeven massa meerdere waardes van de lengte kunnen voorkomen. Grafieken gebruik je als er maar één waarde voor een gegeven massa voorkomt.

Bij **grafieken** verwacht je vaak een bepaalde relatie tussen de gemeten waardes. Op de horizontale as zet je de ingestelde of gekozen waarde, op de verticale as de gemeten waarde. Bijvoorbeeld als je te temperatuur meet op verschillende tijdstippen van de dag dan komt de tijd op de horizontale as en de temperatuur op de verticale as. 
De punten in een grafiek mag je eventueel met een lijn verbinden. Maar let goed op, soms wordt het er niet duidelijker van. 

> **Voorbeeld van een grafiek**
> Bij verschillende weerstations meten we over een periode van een maand de temperatuur op een vast tijdstip op de dag. De meetgegeven geven we weer in een grafiek. Op de horizontale as zetten we de tijd en op de verticale as de gemeten temperatuur. De meetwaardes van de verschillende meetstations geven we weer met verschillende kleuren en om de grafiek duidelijker leesbaar te maken verbinden we de punten met een lijn. De legenda geeft duidelijk weer welke kleur bij welk meetstation hoort.
> ![Plot met verschillende weerstations.](plot5_grafieken_aslabel_lim.png){:width="100%"}<br>

Bij **scatterplots** kan er wel een relatie bestaan tussen de twee grootheden maar er zit geen volgorde in de datapunten. Hierom verbindt je de punten in een scatterplot *nooit*. 

> **Voorbeeld van een scatterplot**
> Van een bolhoop meten van een deel van de sterren zowel de oppervlakte temperatuur ($$T_{eff}$$) als de lichtkracht ($$M_v$$). De datapunten geven we weer in een scatterplot.
> 
> ![Hertzsprung-Russel diagram van bolhoop M55.](HRScatter.jpg){:width="40%"}<br>
> (Bron: Astronomy picture of the day)

Voor het weergeven van grafieken en scatterplots in wetenschappelijke rapporten gelden een aantal richtlijnen die we hieronder samenvatten en kort uitleggen. 

###Richtlijnen opmaak grafieken en scatterplots
- Een grafiek van een dataset wordt geplot met punten en eventueel lijnen die de datapunten verbinden. Een scatterplot alleen met punten en nooit met een lijn.
- Bij een enkele dataset wordt geen legenda gebruikt. Als er meerdere datasets in één grafiek worden weergegeven dan is een legenda noodzakelijk.
- Aslabels geven weer wat elke as representeert (inclusief eenheden!).
- Assen beginnen zo mogelijk bij de oorsprong. Een uitzondering kan zijn als de data heel erg ver van de oorsprong af zit of als er bijvoorbeeld ook negatieve waardes voorkomen.
- Op de assen vindt je maatstreepjes die de waardes op de as markeren. Er bestaan grote en kleine maatstreepjes. Een as begint en eindigt op een groot maatstreepje met een waarde en niet op een klein maatstreepje of een maatstreep zonder getal. Tenzij er een natuurlijk een goede reden is om hiervan af te wijken.  
- Een grafiek voor een wetenschappelijk artikel of een verslag heeft geen titel. Een grafiek voor webteksten of lesmateriaal heeft over het algemeen wel een titel. 
- Als je de onzekerheid op de meetpunten kent, dan is het goed om deze ook weer te geven in je plot. Tenzij deze heel onoverzichtelijk wordt (zoals in een scatterplot met heel veel punten).

*Let op!* Dit zijn weer richtlijnen en geen regels. Denk altijd goed na over wat je doet en waarom. Het eindresultaat moet goed begrijpbaar zijn en daarvoor is het soms nodig om van de richtlijnen af te wijken.


## Staafdiagrammen & Histogrammen

Staafdiagrammen en histogrammen worden allebei typisch gebruikt om frequenties van meetwaardes aan te geven. 

Hier zie je voorbeelden van een staafdiagram en een histogram.

![Een voorbeeld van een staafdiagram.](autos-in-nederland.png){:width="60%"}<br>

Hier<!--FIG , in Fig. \ref{fig:autos-in-nederland}--> zie je een **staafdiagram** dat de hoeveelheid auto's in Nederland laat zien over drie verschillende jaren opgesplitst naar drie auto categorieën. 

![Een voorbeeld van een histogram.](verdeling-van-inkomens-2.png){:width="60%"}<br>

Hierboven<!--FIG , in Fig. \ref{fig:verdeling-van-inkomens-2}--> zie je een **histogram** dat de inkomensverdeling in Nederland laat zien. 

Er is een belangrijk verschil tussen een staafdiagram en een histogram. Een staafdiagram laat de frequentie zien voor *gecategoriseerde* verdelingen. Een histogram wordt gebruikt om het resultaat van een *numeriek sorteerbare* verdeling mee weer te geven. In het geval van een histogram gaat het vaak om data met een continue grootheid, zoals bijvoorbeeld bij het opmeten van lengte of gewicht. In dat geval sorteer je de data per interval.

Bij het weergeven van data in een histogram wordt de data gegroepeerd in intervallen. De breedte van de staven (in het vervolg 'bins' genoemd) geeft de breedte van de intervallen. 

Bij een staafdiagram kun je de frequentie direct aflezen; voor één categorie lees je op de as af hoe vaak deze voorkomt. Voor een histogram is de frequentie gelijk aan de oppervlakte van de balken, en dus afhankelijk van de bin breedte.

### Breedte van de bins bij een histogram

Voor een histogram is de breedte van de intervallen van belang. Als we te weinig bins kiezen dan worden de intervallen erg groot (/breed) en is er minder te zeggen over het gedrag van de data. Als we te veel bins kiezen dan fluctueert de hoogte van de (smalle) bins onderling erg en is het ook lastiger om de trend in de data goed in te schatten.

Dit bekijken we aan de hand van een voorbeeld<!--FIG , zie Fig. \ref{fig:Plot11_RandNorm_Hist_GoedeBins}-->. Zo zou het kunnen zijn dat het ideale plaatje bij een gegeven dataset het volgende is.

![Een histogram met een goede bin en range keuze.](Plot11_RandNorm_Hist_GoedeBins.png){:width="400px"}<br>

Als we te brede bins kiezen dan wordt de data afgevlakt en kunnen we het bovenstaande gedrag niet meer herkennen<!--FIG , zie Fig. \ref{fig:Plot12_RandNorm_Hist_TeWeinigBins}-->.

![Een histogram met een te grove binning.](Plot12_RandNorm_Hist_TeWeinigBins.png){:width="400px"}<br>

Kiezen we juist te smalle bins, <!--FIG ,zoals hieronder in Fig. \ref{fig:Plot13_RandNorm_Hist_TeVeelBins}--> dan kunnen we het gedrag van de data nog wel herkennen (in dit geval) maar er is veel fluctuatie in de hoogte van de bins. 

![Een histogram met een te fijne binning.](Plot13_RandNorm_Hist_TeVeelBins.png){:width="400px"}<br>

Met het kiezen van te veel bins hebben we dus visuele ruis geïntroduceerd, dit maakt het moeilijker om het gedrag op het oog te herkennen.

Bij het bepalen van het optimale aantal bins en de optimale bin breedte is het belangrijkste dat het gedrag van de data goed zichtbaar is. Er zijn verschillende formules (bijvoorbeeld de square of de Sturges formule) ontwikkeld waarmee je het aantal bins dat je nodig hebt kunt berekenen. Echter, geen van die formules kun je blind toepassen. Het is veel beter om gewoon goed naar je dataset te kijken en een inschatting te maken van de bin breedte. 

**Bij het maken van een histogram moet je goed letten op het volgende:**

* Het bereik (de range) die je kiest op de horizontale as. Van waar tot waar plot je de data? Meestal wil je de gehele dataset laten zien, maar soms wil je juist inzoomen op een kleiner stukje. 
* De bin breedte. Meestal kies je voor het hele histogram dezelfde bin breedte, in sommige gevallen kun je verschillende bin breedtes kiezen. In elk geval geldt dat het histogram goed 'leesbaar' moet zijn. Het moet duidelijk blijven hoe de data gedistribueerd is. Wat is de trend? Zijn er afwijkingen van die trend.
* Let bij histogrammen erg goed op waar de grens van een bin ligt. Vooral als je een dataset met natuurlijke getallen weergeeft is het belangrijk dat de bin grenzen netjes *tussen* de natuurlijke getallen ligt. Anders kan de distributie van de data verkeerd gerepresenteerd worden.
* Het histogram is makkelijker leesbaar als de bins een natuurlijk interval hebben. Als je range van 0 tot 10 loopt is het heel gek om deze te verdelen in 7 bins.

**Voor zowel histogrammen als staafdiagrammen geldt:**

* Natuurlijk moeten bij histogrammen en staafdiagrammen ook netjes aslabels worden gebruikt.
* Als je meer dan één dataset laat zien maak dan gebruik van een legenda.

## Wanneer gebruik je wat?

1. Als je de incidentie (of frequentie) van meetwaarden wil laten zien dan gebruik je een histogram of staafdiagram. 
	* Een staafdiagram gebruik je als de meetwaarden discreet zijn gecategoriseerd, bijvoorbeeld in het soort auto of per kleur. 
	* Een histogram gebruik je voor grootheden die numeriek geordend kunnen worden, zoals bijvoorbeeld een grootheid met integer of continue waardes.

2.  Als je de relatie tussen twee grootheden wil tonen kies je voor een grafiek of een scatterplot. 
	*	Je gebruikt een grafiek als de afhankelijke grootheid (meestal de langs de x-as) unieke waardes kent. Dus voor een bepaalde waarde van x is maar één uitkomst van y mogelijk. Andersom zijn er wellicht meerdere waardes voor x voor een bepaalde gemeten grootheid y. Bijvoorbeeld de gemeten temperatuur om 12 uur 's middags op een bepaalde locatie. Er kan maar 1 gemeten temperatuur bestaan.
	*  Je gebruikt een scatterplot als er geen unieke waarde is per afhankelijke grootheid. Bijvoorbeeld als je de lengte van een student meet in relatie met de leeftijd. Er zijn waarschijnlijk meerdere studenten met dezelfde leeftijd in de groep die hoogstwaarschijnlijk in lengte van elkaar verschillen.

	
###Richtlijnen opmaak staafdiagrammen en histogrammen




## Data plotten met Python

Om in Python te kunnen plotten moeten we als eerste een library importeren die ingebouwde functies heeft voor het visueel weergeven van data. Een populair pakket is Matplotlib, deze zullen we in dit vak dan ook gebruiken (er zijn ook andere geschikte pakketten zoals Seaborn, geplot en Plotly). 
We importeren de **`pyplot`** functie vanuit Matplotlib en geven deze de naam 'plt' met het volgende commando:

    import matplotlib.pyplot as plt

De naamgeving **`plt`** met het commando **`as plt`** is optioneel, maar wel handig omdat we deze functie over het algemeen vaak zullen gebruiken (dat scheelt typen).


### Voorbeeld: een grafiek plotten
Stel we hebben de hoogte van een vallende bal gemeten als functie van de tijd. In de tabel is de gemeten data weergegeven:

| t (s) | 0.0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 | 5.5 | 6.0 |
| --- | ---| --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| h(cm) | 180.0 | 178.8 | 175.1 | 169.0 | 160.4 | 149.3 | 135.9 | 120.0 | 102.0 | 80.7 | 57.4 | 31.6 | 3.4 |


Nu maken we een lijst **`t_data`** aan voor de tijd en een lijst **`h_data`** voor de hoogte van de bal:

    t_data = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
    h_data = [180.0, 178.8, 175.1, 169.0, 160.4, 149.3, 135.9, 120.0, 102.0, 80.7, 57.4, 31.6, 3.4]

Daarna roepen we het **`plot`** commando uit matplotlib.pyplot aan:

    plt.plot(t_data, h_data, 'ro')

Met **`'ro'`** geven we aan dat we rode gevulde punten in de plot willen. De plot ziet er nu als volgt <!--FIG (zie Fig. \ref{fig:Plot14_Vallenbal_PlotOnopgemaakt})--> uit.

![Plot met rode punten.](Plot14_Vallenbal_PlotOnopgemaakt.png){:width="400px"}<br>

Je ziet dat de assen automatisch vanaf de laagste waarde tot aan de hoogste waarden gaan, en hierbij niet eindigen op een maatstreepje. Daarnaast willen we graag labels op de assen.

De limiet van de assen kunnen we aangeven met de commando's **`plt.xlim`** en **`plt.ylim`**:

    plt.xlim(0,7)
    plt.ylim(0,200)

Labels voor de assen kunnen we als volgt specificeren:

    plt.xlabel('t (s)')
    plt.ylabel('h (cm)')
    
Het resultaat is<!--FIG (Fig. \ref{fig:Plot15_Vallenbal_PlotOpgemaakt})-->.

![Plot met aslabels en -ranges.](Plot15_Vallenbal_PlotOpgemaakt.png){:width="400px"}<br>

De volledige code tot nu toe is:    

    # dataset in lijsten zetten
    t_data = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
    h_data = [180,178.8,175.1,169.0,160.4,149.3,135.9,120,102,80.7,57.4,31.6,3.4]
    
    # data plotten, as-limieten instellen, as-labels instellen
    plt.plot(t_data, h_data, 'ro')    
    plt.xlim(0,7)
    plt.ylim(0,200)
    plt.xlabel('t (s)')
    plt.ylabel('h (cm)')

Als we nu nog een dataset hebben, bijvoorbeeld van dezelfde bal die vanaf een hoogte van 160 cm valt in plaats van een hoogte van 180 cm:

    # tweede dataset in lijsten zetten
    t_data2 = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
    h_data2 = [160,158.8,155.1,149.0,140.4,129.3,115.9,100,82,60.7,37.4,11.6]
    
Deze dataset kunnen we in de grafiek van de eerste plotten door twee keer het plot commando achter elkaar te gebruiken: daarna gebruiken we weer dezelfde eigenschappen voor de limieten en de aslabels:

    plt.plot(t_data, h_data, 'ro')
    plt.plot(t_data2, h_data2, 'bo')
   
Daarna gebruiken we weer dezelfde eigenschappen voor de as-limieten en de as-labels:

    plt.xlim(0,7)
    plt.ylim(0,200)
    plt.xlabel('t (s)')
    plt.ylabel('h (cm)')
    
De plot ziet er dan als volgt uit<!--FIG (Fig. \ref{fig:PLOT16_MeerdereScatter})-->.<br>

![Twee datasets.](PLOT16_MeerdereScatter.png){:width ="400px"}<br>

Omdat er meerdere datasets in één grafiek zijn weergegeven is het noodzakelijk om hier een legenda bij te plaatsen. Een legenda kan op meerdere plaatsen in de figuur neergezet worden. Voordat we de legenda kunnen toevoegen moeten we de plots eerst labelen. Dit doen we door **`label = "naam"`** achteraan in de **`plot`** commando's toe te voegen:

    plt.plot(t_data, h_data, 'ro' , label='h(0) = 180 cm')
    plt.plot(t_data2, h_data2, 'bo', label='h(0) = 160 cm')

Nu kunnen we de legenda als volgt toevoegen (hier kiezen we ervoor om de legenda in de rechterbovenhoek neer te zetten zodat er geen overlap is met de grafieken zelf): 

    plt.legend(loc='upper right', shadow=True, ncol=1)

De grafiek is nu als volgt<!--FIG (Fig. \ref{fig:PLOT18_MeerdereScatter_legenda})-->.

![Plot met legenda.](PLOT18_MeerdereScatter_legenda.png){:width ="400px"}<br>

De volledige code tot nu toe is:    

    # dataset in lijsten zetten
    t_data = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
    h_data = [180,178.8,175.1,169.0,160.4,149.3,135.9,120,102,80.7,57.4,31.6,3.4]
    
    # tweede dataset in lijsten zetten
    t_data2 = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
    h_data2 = [160,158.8,155.1,149.0,140.4,129.3,115.9,100,82,60.7,37.4,11.6]
    
    # data plotten, as-limieten instellen, as-labels instellen
    plt.plot(t_data, h_data, 'ro' , label='h(0) = 180 cm')
    plt.plot(t_data2, h_data2, 'bo', label='h(0) = 160 cm')
    plt.xlim(0,7)
    plt.ylim(0,200)
    plt.xlabel('t (s)')
    plt.ylabel('h (cm)')
    
    # legenda toevoegen
    plt.legend(loc='upper right', shadow=True, ncol=1)


Een ander voorbeeld is dat we lijnen willen plotten, bijvoorbeeld van een theoretisch verband. (De conventie is dat data altijd met punten wordt uitgebeeld.) 
Dit kan je als volgt doen:


    # datasets in lijsten
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] #2x+1
    y2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] #x+2

    # datasets plotten als 'solid' lijnen
    plt.plot(x, y1, 'r-' , label='dataset 1')
    plt.plot(x, y2, 'b-', label='dataset 2')
    plt.xlim(0,7)
    plt.ylim(0,20)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # legenda toevoegen
    plt.legend(loc='upper right', shadow=True, ncol=1)

    
De bijbehorende plot<!--FIG (Fig. \ref{fig:PLOT17_MeerdereLijnen_legenda})-->.

![Een plot met twee lijnen en legenda.](PLOT17_MeerdereLijnen_legenda.png){:width="400px"}<br>

### Voorbeeld een histogram plotten

In de allereerste opgave van module 1 ga je een histogram plotten. In die opgave staat stap voor stap uitgelegd hoe je dat moet doen. 

Maar kijk vooral ook in de [online manual](https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html) van matplotlib.

Succes!






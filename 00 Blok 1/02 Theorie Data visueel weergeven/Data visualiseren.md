## Data visueel weergeven

In dit deel bekijken we de verschillende manieren om data visueel te representeren. Aan bod komen grafieken, staafdiagrammen en histogrammen. Daarnaast zullen we deze gaan plotten met behulp van Python.

### Grafieken

Een grafiek is over het algemeen een visuele weergave van een functieverband of van data in een tweedimensionaal assenstelsel. Hierbij kun je bijvoorbeeld denken aan het plotten van de   

Er zijn een aantal afspraken m.b.t. het plotten van een functieverband of data in een grafiek.

Als we de grafiek van een dataset plotten dan doen we dat over het algemeen met een **scatter plot** (data wordt weergegeven met punten). Lijnen zijn doorgaans voorbehouden aan theoretische verbanden en fit functies. Gemeten data plotten met een lijn is over het algemeen niet inzichtelijk. De datapunten zijn vak verspreid, en plotten met een lijn geeft dan een onoverzichtelijk resultaat. Daarnaast geeft de lijn niet het werkelijke gedrag van de gemeten data aan. Stel bijvoorbeeld dat we naar de gemiddelde temperatuur per maand van 1981 t/m 2014 in de Bilt willen kijken. Hieronder een plot met een lijn tussen elk datapunt (Bron: KNMI, gehomogeniseerde data):

<p align="center">![higgs](plot1_lijn_geenOpmaak_NoTopBot_monthscorrect.png){:width="40%"}</p>

Je ziet dat dit niet erg duidelijk is. Het is bijvoorbeeld niet precies te zien waar de gemeten punten zitten, we hebben wel een vermoeden voor de plaatsen waarop de lijn abrupt van richting veranderd, maar wie weet zitten er nog wel meer datapunten tussen.

Laten we dezelfde data eens plotten als *scatterplot*:

<p align="center">![higgs](plot2_scatter_geenOpmaak_NoTopBot_monthscorrect.png){:width="40%"}</p>

Vanuit de scatterplot zien we dat er inderdaad sprake is van veel meer datapunten dan er vanuit de lijnplot te zien is. De plot kan echter netter. Zo staan er geen labels op de assen. Nu kunnen we in dit geval wel raden welke as het jaar aangeeft en welke as de temperatuur, maar in veel gevallen is dat niet zo duidelijk. Om die reden moeten er altijd **labels op de assen** staan, zie het figuur hieronder:

<p align="center">![higgs](plot3_scatter_aslabels_NoTopBot_monthscorrect.png){:width="40%"}</p>

Een andere conventie is dat grafieken doorgaans **beginnen bij de oorsprong, tenzij de data dan onvolledig of onleesbaar wordt**. In het geval van het weergeven van de temperaturen van 1981 t/m 2014 wordt de data bijvoorbeeld onvolledig als we de temperatuur bij nul laten beginnen, we hebben immers ook temparaturen onder het vriespunt. Daarnaast wordt de data onleesbaar als we het jaartal vanaf het jaar nul laten lopen, de datapunten voor de jaren waarin we geïntereseerd zijn zullen dan over elkaar vallen. In het huidige geval is het dus niet van toepassing om in de oorsprong te beginnen, maar dit is bij elke dataset wel het uitgangspunt.

De assen kunnen nog wat netter. Zo eindigd de $$x$$-as *na* de waarde $$20$$, maar het is niet helemaal duidelijk bij welke waarde precies. De $$y$$-as begint een klein stukje voor 1980 en eindigd een klein stukje na 2015. Conventie is om assen te laten **beginnen en eindigen op een maatstreepje**. Daarnaast willen we niet te veel maatstreepjes maar ook niet te weinig. In het algemeen worden **zeven maatstreepjes** aangehouden voor de goede leesbaarheid (eentje meer of minder is niet erg). In ons geval laten we het jaartal beginnen op 1980 en eindigen op 2015, daarnaast laten we de temperatuur beginnen op $$-5$$ C&deg; en eindigen op $$25$$ C&deg;. Op de $$x$$-as hebben we 8 maatstreepjes en op de $$y$$-as hebben we 7 maatstreepjes:

<p align="center">![higgs](plot4_scatter_aslabels_startendMayorTick_NoTopBot_monthscorrect.png){:width="40%"}</p>

Stel we willen de temperatuur in de Bilt nu weergeven t.o.v. de 'Centraal Nederland Temperatuur' (CNT). De CNT is een combinatie van vijf weerstations representatief voor het gebied tussen de steden Utrecht, Arnhem, Breda en Eindhoven. De plot ziet er als volgt uit:

<p align="center">![higgs](plot5_scatter_samen.png){:width="40%"}</p>

De kleuren zijn aangepast t.o.v. eerder. Welk van de twee series hoort bij 'de Bilt' en welke hoort bij 'Centraal Nederland'? Dat is lastig te zien vanuit de plot. Om deze reden wordt er, bij twee of meer series, een **legenda** aan de plot toegevoegd. Bovenstaande plot ziet er met legenda als volgt uit:

<p align="center">![higgs](plot6_scatter_samen_metLegenda.png){:width="50%"}</p>

Tot nu toe hebben we nog geen titels toegevoegd aan de plots. Dit komt omdat dat voor verslagen en wetenschappelijke artikelen ongebruikelijk is, daar moet het onderschrift namelijk al vertellen wat er te zien is in de grafiek. In webteksten, lesteksten en presentaties kan het echter voorkomen dat een grafiek wel een titel heeft, omdat er in die context vaak geen onderschrift toegevoegd kan worden. 

Samengevat:

- Een grafiek van een dataset wordt geplot met punten (een 'scatter plot'). 
- Het resultaat van een fit of een theoretisch verband wordt met een lijn geplot.
- Bij een enkele dataset wordt geen legenda gebruikt. Als er meerdere datasets in één grafiek worden weergegeven dan is een legenda noodzakelijk.
- Aslabels geven weer wat elke as representeerd (inclusief eenheden).
- Assen beginnen in de oorsprong. Een uitzondering kan zijn als de data heel erg ver van de oorsprong af zit.
- Op elke as staan $$\pm$$ 7 maatstreepjes ('ticks').
- Een as begint en eindigd op een groot maatstreepje met een waarde ('major tick') en niet op een klein maatstreepje of een maatstreep zonder getal.
- Een grafiek voor een wetenschappelijk artikel of een verslag heeft geen titel. Een grafiek voor webteksten of lesmateriaal heeft over het algemeen wel een titel.

### Staafdiagrammen & Histogrammen

Staafdiagrammen en histogrammen lijken grafisch gezien op elkaar. Er is echter een belangrijk verschil tussen een staafdiagram en een histogram. 

Een staafdiagram wordt gebruikt om de frequentie bij een *discrete* verdeling aan de geven. Een voorbeeld van een discrete verdeling is het aantal keer dat er kop of munt gegooid wordt met een muntstuk. De discrete waarden zijn in dit geval 'kop' en 'munt'. Een ander voorbeeld van een discrete verdeling is het aantal inwoners in 'Europa', 'Amerika' en 'Azië'. 

Een histogram wordt gebruikt om het resultaat van een *continue* verdeling mee weer te geven. Dit houdt in dat alle tussenligende waarden aangenomen mogen worden. Een voorbeeld van een continue verdeling is het genereren van random kommagetallen tussen de 0 en de 1. Elke tussenliggende waarde kan aangenomen worden. Een ander voorbeeld van een continue verdeling is het gewicht van elke persoon in Nederland. 

Hieronder aan de linkerkant het resultaat van 100 keer kop/munt gooien met een muntstuk weergegeven in een staafdiagram. Aan de rechterkant het resultaat van het genereren van 1000 random kommagetallen tussen de 0 en de 100:

PLOT7PLOT8

VERDERVERDER over bingrootte en de regels daarvan.

Bij een staafdiagram heeft elke groep een staaf die de frequentie aangeeft. Zo is er bij het bovenstaande voorbeeld een staaf voor de groep 'kop' waaruit we kunnen aflezen dat er 60 keer kop is gegooid. Daarnaast kunnen we vanuit de staaf bij de groep 'munt' aflezen dat er 40 keer munt is gegooid. 

Bij het weergeven van data in een histogram wordt de data gegroepeerd in categoriën. De breedte van de staven (in het vervolg 'bins' genoemd), geeft de breedte van een categorie aan. Zo zijn de categoriën bij het histogram hierboven bijvoorbeeld de getallen van: 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99. Vanuit het histogram kunnen we bijvoorbeeld aflezen dat er 100 keer een getal tussen de 60 en 69 en tussen de 80 en 89 voorkomt. Daarnaast kunnen we zien dat getallen tussen de 70 en 80 het minst vaak in de dataset voorkomen en dat getallen tussen de 90 en 99 het meeste voorkomen in de dataset.

Voor een histogram is de breedte van de categoriën van belang. Als we te weinig bins kiezen dan worden de categoriën erg groot (/breed) en is er minder te zeggen over het gedrag van de data. Als we te veel bins kiezen dan fluctueerd de hoogte van de (smalle) bins onderling erg en kan er ook minder over het gedrag van de data gezegd worden.  

Dit bekijken we aan de hand van een voorbeeld. Zo zou het kunnen zijn dat het ideale plaatje bij een gegeven dataset het volgende is:

PLOT 11

Als we te weinig bins kiezen dan wordt de data afgevlakt en kunnen we het bovenstaande gedrag niet meer herkennen:

PLOT 12

Kiezen we juist te veel bins, dan fluctueerd de hiigte van de staven onderling en kunnen we het gedrag ook niet meer herkennen:

PLOT 13

Voor het bepalen van het optimale aantal bins en de optimale binbreedte bestaan verschillende methodes. In dit vak zullen we de METHODE

REGELS BINBREEDTE


### Data plotten met Python

#### Een grafiek plotten

Stel we hebben de snelheid van een rijdend speelgoedautotje gemeten als functie van de tijd. In de tabel hieronder is de gemeten data weergegeven:

TABEL

Om in Python te kunnen plotten moeten we als eerste een library importeren die ingebouwde functies heeft voor het visueel weergeven van data. Een populair pakket is Matplotlib, deze zullen we in dit vak dan ook gebruiken (er zijn ook andere geschikte pakketten zoals Seaborn, ggplot en Plotly). 
We importeren de `pyplot` functie vanuit Matplotlib en geven deze de naam 'plt' met het volgende commando:

    import matplotlib.pyplot as plt

De naamgeving 'plt' met het commando `as plt` is optioneel, maar wel handig omdat we deze functie over het algemeen vaak zullen gebruiken (dat scheelt typen).
Nu maken we een lijst `t_data` aan voor de tijd en een lijst `v_data` voor de snelheid:

    t_data = [,,,]
    v_data = [,,,]

Daarna roepen we het `plot` commando uit matplotlib.pyplot aan:

    plt.plot(t_data, v_data, 'ro')

Met `'ro'` geven we aan dat we rode gevulde punten in de plot willen. Je ziet dat de assen automatisch op ... en ... beginnen. Daarnaast willen we graag labels op de assen en het aantal ticks is nog niet correct. VERDER

VERDER MET VOORBEELD (omdat het om gemeten data gaat, plotten we een scatter plot, ook laten zien hoe een lijn erbij kan (theoretische waarde) en een legenda) Daarna een plot met alleen lijnen.


#### Een staafdiagram plotten

#### Een histogram plotten


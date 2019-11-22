## Data visueel weergeven

In dit deel bekijken we de verschillende manieren om data visueel te representeren. Aan bod komen grafieken, staafdiagrammen en histogrammen. Daarnaast zullen we deze gaan plotten met behulp van Python.

### Grafieken

Een grafiek is over het algemeen een visuele weergave van een functieverband of van data in een tweedimensionaal assenstelsel. Hierbij kun je bijvoorbeeld denken aan het plotten van de   

Er zijn een aantal afspraken m.b.t. het plotten van een functieverband of data in een grafiek. Als we de grafiek van een dataset plotten dan doen we dat over het algemeen met een scatter plot (data wordt weergegeven met punten). Lijnen zijn over het doorgaans voorbehouden aan theoretische verbanden en fit functies. Bij data weet je namelijk niet zeker of deze zich tussen de gemeten punten wel gedraagd zoals een lijn zou aangeven.  

VERDER. hier een voorbeeld met data met veel ruimte ertussen, als je een lijn zou plotten dan impliceert dat een zeker gedrag (laten zien dat het kan zijn dat als je meer punten meet deze bijvoorbeeld hoger zitten). Daarom scatter plot.
VERDER. Ook over een legenda (niet bij 1 dataset, wel bij meerdere/fits/theoretische verbanden)
VERDER labels op de assen
VERDER 7 ticks op de assen
VERDER assen beginnen op nul

SAMENGEVAT BULLET POINTS 

### Staafdiagrammen

### Histogrammen

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


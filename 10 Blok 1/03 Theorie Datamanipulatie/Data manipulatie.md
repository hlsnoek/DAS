## Datamanipulatie

In deze sectie bespreken we het effect van verschuiving, vermenigvuldiging en het verwijderen of toevoegen van datapunten op het gemiddelde, de mediaan, de modus, de range, de variantie, de standaarddeviatie en de coëfficiënt van variatie.

### Data verschuiven

Als alle waarden in een dataset worden opgehoogd of verlaagd met een constante waarde $$b$$, dan veranderen het gemiddelde, de mediaan en de modus met diezelfde waarde $$b$$. De range, variantie en standaarddeviatie blijven gelijk. De coëfficiënt van variatie veranderd proportioneel met $$b$$.

Dit bekijken we eens aan de hand van een voorbeeld. Als dataset nemen we de waarden:

$$5.0, 8.0, 9.0, 11.0, 11.0, 15.0$$

We bekijken het effect op de eigenschappen als we bij alle elementen een waarde van $$6$$ optellen of als we bij alle elementen een waarde $$10$$ af halen:

|Eigenschap| Dataset | Dataset plus 6 | Dataset min 10|
|---|---|---|---|
|Gemiddelde|9.8|15.8|-0.2|
|Mediaan|10|16|0|
|Modus|11|17|1|
|Range|10|10|10|
|Variantie|11.4|11.4|11.4|
|Standaarddeviatie|3.4|3.4|3.4|
|Coeff. var.|~ 0.35|~ 0.26|~ -20|

Je ziet dat het gemiddelde, de variantie en de modus evenveel omhoog/omlaag gaan als de respectievelijke ophoging of verlaging van de waarden in de dataset. De range, variantie en standaarddeviatie veranderen niet. De coëfficiënt van variatie is de verhouding tussen de standaarddeviatie en het gemiddelde. Doordat het gemiddelde veranderd, varieert de verhouding ook tussen de datasets.

### Data vermenigvuldigen

Bij het vermenigvuldigen van data met een bepaalde factor $$c$$ worden het gemiddelde, de mediaan, de modus, de range en de standaarddeviatie met dezelfde factor $$c$$ vermenigvuldigd. De coëfficiënt van variatie blijft hetzelfde. Dit is immers de verhouding tussen de standaarddeviatie en het gemiddelde, en deze verhouding blijft gelijk. De variantie veranderd met een factor $$c^2$$.


Neem als dataset bijvoorbeeld de waarden:

$$20.0, 21.0, 21.0, 27.0, 31.0, 38.0$$

We bekijken het effect op de eigenschappen als we de dataset met een factor $$2$$ vermenigvuldigen en als we de dataset met een factor $$\frac{1}{2}$$ vermenigvuldigen:

|Eigenschap| Dataset | Dataset maal 2 | Dataset maal $$\frac{1}{2}$$|
|---|---|---|---|
|Gemiddelde|26.3|52.7|13.2|
|Mediaan|24|48|12|
|Modus|21|42|10.5|
|Range|18|32|9|
|Variantie|51.1|204.|12.8|
|Standaarddeviatie|7.15|14.3|3.57|
|Coeff. var.|~ 0.27|~ 0.27|~ 0.27|

Je ziet dus dat het gemiddelde, de mediaan, modus, range en standaarddeviatie allen veranderen met een factor $$2$$ respectievelijk $$\frac{1}{2}$$. De variantie veranderd met een factor $$2=2^2$$ en $$\frac{1}{4}=\left(\frac{1}{2}\right)^2$$ respectievelijk. De coëfficiënt van variatie blijft hetzelfde.

### Datapunten verwijderen of toevoegen

Asl we een datapunt verwijderen uit een dataset of toevoegen aan een dataset, dan heeft dit gevolgen voor de waarde van het gemiddelde, mediaan, variantie, standaarddeviatie en coëfficiënt van variatie. Afhankelijk van het punt dat toegevoegd of verwijderd wordt kan het gevolgen hebben voor de modus en de range.

Als we als dataset bijvoorbeeld nogmaals de volgende waarde nemen:

$$20.0, 21.0, 21.0, 27.0, 31.0, 38.0$$

En we verwijderen één van de datapunten met waarde $$21.0$$ dan worden de eigenschappen van deze nieuwe dataset als volgt:

|Eigenschap| Dataset | Dataset punt verwijderd  |
|---|---|---|---|
|Gemiddelde|26.3|27.4|
|Mediaan|24|27|
|Modus|21|geen|
|Range|18|18|
|Variantie|51.1|55.3|
|Standaarddeviatie|7.15|7.4|
|Coeff. var.|~ 0.2713|~ 0.2714|

*Opmerking: De coëfficiënt van variatie is hiet niet met het juiste aantal significante cijfers weergegeven, zodat te zien is dat het verwijderen van een punt ook hier effect op heeft.*

Als we een datapunt met een andere waarde verwijderen uit deze dataset dan heeft dit wel effect op het gemiddelde, de mediaan, variantie, standaarddeviatie en coëfficiënt van variatie maar niet op de modus. Verwijderen we de randwaarden $$20.0$$ of $$38.0$$ of voegen we juist een grotere danwel kleinere waarde toe, dan veranderd de range van de dataset. 









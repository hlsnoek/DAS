## Datamanipulatie

In deze sectie bespreken we het effect van verschuiving, vermenigvuldiging en het verwijderen of toevoegen van datapunten op het gemiddelde, de mediaan, de modus, de range, de variantie, de standaarddeviatie en de coëfficiënt van variatie.

### Data verschuiven

Als alle waarden in een dataset worden opgehoogd of verlaagd met een constante waarde $$b$$, dan veranderen het gemiddelde, de mediaan en de modus met diezelfde waarde $$b$$. De range, variantie en standaarddeviatie blijven gelijk. De coëfficiënt van variatie veranderd proportioneel met $$b$$.

Dit bekijken we eens aan de hand van een voorbeeld. Als dataset nemen we de waarden:

$$5.0, 8.0, 9.0, 11.0, 11.0, 15.0$$

We bekijken het effect op de eigenschappen als we bij alle elementen een waarde van $$6$$ optellen of als we bij alle elementen een waarde $$10$$ af halen:

|Eigenschap| Dataset | Dataset plus 6 | Dataset min 10|
|---|---|---|---|
|Gemiddelde|9.8|15.8|-0.17|
|Mediaan|10|16|0|
|Modus|11|17|1|
|Range|10|10|10|
|Variantie|11.4|11.4|11.4|
|Standaarddeviatie|3.4|3.4|3.4|
|Coeff. var.|~ 0.35|~ 0.26|~ -20|

Je ziet dat het gemiddelde, de variantie en de modus evenveel omhoog/omlaag gaan als de respectievelijke ophoging of verlaging van de waarden in de dataset. De range, variantie en standaarddeviatie veranderen niet. De coëfficiënt van variatie is de verhouding tussen de standaarddeviatie en het gemiddelde. Doordat het gemiddelde veranderd, varieert de verhouding ook tussen de datasets.

### Data vermenigvuldigen

Bij het vermenigvuldigen of delen van data met een bepaalde factor $$c$$ blijven het gemiddelde, de mediaan, de modus, de range, variantie, standaarddeviatie en de coëfficiënt van variatie met dezelfde factor $$c$$.

Neem als dataset bijvoorbeeld de waarden:

$$20.0, 21.0, 21.0, 27.0, 31.0, 38.0$$

We bekijken het effect op de eigenschappen als we de dataset met een factor $$2$$ vermenigvuldigen en als we de dataset met een factor $$\frac{1}{2}$$ vermenigvuldigen:

|Eigenschap| Dataset | Dataset maal 2 | Dataset maal \frac{1}{2}|
|---|---|---|---|
|Gemiddelde|26.3|52.7|-0.17|
|Mediaan|10|16|0|
|Modus|11|17|1|
|Range|10|10|10|
|Variantie|11.4|11.4|11.4|
|Standaarddeviatie|3.4|3.4|3.4|
|Coeff. var.|~ 0.35|~ 0.26|~ -20|

### Data verwijderen of aanvullen







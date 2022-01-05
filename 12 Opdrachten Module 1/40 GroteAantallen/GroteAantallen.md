## M1.4 - Grote Aantallen \*\*\*
<!--REF\label{/opdrachten-module-1/groteaantallen}-->

We hebben een enorme ton kogeltjes en we willen weten hoe zwaar een enkele kogel uit de ton is. De kogels zijn, door variaties in het productieproces, niet allemaal precies even zwaar. De massa's van de kogels zijn **Normaal** ofwel **Gaussisch** verdeeld. We willen graag weten wat de ***typische*** massa is van een kogel uit deze ton. 
Er zit ook een onzekerheid op de meting, maar die is veel kleiner dat de variatie in de kogelmassa's en mogen we negeren.

Het is te veel werk om alle kogels apart te wegen, dus we nemen een steekproef. We nemen eerst een enkele kogel en wegen die. Omdat we niet weten wat de spreiding is in de massa van de kogels, kunnen we nu ook nog niet weten hoe representatief de massa van deze enkele kogel is voor de gemiddelde massa.

We doen daarom nog een tweede meting. Nu kunnen we de resultaten van deze twee metingen vergelijken en een eerste schatting doen van de onzekerheid op de gemeten waardes. Deze schatting op de spreiding van kogel massa's is natuurlijk nog erg onnauwkeurig. We weten niet hoe groot de fout is op de grootheid die we willen meten, namelijk de ***typische*** massa.

We herhalen het experiment daarom nog een paar keer en elke keer kijken we naar het gemiddelde van de metingen die we hebben gedaan. Uiteindelijk kunnen we een de distributie van de metingen bekijken en bepalen wat de standaardafwijking is van de verdeling. Nu hebben we eindelijk een maat voor de nauwkeurigheid van een enkele meting.

Doordat we nu eigenlijk heel veel metingen hebben genomen is de nauwkeurigheid op het gemiddelde, en zo de nauwkeurigheid van de grootheid die we wilden bepalen een heel stuk verbeterd. Intuïtief snappen we dat hoe meer kogeltjes we wegen uit de ton hoe beter we weten wat het gemiddelde is van de kogeltjes in de ton.

De Wet van de Grote Aantallen zegt dat als we een verdeling hebben van random (stochastische) waardes, en deze verdeling een mathematisch goed gedefinieerd gemiddelde heeft, dat het gemiddelde van een steeds grotere dataset uiteindelijk convergeert. Dit betekent dus dat als de dataset aan de voorwaarde voldoet, we een steeds nauwkeuriger beeld hebben van wat het gemiddelde van de data is. We komen hier later nog uitgebreid op terug.

We gaan onze metingen nu simuleren om een gevoel te krijgen hoe de wet van grote aantallen werkt.


Download het volgende bestand in je werkfolder op de computer: [M1.4_GroteAantallen.py](https://das.mprog.nl/course/12%20Opdrachten%20Module%201/40%20GroteAantallen/M1.4_GroteAantallen.py).
Zorg dat dit bestand in dezelfde folder staat als de `DAS_DatasetGenerator.py` file die je in opgave M1.1 al hebt gebruikt.


In `M1.4_GroteAantallen.py` bestand zie je eerst een aantal functies (**`berekenGemiddelde()`**, **`maakSetGemiddelde()`**) die gaan we **later pas** gebruiken.  

Eerst kijken we naar de regel:

	set_gauss = ds.DataSetGroteAantallen(),
	
Hier wordt de dataset met de **gemeten kogel massa (in grammen)** aangemaakt waarbij de elementen een normaalverdeling volgen. We gaan eerst kijken naar de gehele dataset.

> - **M1.4a) Laat zien dat de waardes in de dataset een normaalverdeling volgen. Doe dit door de waardes te plotten in een *histogram*. Zorg dat het histogram er netjes uitziet en dat je de as-labels ook aanmaakt. Kijk eventueel naar de code van opgave M1.1 om te zien hoe je dat moet doen.**<br><br>
>
> - **M1.4b) Reken het gemiddelde, $$\bar{m}$$, en de standaardafwijking, $$s$$, uit van de gehele set metingen. Let bij het noteren van het resultaat op de notatieregels. Programmeer dit zelf uit (en maak dus geen gebruik van functies in python libraries die dit voor je kunnen doen). Je kan je functie uit opdracht M1.3 natuurlijk weer opnieuw gebruiken.**

We gaan nu simuleren dat we steeds meer datapunten hebben in onze dataset. We willen weten wat het gevonden kogel massa is na $1, 2, 3 ... n$ metingen. Hoe verandert het gevonden gemiddelde van de dataset als we nog een extra kogel massa eraan toevoegen?

> Voltooi nu eerst de functie **`berekenGemiddelde(dataset,n)`**. Als je de functie aanroept met n=2 dan is de bedoeling dat functie het gemiddelde uitrekent over de *eerste twee punten in de dataset*, bij n=3 over de eerste drie datapunten etc. 
 
**TIP:** Controleer of de functie goed werkt door het resultaat van bijvoorbeeld n=4 met de hand na te rekenen.

Nu gaan we de functie **`maakSetGemiddeldes()`** afmaken. Deze functie geeft twee lijsten terug: ***n*** en ***gemiddeldes***. **n** loopt van 1 tot het aantal punten in de originele set_gauss dataset en  ***gemiddeldes*** waarin steeds het gemiddelde over de eerste **n** meetwaardes in de dataset wordt berekend. Controleer of de functie goed werkt door bijvoorbeeld de gevonden gemiddeldes uit te printen.

> - **M1.4c) Maak nu een grafiek met op de horizontale as *n* en op de verticale as de bijbehorende berekende gemiddelde waarde, $$\bar{m_n}$$. Als je nu de grafiek afleest bij n=2 dan is het de bedoeling dat je op de verticale as het gemiddelde afleest over de eerste twee punten van de dataset. Let goed op het goed leesbaar maken van de grafiek.**<br><br>
> 
> - **M1.4d) Beschrijf in de grafiek wat er gebeurt. Is dit wat je verwacht had? Waarom wel of waarom niet?**


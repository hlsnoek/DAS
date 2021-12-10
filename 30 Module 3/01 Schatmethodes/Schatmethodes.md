# Schatmethodes

Voordat we met de andere hoofdstukken in deze module beginnen staan we nog even stil bij wat een **schatter** eigenlijk is. 
Dit begrip is al kort geïntroduceerd in opgave [M2.3](opdrachten-module-2/halfwaardedikteii). 


Vaak willen we met behulp van een meting een bepaalde grootheid te weten komen. Soms kunnen we die direct opmeten, maar meestal hebben we een methode of een recept nodig om dit te doen. Denk bijvoorbeeld bij de proef met de halfwaardedikte. We nemen eerst een set metingen en vervolgens hebben we een recept om hieruit de halfwaardedikte te bepalen. Deze halfwaardedikte *schatten* we met behulp van de methode die we een *schatter* noemen (Engels: estimator). 


> Een **schatter** is een steekproefgrootheid (stochast) die als doel heeft een populatieparameter in te schatten.

Het woord schatten is in het Nederlands vaak geassocieerd met een wat slordige manier om iets te bepalen. "Even schatten hoeveel knikkers er in de pot zitten in plaats ze nauwkeurig te tellen." 
Het begrip **schatter** in de statistiek is veel algemener en probeert juist uit te gaan van nauwkeurigheid.

Zonder dat we dit expliciet benoemd hebben zijn we al veel schatters tegengekomen. Bijvoorbeeld het steekproefgemiddelde is een voorbeeld van een schatter. 

> **Voorbeeld** Het gemiddelde van een steekproef met waardes $$x_i$$ en grootte $$n$$ is gedefinieerd als: 
> 
>    $$\displaystyle{ \overline{x} = \frac{1}{n} \sum_{i=1}^{n} x_i.}$$
> 
> Het steekproefgemiddelde $$\overline{x}$$ is berekend met een formule (recept) van metingen. Het steekproefgemiddelde $$\overline{x}$$ noemen we hierom ook wel een **schatter**. De grootheid die we proberen in te schatten is het populatiegemiddelde.


Het doel van de schattingstheorie is een functie of methode te vinden die een goede schatting oplevert van de grootheid die we willen meten. Dat we deze grootheid nooit exact kunnen bepalen is inmiddels duidelijk, alle metingen zijn onderhevig aan meetfouten en onzekerheden.

Er zijn 3 criterea waarmee we evalueren waaraan een goede schatter voldoet:

- de schatter moet **zuiver** zijn, 
- de schatter moet **consistent** zijn,
- de schatter moet **relatief efficïent** zijn. 

Als we verschillende schatters definïeren bieden de criterea een houvast om te bepalen wat de beste schatter is. We gaan kort op deze 3 criterea in.

### Zuiver
We hebben al een andere eigenschap van de schatter bekeken in de opgaves namelijk de zuiverheid die wordt gegeven door: 

$$b = E(\hat{x}) - \mu$$

Waarbij $$b$$ de onzuiverheid is, $$E(\hat{x})$$ de verwachtingswaarde van de te schatten grootheid en $$\mu$$ het populatiegemiddelde van de te schatten grootheid.

Een goede schatter is zuiver. Dat wil zeggen dat de verwachtingswaarde van de schatter gelijk is aan de populatiegrootheid.

> **Voorbeeld** Het steekproefgemiddelde is zuiver als de verwachtingswaarde van het steekproefgemiddelde $$E(\overline{x})$$ gelijk is aan het populatiegemiddelde $$\mu.$$

### Consistent
Naarmate de steekproef groter wordt benaderen we de populatiegrootheid met de schatter. Met andere woorden, de schatter voldoet aan de wet van grote aantallen. 

> **Voorbeeld** Naarmate we meer data nemen benadert het steekproefgemiddelde (de schatter) het populatiegemiddelde (de populatiegrootheid).

### Efficïent
Als er meerdere schatters kunnen worden gedefinïeerd dan heeft een goede schatter relatief de kleinste variantie.
Anders gezegd, als we meerdere recepten kunnen bedenken om tot een inschatting te komen van de populatiegrootheid die we willen meten dan is de beste schatter met de kleinste meetonzekerheid heeft. 

>  **Voorbeeld** We hebben twee schatters, $$\theta_1$$ en $$\theta_2$$, die allebei het doel hebben dezelfde populatiegrootheid $$\mu$$ te bepalen. De variantie op de schatters zijn $$s_1^2$$ en $$s_2^2$$ waarbij $$s_1 < s_2$$. Beide schatters voldoen aan de zuiverheid en consistentheid criterea. De beste schatter is degene met de kleinste variantie. In dit voorbeeld is dat $$\theta_1$$.



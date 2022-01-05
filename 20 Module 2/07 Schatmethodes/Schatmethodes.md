# Schatmethodes
<!--REF\label{/module-2/schatmethodes}-->
1. Ordered TOC
{:toc}

In dit hoofdstuk leggen we uit wat een **schatter** is. 

In een experiment willen we met een meting een bepaalde grootheid te weten komen. Soms kunnen we die direct opmeten, maar meestal hebben we een methode of een recept nodig om dit te doen. Denk bijvoorbeeld bij de proef met de halfwaardedikte. We nemen eerst een set metingen en vervolgens hebben we een recept om hieruit de halfwaardedikte te bepalen. Deze halfwaardedikte *schatten* we met behulp van de methode die we een *schatter* noemen (Engels: estimator). 


> Een **schatter** is een steekproefgrootheid (stochast) die als doel heeft een populatieparameter in te schatten.

Het woord schatten is in het Nederlands vaak geassocieerd met een wat slordige manier om iets te bepalen. "Even schatten hoeveel knikkers er in de pot zitten in plaats ze nauwkeurig te tellen." 
Het begrip **schatter** in de statistiek is veel algemener en gaat uit van nauwkeurigheid.

Zonder dat we dit expliciet benoemd hebben zijn we al veel schatters tegengekomen. Het steekproefgemiddelde zelf is bijvoorbeeld ook een schatter. Het is een recept om, met behulp van een steekproef, een grootheid af te schatten. 

> **Voorbeeld** Het gemiddelde van een steekproef met waardes $$x_i$$ en grootte $$n$$ is gedefinieerd als: 
> 
> $$\displaystyle{ \overline{x} = \frac{1}{n} \sum_{i=1}^{n} x_i.}$$
> 
> Het steekproefgemiddelde $$\overline{x}$$ is berekend met een formule (recept) van metingen. Het steekproefgemiddelde $$\overline{x}$$ noemen we hierom ook wel een **schatter**. De grootheid die we proberen in te schatten is het populatiegemiddelde.


Het doel van de schattingstheorie is een functie of methode te vinden die een goede schatting oplevert van de grootheid die we willen meten. Dat we deze grootheid nooit exact kunnen bepalen is inmiddels duidelijk, alle metingen zijn onderhevig aan meetfouten en onzekerheden.

Er zijn drie criteria waarmee we evalueren waaraan een goede schatter voldoet:

- de schatter moet **zuiver** zijn, 
- de schatter moet **consistent** zijn,
- de schatter moet **relatief efficiënt** zijn. 

Als we verschillende schatters definiëren bieden de criteria een houvast om te bepalen wat de beste schatter is. We gaan kort op deze drie criteria in.

## Zuiver
De zuiverheid van een schatter wordt gedefinieerd als:

$$b = E(\bar{x}) - \mu$$

Waarbij $$b$$ de onzuiverheid is, $$E(\bar{x})$$ de verwachtingswaarde van de te schatten grootheid en $$\mu$$ het populatiegemiddelde van de te schatten grootheid. In het Engels noemen we deze afwijking de bias, vandaar de letter $$b.$$
Voor het woord zuiverheid gebruiken we ook wel *vertekend*. 

Een goede schatter is zuiver. Dat wil zeggen dat de verwachtingswaarde van de schatter gelijk is aan de populatiegrootheid.

> **Voorbeeld** Het steekproefgemiddelde is zuiver als de verwachtingswaarde van het steekproefgemiddelde $$E(\overline{x})$$ gelijk is aan het populatiegemiddelde $$\mu.$$

## Consistent
Naarmate de steekproef groter wordt benaderen we met de schatter de populatiegrootheid. Met andere woorden, de schatter voldoet aan de wet van grote aantallen. 

> **Voorbeeld** Naarmate we meer data nemen benadert het steekproefgemiddelde (de schatter) het populatiegemiddelde (de populatiegrootheid).

## Efficiënt
Als er meerdere schatters kunnen worden gedefinieerd dan heeft een goede schatter relatief de kleinste variantie.
Anders gezegd, als we meerdere recepten kunnen bedenken om tot een inschatting te komen van de populatiegrootheid die we willen meten dan heeft de beste schatter de kleinste meetonzekerheid. 

>  **Voorbeeld** We hebben twee schatters, $$\theta_1$$ en $$\theta_2$$, die allebei het doel hebben dezelfde populatiegrootheid $$\mu$$ te bepalen. De variantie op de schatters zijn $$s_1^2$$ en $$s_2^2$$ waarbij $$s_1 < s_2$$. Beide schatters voldoen aan de zuiverheid en consistent criteria. De beste schatter is degene met de kleinste variantie. In dit voorbeeld is dat $$\theta_1$$.


## Voorbeelden

We bekijken een aantal voorbeelden. 


> **Onzuiver: Een ongeijkte meetlat**
> Je meet in een experiment de gemiddelde lengte van lucifers. Elke lucifer leg je langs een nauwkeurige liniaal en je noteert heel precies de lengte in millimeters. De meetlat zelf is helaas ongeijkt en 1 millimeter op de schaal van de meetlat is in werkelijkheid $$10\%$$ groter. Als we een lengte van 1.0 cm meten, dan is de daadwerkelijke lengte 1.1 cm. Hierdoor ontstaat er een vertekend beeld van de lengte van de lucifers. De verwachtingswaarde van het gemiddelde is dat die $$10\%$$ te klein zal uitvallen. De relatieve onzuiverheid zal dan ook precies $$-10\%$$ zijn. Als we de het gemeten gemiddelde kennen kunnen we deze omrekenen naar de absolute onzuiverheid $$b.$$

 <br>

> **Onzuiver: Een school vissen**
> Je bestudeert een school vissen. Sommige vissen hebben twee zwarte strepen en sommige drie. Het doel van je onderzoek is om de verhouding te bepalen tussen het aantal vissen met twee strepen en het aantal vissen met drie strepen. Je telt in totaal 150 vissen, 50 vissen hebben twee strepen, 70 vissen hebben drie strepen. Van 40 vissen kun je niet zien hoeveel strepen ze hebben omdat er toevallig net steeds een andere vis voor zwemt. Je besluit de 40 vissen eerlijk te verdelen over de twee groepen. Je meet nu 70 vissen met twee strepen en 90 vissen met drie strepen en vindt een verhouding van 7:9.
> 
> Deze schatmethode levert een vertekend beeld op en is dus **onzuiver**. Het zou beter zijn om de 40 ongeïdentificeerde weg te laten uit de berekening en de verhouding op 5:7 te bepalen. Immers van de groep ongeïdentificeerde vissen mag je aannemen dat ze dezelfde verhouding hebben als de vissen die je wel goed hebt kunnen zien. Wel levert de groep van 40 een extra onzekerheid in de bepaalde verhouding. 
> 
> In dit voorbeeld heeft de onzuiverheid niet te maken met een ongeijkt meetinstrument maar met een onzuivere schatmethode.  
> 
> Het zou goed zijn om nog iets meer te weten over dit onderzoek. Kan het zo zijn dat bij sommige vissen waarbij maar twee strepen geteld zijn de derde streep er wel was maar niet zichtbaar was? Ook dat kan een vertekening van het eindresultaat opleveren.  


 <br>

> **Niet consistent: De eerste waarde**
> Het meest bekende voorbeeld van een schatter die niet consistent is, is de volgende. Je neemt een steekproef met $$n$$ waardes van $$x$$. Je steekproef ziet er als volgt uit: $$\{x_1,x_2, .. , x_n \}.$$ We willen met de steekproef het populatiegemiddelde $$\mu_x$$ bepalen en gebruiken hiervoor de eerste waarde van de steekproef, $$x_1.$$ Op zich is dit een zuivere schatter, de waarde van $$x_1$$ geeft wellicht niet een heel nauwkeurige schatting van $$\mu_x$$, maar hij is niet vertekend. De schatmethode is echter niet consistent met de wet van grote aantallen. De nauwkeurigheid van de schatting wordt niet beter als we de steekproef vergroten en de schatmethode noemen we dus *niet consistent*. 


 <br>

> **Efficiënt: Een betere schatter**
> Stel we hebben een verzameling van dinosaurusbotten en we weten dat de botten afkomstig zijn van twee soorten dinosaurussen. We gaan de botten classificeren. We kunnen hierbij gebruik maken van de kleur van de botten. De botten van de ene dinosaurus lijken iets lichter van kleur te zijn dan de andere. Er is wel een grijs gebied, er zijn botten die we niet kunnen classificeren omdat ze niet heel licht en ook niet heel donker van kleur zijn. Deze botten vallen er precies tussen in. 
> 
> Een andere methode is om te kijken naar de dichtheid van de botten. Hier zit een groot verschil in. De botten van de ene soort dino's hebben een veel grotere massadichtheid dan de andere. We kunnen door het volume op te meten en het massa van de botten het soortelijk gewicht bepalen. Het verschil in massadichtheid is veel groter dan de onzekerheid van de meting en ook zit er maar een heel kleine spreiding in de massadichtheid voor de verschillende exemplaren dino's van dezelfde soort. 
> 
> Dit tweede methode is heel omslachtig maar wel zeer efficiënt. Voor alle botten kun je uitsluitsel geven. Omdat er een alternatieve methode bestaat die beter is, noemen we de classificatie methode met behulp van kleur *niet efficiënt*.



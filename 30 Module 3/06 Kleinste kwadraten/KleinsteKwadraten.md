# De kleinste-kwadraten methode

De methode van de kleinste kwadraten is een manier om onbekende parameters te bepalen met behulp van een dataset. Het recept van de kleinste kwadraten is een heel krachtige schatter.

De methode van de kleinste kwadraten wordt ook wel lineaire regressie, of 'fitten' genoemd. De methode kan wiskundig worden afgeleid met behulp van de zogeheten 'maximale waarschijnlijkheid principes'. 



##Schatters
Eerst staan we nog even stil bij wat een *schatter* eigenlijk is. Vaak willen we met behulp van een meting een bepaalde grootheid te weten komen. Soms kunnen we die direct opmeten, maar vaak hebben we een methode of een recept nodig om dit te doen. Denk bijvoorbeeld bij de proef met de halfwaardedikte. We nemen eerst een set metingen en vervolgens hebben we een recept om hieruit de halfwaardedikte te bepalen. Deze halfwaardedikte *schatten* we met behulp van de methode die we een *schatter* noemen (Engels: estimator). 

Als we een meting doen maken we altijd meetfouten, en als we een schatting doen dan is dus ook de nauwkeurigheid van de schatting begrensd. We hebben al een andere eigenschap van de schatter bekeken in de opgaves namelijk de onzuiverheid die wordt gegeven door: 

$$b = E(\hat{x}) - \mu$$

Waarbij $$b$$ de onzuiverheid is, $$E(\hat{x})$$ de verwachtingswaarde van de te schattengrootheid en $$\mu$$ het populatiegemiddelde van de te schatten grootheid.


##De kleinste-kwadraten methode en $$\chi^2$$
Een van de meest krachtige schatters is de methode van de kleinste-kwadraten. Deze gaan we hier bespreken.

Met de kleinste kwadraten methode minimaliseren we het kwadratisch verschil tussen een set metingen en de voorspelde waardes op die metingen, waarbij de voorspelling afhangt van één of meerdere parameters. 

We beginnen meteen met een voorbeeld. Stel dat we een set metingen hebben die er als volgt uitziet. 

![](VoorbeeldLeastSquares0.png){: width="60%"}

We vermoeden een lineair verband tussen de variabelen $$x$$ en $$y$$ met parameters $$a$$ en $$b$$. We willen nu een deze parameters schatten. De vraag is nu hoe bepalen we $$\hat{a}$$ en $$\hat{b}$$. Oftewel bij welke waardes van $$a$$ en $$b$$ wordt onze dataset optimaal beschreven met het lineaire verband. 

![](VoorbeeldLeastSquares.png){: width="60%"}

Bekijk het voorbeeldje hierboven, we zien twee voorbeelden van oplossingen (de rode lijn en de gestreepte zwarte lijn) met elk hun waardes voor $$a$$ en $$b$$. De vraag is nu hoe bepaal je welke het beste is. Hiervoor gebruiken we een maat die we $$\chi^2$$ noemen. 

Stel dat we een functie $$f(x;a,b)$$ hebben die waardes van $$y$$ voorspelt. En we hebben dataset met $$N$$ waardes voor $$x: {x_1,x_2,...,x_N}$$ met corresponderende waardes voor $$y: {y_1,y_2,...,y_N}$$ waarbij elke waarde van $$y$$ gemeten is met precisie $$\sigma_i$$. Nu kunnen we de som nemen van het kwadratische verschil van alle punten in de dataset met de voorspelde waardes $$f(x_i;a,b)$$, geschaald met de onzekerheden $$\sigma_i$$. Deze som noemen we $$\chi^2:$$<br>
<center>$${\displaystyle \chi^2 = \sum_{i=1}^N \left( \frac{y_i - f(x_i;a)}{\sigma_i}\right)^2 }$$</center> 

De meest optimale waarde voor $$a$$ en $$b$$ geeft de kleinste $$\chi^2$$. 

Door het kwadraat te gebruiken en niet het absolute verschil tussen de datapunten en de voorspelling geven we meer waarde aan de punten die ver van de voorspelling afliggen. 

In de meeste gevallen kunnen we vaak algebraïsch de vergelijking oplossing. Namelijk door het minimum van de vergelijking te vinden. Als we nu kijken naar een functie die afhangt van slechts één parameter $$a$$ dan kunnen we het minimum vinden op het punt dat de afgeleide gelijk is aan nul:<br>

<center>$${\displaystyle \frac{\partial \chi^2}{\partial a} =0}$$</center><br>

Dit geeft: 

<center>$${\displaystyle \frac{\partial \chi^2}{\partial a} = \sum_{i=1}^N \frac{1}{\sigma_i^2} \frac{\partial f(x_i;a)}{\partial a} \left( y_i - f(x_i;a)\right) = 0 }$$</center> 

De betreffende waarde van $$a$$ waarvoor dit geldt, genoteerd als $$\hat{a}$$ is dicht bij de echte waarde van de parameter, maar zal natuurlijk nog steeds een afschatting zijn. 

In de vergelijkingen hierboven hebben we maar één afhankelijke parameter gezien maar dit principe kun je ook toepassen op functies met meerder afhankelijke parameters die je dan tegelijkertijd oplost.

Met behulp van een computerprogramma kun je het minimum ook vinden door de $$\chi^2$$ voor veel waardes van $$a$$ en $$b$$ uit te rekenen en uit deze set van waardes het punt met de laagste $$\chi^2$$ te bepalen. 
Uiteraard werkt dat ook voor functies die nog meer vrije parameters kennen. 

Twee filmpjes die het principe van de kleinste kwadraten goed illustreren vind je <a href="https://www.youtube.com/watch?v=YwZYSTQs-Hk">hier</a> en <a href = "https://www.youtube.com/watch?v=0T0z8d0_aY4">hier</a>. 


Om in te schatten **hoe goed** je fit gelukt is moeten we eerst meer weten over de $$\chi^2$$-distributie. Daar gaat het volgende hoofdstuk over.


In opgave M3.1 ga je het principe van de kleinste kwadraten toepassen.






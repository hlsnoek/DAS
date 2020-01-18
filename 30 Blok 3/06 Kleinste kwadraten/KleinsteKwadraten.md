# De kleinste-kwadraten methode

De methode van de kleinste kwadraten is een manier om onbekende parameters te bepalen met behulp van een dataset. De parameters zou je schatters kunnen noemen, immers we bepalen ze met behulp van een recept. Het recept van de kleinste kwadraten is een heel krachtige.


De methode van de kleinste kwadraten wordt ook wel lineaire regressie genoemd. De methode kan wiskundig worden afgeleid met behulp van de zogeheten 'maximale waarschijnlijkheid principes'. Dat gaan we hier niet doen, maar als je er meer over wilt weten kun je er bijvoorbeeld <a href="https://www.youtube.com/watch?v=_-Gnu498s3o">hier</a> wat over vinden.


Met de kleinste kwadraten methode minimaliseren we het kwadratisch verschil tussen een set metingen en de voorspelde waardes op die metingen, waarbij de voorspelling afhangt van één of meerdere parameters. Dit doe je door de parameters die je wilt schatten te variëren. Door het kwadraat te gebruiken en niet het absolute verschil tussen de datapunten en de voorspelling geven we meer waarde aan de punten die ver van de voorspelling afliggen. 

Stel dat we een functie $$f(x;a)$$ hebben die waardes van $$y$$ voorspelt. En we hebben dataset met $$N$$ waardes voor $$x: {x_1,x_2,...,x_N}$$ met corresponderende waardes voor $$y: {y_1,y_2,...,y_N}$$ waarbij elke waarde van $$y$$ gemeten is met precisie $$\sigma_i$$. Nu kunnen we de som nemen van het kwadratische verschil van alle punten in de dataset met de voorspelde waardes $$f(x_i;a)$$, geschaald met de onzekerheden $$\sigma_i$$. Deze som noemen we $$\chi^2:$$<br>
<center>$${\displaystyle \chi^2 = \sum_{i=1}^N \left( \frac{y_i - f(x_i;a)}{\sigma_i}\right)^2 }$$</center> 

De meest optimale waarde voor $$a$$ geeft de kleinste $$\chi^2$$. 


In de meeste gevallen kunnen we vaak algebraïsch de vergelijking oplossing. Namelijk door het minimum van de vergelijking te vinden. <br>

<center>$${\displaystyle \frac{\partial \chi^2}{\partial a} =0}$$</center><br>

Dit geeft: 

<center>$${\displaystyle \chi^2 = \sum_{i=1}^N \frac{1}{\sigma^2} \frac{\partial f(x_i;a)}{\partial a} \left( y_i - f(x_i;a)\right) = 0 }$$</center> 

De betreffende waarde van $$a$$ waarvoor dit geldt, genoteerd als $$\hat{a}$$ is dicht bij de echte waarde van de parameter, maar zal natuurlijk nog steeds een afschatting zijn. 

In de vergelijkingen hierboven hebben we maar één afhankelijke parameter gezien maar dit principe kun je ook toepassen op functies met meerder afhankelijke parameters die je dan tegelijkertijd oplost.

Twee filmpjes die het principe van de kleinste kwadraten goed illustreren vind je <a href="https://www.youtube.com/watch?v=YwZYSTQs-Hk">hier</a> en <a href = "https://www.youtube.com/watch?v=0T0z8d0_aY4">hier</a>. 


In opgave B3.A ga je het principe van de kleinste kwadraten toepassen.






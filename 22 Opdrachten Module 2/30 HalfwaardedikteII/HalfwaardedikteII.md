## M2.3 Halfwaardedikte II ***

We gaan nu terug naar het experiment uit opgave M1.5 waarbij we de halfwaardedikte van lood onderzoeken bij een bepaalde gamma-bron. We gaan de onzekerheid op het meetresultaat, $$d_{half}$$ onderzoeken. 

In opgave M1.5 gebruikten we een methode om de halfwaardedikte te bepalen waarbij we steeds de ratio tussen het aantal counts zonder lood $$N_0$$ en een waarde met lood $$N_{half}$$ uitrekende. Zodra deze ratio onder de 0.5 komt nemen we $$x$$ als de halfwaardedikte. 

> - **M2.3a) Wat is de fout op de ratio R? Bereken deze door gebruik te maken van de fouten op $$N_0$$ en $$N_{half}$$ en de regels voor propagatie van ongecorreleerde fouten ([Deze kan je hier vinden](/module-2/foutenpropagatie)). Schrijf je berekening helemaal uit.** 

Een **schatter** is een recept om de waarde van een parameter af te schatten. De parameter die we hier willen bepalen is de halwaardedikte van lood (voor de energie van onze bron). De schatter is in dit geval $$d_{half}$$.

Nu gaan we het experiment 50 keer herhalen en gaan we kijken naar de distributie van de gevonden halfwaardediktes. We gaan uit deze distributie de standaard deviatie halen en dit gebruiken om de onzekerheid op de gevonden dikte $$d_{half}$$ te bepalen.

Schrijf een loop waarin je 50x een nieuwe dataset genereert waaruit je 50x opnieuw een halfwaardedikte bepaald. Om 50 unieke dataset te maken moet je steeds de zogeheten ***seed*** veranderen. Dat kan je doen door een seed mee te geven aan de DAS dataset generator:
 	
 	for j in range(0,50) :
 		counts, diktes = ds.DataSetHalfwaardeDikte(j)

Binnen deze loop maak je 50 unieke datasets aan waarbij de counts die gemeten worden steeds worden gevarieerd volgens de Poisson statistiek. 

> - **M2.3b) Maak een histogram waarin je de gevonden halfwaardediktes van de 50 verschillende experimenten laat zien. Zorg dat het histogram de distributie netjes laat zien en dat de as-labels goed zijn aangemaakt.**<br>
> **TIP:** de binning in het histogram luistert nauw doordat er alleen bepaalde uitkomsten van de halfwaardedikte mogelijk zijn. Reken precies uit wat de range en de binning moet zijn in het histogram om te voorkomen dat je lege bins midden in de distributie krijgt.  <br><br>
>
> - **M2.3c) Ziet de distributie eruit zoals je verwacht had? Beredeneer je antwoord.**<br><br>
> 
> - **M2.3d) Bepaal nu het gemiddelde van de meetuitkomsten en de standaarddeviatie van de distributie.**  <br><br>
> 
> - **M2.3e) Zeggen deze getallen ook iets of de gemeten waardes gemiddeld altijd te hoog of te laag uitkomen. Beredeneer je antwoord.**

 
We gaan nu kijken hoe zuiver de meting is. De onzuiverheid is gedefinieerd als het verschil tussen de echte waarde en de gemiddelde gemeten waarde. Bij gesimuleerde data kunnen we dit onderzoeken, daarvan kunnen we het meetresultaat vergelijken met de initiële waardes die we hebben gebruikt in de simulatie.
 
Om de zuiverheid van ons experiment te bepalen gaan we dus de bepaalde halfwaardedikte te vergelijken met de initiële halfwaardedikte die gebruikt is om de data te simuleren. Roep hiervoor de volgende functie aan in de dataset generator:

	metingen, diktes, d_true = ds.DataSetHalfwaardeDikteVariatie(s,d_input)

Je geeft twee variabelen mee aan de functie: de seed (**`s`**) en een waarde(**`d_input`**). We komen er zo op terug wat deze variabelen betekenen.
De functie geeft drie objecten terug. De eerste twee zijn de lists met de counts en de looddikte (zoals je eerder ook terugkreeg), de derde variable is halfwaardedikte die gebruikt is als input voor de simulatie. Dit noemen we meestal de *true* waarde in simulaties vandaar dat we hem **`d_true`** noemen. Met de variabele **`d_input`** kunnen we nu de input waarde van de simulatie controleren. In principe is **`d_input`** gelijk aan **`d_true`**, tenzij je de waarde -1 kiest. 

Met deze dataset generator gaan we nu de zuiverheid van onze meting bestuderen.

> * Kijk eerste eens naar wat de *true* waarde was in je datasets die je hierboven hebt gebruikt! Als je voor **`d_input`** nu -1 invult krijg je de halfwaardeditke die gebruikt is voor het genereren van de 50 datasets die je eerder in deze opdracht hebt gebruikt. <br><br>
>
>
> - **M2.3f) Hoe groot is de onzuiverheid van ons experiment? Vergelijk hiervoor de gemiddelde bepaalde halfwaardediktes van de 50 experimenten me de `d_true`.**


Nu kun je het gedrag bekijken over meerdere waardes rond de **`d_true`** waarde. Plaats een grote loop over je hele code en varieer de **`d_input`** waarde bijvoorbeeld met 5 of 10 procent rond je aanvankelijke waarde. Voor elke setting van **`d_input`** bepaal je over 50 experimenten het gemiddelde van de bepaalde waardes van $$\text{d}_{\text{half}}$$. 


> - **M2.3g) Zet de gevonden gemiddelde waardes zet je in een grafiek uit tegen de gekozen waardes van`d_input`. Let goed op de leesbaarheid van je grafiek.**<br><br>
>
> - **M2.3h) Is de onzuiverheid altijd constant of varieert die afhankelijk van de halfwaardedikte?**<br><br>
> 
> - **M2.3i) In dit geval simuleren we het experiment. Zou je een methode kunnen bedenken om de onzuiverheid van je experiment te onderzoeken bij een echte meting?**

## M2.3 Halfwaardedikte II ***
<!--REF\label{/opdrachten-module-2/halfwaardedikteii}-->

We gaan nu terug naar het experiment uit opgave M1.5 waarbij we de halfwaardedikte van lood onderzoeken voor een bepaalde gamma-bron. We onderzoeken in deze opdracht de onzekerheid op het meetresultaat.


In opgave M1.5 gebruikten we een methode om de halfwaardedikte te bepalen. Bij deze methode zochten we naar de eerste dikte, $$d$$, in de grafiek waarvoor geldt dat $$N\leq 0.5 \times N_0$$. Hiervoor wordt steeds een ratio, $$R$$, berekend: 

$${\displaystyle R = \frac{N_d}{N_0}.}$$

Zodra deze ratio onder de 0.5 komt nemen we $$d$$ als de halfwaardedikte. Hierbij geldt dan $$N_d \equiv N_{\mathrm{half}}$$.

> - **M2.3a) Wat is de onzekerheid op de ratio R? Bereken deze door gebruik te maken van de onzekerheden op $$N_0$$ en $$N_{half}$$ en de regels voor propagatie van ongecorreleerde fouten ([Deze kan je hier vinden](/module-2/foutenpropagatiei)). Schrijf je berekening helemaal uit en vul deze ook in om de waarde van de onzekerheid te berekenen.** 

We maken bij het bepalen van de halfwaardedikte gebruik van een recept. 
Zo'n recept om de waarde van een parameter te bepalen noemen we ook wel een **schatter**. De parameter die we hier willen bepalen is de halfwaardedikte van lood (voor de energie van onze bron). De schatter is in dit geval:<br>

$$d_{half} = $$ kleinste waarde van $$d$$ waarvoor geldt dat $$R = \frac{N_d}{N_0} < 0.5$$.

We gaan het experiment nu 50 keer herhalen en kijken naar de distributie van de gevonden halfwaardediktes. Uit deze distributie bepalen we de standaardafwijking en gebruiken dit als onzekerheid op de gevonden dikte $$d_{half}$$.

> - Schrijf een loop waarin je 50 maal een nieuwe dataset genereert. Uit elk van deze datasets bepaal je een de halfwaardedikte met de ratio-methode. Om 50 unieke dataset te maken moet je steeds de *seed* veranderen. Dat kan je doen door deze mee te geven aan de DAS dataset generator:
> 	
>		for j in range(0,50) : 
>			counts, diktes = ds.DataSetHalfwaardeDikte(j)
>
> - Met de bovenstaande loop maak je 50 unieke datasets aan waarbij de counts die gemeten worden steeds worden gevarieerd volgens de Poisson statistiek. Bereken nu, binnen de loop, voor elk van deze dataset de halfwaardedikte met de ratio-methode. Zorg dat je dit getal bewaart in een lijst.
>
> - **M2.3b) Maak een histogram waarin je de gevonden halfwaardediktes van de 50 verschillende experimenten laat zien.** Zorg dat het histogram de distributie netjes laat zien en dat de as-labels goed zijn aangemaakt.<br>
> **TIP:** De binning in het histogram luistert nauw doordat er alleen bepaalde uitkomsten van de halfwaardedikte mogelijk zijn. Reken precies uit wat de range en de binning moet zijn in het histogram om te voorkomen dat je lege bins midden in de distributie krijgt, en de mogelijke uitkomsten gecentreerd zijn op de bin centra.<br><br>
>
> - **M2.3c) Ziet de distributie eruit zoals je verwacht had? Beredeneer je antwoord.**<br><br>
> 
> - **M2.3d) Bepaal nu het gemiddelde van de meetuitkomsten en de standaardafwijking van de distributie.**<br><br>
> 
> - **M2.3e) Zeggen deze getallen ook iets of de gemeten waardes systematisch te hoog of te laag uitkomen. Beredeneer je antwoord.**

 
We gaan nu bekijken hoe zuiver de meting is. Lees hiervoor eerst het hoofdstuk [schatmethodes](/module-2/schatmethodes).

De zuiverheid is gedefinieerd als het verschil tussen de verwachtingswaarde van een schatter en de 'echte' waarde van de te meten parameter. Het symbool voor de zuiverheid is $$b$$ (van het Engelse bias). De formule van de onzuiverheid is: 

$${\displaystyle b = {\text{gemeten waarde}} - {\text{echte waarde}}}.$$


Hoe groter dit verschil, hoe meer vertekend (onzuiver) de meting is. In ons geval is de onzuiverheid het verschil tussen de gemiddelde gemeten $$d_{\mathrm{half}}$$ en de 'echte' halfwaardedikte.
Bij gesimuleerde data kunnen we dit onderzoeken. We kunnen de verwachtingswaarde van de schatter vergelijken met de initiële waardes die we hebben gebruikt om in de simulatie de dataset aan te maken.



 
> Om de zuiverheid van ons experiment te bepalen gaan we dus de bepaalde halfwaardedikte te vergelijken met de initiële halfwaardedikte die gebruikt is om de data te simuleren. Roep hiervoor de volgende functie aan in de dataset generator:<br><br>
>
>	metingen, diktes, d_true = ds.DataSetHalfwaardeDikteVariatie(s,d_input)
>
> Je geeft twee variabelen mee aan de functie: de seed (**`s`**) en een waarde(**`d_input`**). We komen er zo op terug wat deze variabelen betekenen.
> De functie geeft drie objecten terug. De eerste twee zijn de lists met de counts en de looddikte (zoals je eerder ook terugkreeg), de derde variabele is halfwaardedikte die gebruikt is als input voor de simulatie. Dit noemen we meestal de *true* waarde in simulaties vandaar dat we hem **`d_true`** noemen. Met de variabele **`d_input`** kunnen we nu de input waarde van de simulatie controleren. In principe is **`d_input`** gelijk aan **`d_true`**, tenzij je de waarde -1 kiest.<br>
> 
> Met deze dataset generator gaan we nu de zuiverheid van onze meting bestuderen.<br>
> 
> - Kijk eerst eens naar wat de *true* waarde was in je datasets die je hierboven hebt gebruikt! Als je voor **`d_input`** nu -1 invult krijg je de halfwaardedikte terug die gebruikt is voor het genereren van de 50 datasets die je eerder in deze opdracht hebt gebruikt. Het maakt hierbij niet uit wat voor waarde je aan de seed meegeeft, maar je moet wel iets meegeven, gebruik bijvoorbeeld **`s=1`**.<br><br>
>
> - **M2.3f) Hoe groot is de onzuiverheid van ons experiment? Vergelijk hiervoor de gemiddelde bepaalde halfwaardediktes van de 50 experimenten met de `d_true`.**


Nu kun je het gedrag bekijken over meerdere waardes rond de **`d_true`** waarde. 


> - Pas nu je code aan en varieer de **`d_input`** waarde bijvoorbeeld met 5 of 10 procent rond de aanvankelijke waarde. Voor elke setting van **`d_input`** bepaal je over 50 experimenten het gemiddelde van de bepaalde waardes van $$\text{d}_{\text{half}}.$$<br><br> 
>
> - **M2.3g) Zet de gevonden gemiddelde waardes in een grafiek uit tegen de gekozen waardes van `d_input`. Let goed op de leesbaarheid van je grafiek.**<br>
> Tip: Bedenk hoe je de lezer helpt om makkelijk af te lezen waar de zuivere meting zou liggen (dus als d\_half = d\_input). <br><br>
>
> - **M2.3h) Is de onzuiverheid altijd constant of varieert die afhankelijk van de waarde van de halfwaardedikte?**<br><br>
> 
> - **M2.3i) In dit geval simuleren we het experiment. Zou je een methode kunnen bedenken om de onzuiverheid van je experiment te onderzoeken bij een echte meting?**

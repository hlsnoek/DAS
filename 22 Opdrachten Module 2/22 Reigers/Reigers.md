## M2.2 Reigers \*\*\*\*
<!--REF\label{/opdrachten-module-2/reigers}-->

Je vindt helaas een dode reiger in de tuin bij de sloot. Het lijkt op een blauwe reiger maar het zou ook een purperreiger kunnen zijn. Deze twee vogels lijken erg veel op elkaar.
Er zijn [manieren](https://www.vogelbescherming.nl/beleefdelente/blog/lezen/reigers-in-soorten-en-maten) om blauwe en purperreigers te onderscheiden met behulp van uiterlijke kenmerken. Maar je bent een Natuurkundige en geen Bioloog. Online vind je een dataset met informatie over de massa en de spanwijdte van beide soorten reigers.


Download het bestand [M2.2_Reigers.py](https://das.proglab.nl/course/22%20Opdrachten%20Module%202/22%20Reigers/M2.2_Reigers.py) en zorg dat deze in dezelfde folder staat als het `DAS_DatasetGenerator.py` bestand. Je kan eventueel een nieuwe folder voor M2 aanmaken en hier een kopie van het `DAS_DatasetGenerator.py` bestand in plaatsen.


We genereren eerst twee datasets met behulp van de volgende regel code: 

	m_br, span_br, m_pr, span_pr = ds.datasetVogels()
	
De variabelen hebben de volgende betekenis: 

	m_br    : de massa van een blauwe reiger in gram
	span_br : de spanwijdte van een blauwe reiger in cm

De laatste twee variabelen zijn de datapunten voor purperreigers. 
De twee variabelen van de blauwe reigers horen bij elkaar. Van elke reiger in de dataset zijn zowel de massa als de spanwijdte gemeten. De dataset is zo geordend dat het n-de punt uit de **`m_br`**-lijst bij het n-de punt uit de **`span_br`**-lijst hoort. Dit zijn de gegevens van de n-de reiger. <br>
**Let er dus goed op dat je de lijsten in de juiste volgorde houdt.**
Voor de twee variabelen die eindigen op **`_pr`** van de purperreigers geldt precies hetzelfde.


We gaan eerst naar de twee massaverdelingen van de reigers kijken. 

> - **M2.2a) Plot de massaverdelingen van beide reigers in een histogram. Maak een apart histogram waarin je spanwijdtes van de twee soorten reigers plot.** Laat in een legenda zien welke reiger bij welke kleur hoort. Maak de twee histogrammen netjes af en zorg dat duidelijk is welke distributie bij welke soort reiger hoort.<br><br>
> TIP: Gebruik de plot optie **`alpha=0.8`** zodat je histogrammen wat doorzichtig worden. Zo kan je het achterste histogram ook nog altijd goed zien.<br><br>
>  
> - **M2.2b) Maak een tabel waarin je voor beide soorten reigers de gemiddeldes, de standaardafwijkingen en de varianties noteert.** Let goed op de notatie en denk ook even aan de eenheden.


We meten nu de massa op van de reiger dat je gevonden hebt. Gebruik de volgende regel code om dat te doen: 

		reiger_m_laag, reiger_m_hoog = ds.meetMassaReiger()
		
Je krijgt nu een onderwaarde **`reiger_m_laag`** en een bovenwaarde **`reiger_m_hoog`** terug. Deze geven de onzekerheid op de meting aan. Het gemiddelde van deze twee is de gemeten massa: *de centrale waarde*. De waarde van de massa van de reiger ligt **zeker** tussen de boven- en onderwaarde in. 

Met deze informatie kunnen we nu met de Frequentist Methode de kans uitrekenen dat onze reiger een blauwe reiger is. 

> - **M2.2c) Gebruik de dataset `m_br` om de kans uit te rekenen dat je een blauwe reiger vindt die een massa heeft die in het gebied `reiger_m_laag` en `reiger_m_hoog` in ligt. Herhaal dit voor de purperreiger, bereken dus ook $$P(m_{\text{obs}} \mid \text{purperreiger})$$.** <br>
> Dit noem je ook wel de voorwaardelijke kans 
> $$P(\text{reiger_m_laag}$$  $$< m <$$ $${reiger_m_hoog}$$ $$\mid \text{purperreiger})$$. 
> Voor het gemak noteren we dit even als $$P(m_{\text{obs}} \mid \text{purperreiger} )$$. 
> Zie ook het hoofdstuk over [Extra Kansrekenregels](/module-2/extra-kansrekenregels) over voorwaardelijke kansen.<br>
> **Tip** Bedenk dat je voor de dataset van de purperreigers altijd zeker weet dat het om een purperreiger gaat en dat dus per definitie $$P(\text{purperreiger}) \equiv 1.$$<br>
>
> - **M2.2d) Als je kijkt naar de uitkomst van M2.2c), wat voor soort vogel denk je dat het is? Beredeneer je antwoord.**

De frequentist methode, zoals we die hierboven gebruiken, is uiteindelijk een ratio tussen twee getallen. Deze twee getallen hebben een onzekerheid volgens de Poisson verdeling. 

> - **M2.2e) Schrijf de formule uit hoe de onzekerheden van de noemer en teller zich propageren naar de onzekerheid op de uitgerekende kans. Noteer deze formule en bereken met behulp van deze formule de onzekerheden uit op de kansen die je in M2.2c) hebt berekend.**

Je besluit ook de spanwijdte van de reigers op te meten. Misschien geeft dat wel meer uitsluitsel.

		reiger_span_laag, reiger_span_hoog = ds.meetLengteReiger()
		
De output volgt dezelfde logica als hiervoor.

> - **M2.2f) Gebruik dezelfde methode als hiervoor om beide kansen 
> $$ P(w_{\text{obs}} \mid \text{blauwe reiger} )$$ en $$P(w_{\text{obs}} \mid \text{purper reiger} )$$ uit te rekenen maar nu door (alleen) gebruik te maken van de informatie van de spanwijdtes. Noteer ook de onzekerheden op de uitgerekende kansen.**<br><br>
> 
> - **M2.2g) Op basis van deze informatie, wat denk je nu dat het voor vogel is? Beredeneer je antwoord.**

We kunnen nu natuurlijk ook de gecombineerde informatie gebruiken. Hiervoor gaan we eerst de data visualiseren.

> - **M2.2h) Maak een tweedimensionale scatterplot die de tweedimensionale dataset van de massa versus de spanwijdte voor zowel de purperreigers als de blauwe reigers.**  
> **TIP** gebruik de opties **`'o',markersize=3`** in de plot functie. Zorg dat beide datasets weer hun eigen kleur hebben en vergeet de legenda niet. 

Het valt misschien op dat er een verband lijkt te zijn tussen beide grootheden. We gaan eerst kijken naar [de covariantie](/module-2/meerdimensionale-data) en de correlatie tussen de massa en de spanwijdte voor beide vogelsoorten. 

> - **M2.2i) Bereken de covariantie en de correlatie tussen de massa en de spanwijdte voor zowel de meetgegevens van de blauwe reigers als voor de purperreigers.**<br>
> **NB** Het is ook hier de bedoeling dat je dit zelf programmeert. Je mag geen gebruik maken van standaard functies van python die dit direct voor je teruggeven. Uiteraard mag je wel gebruiken maken van functies als `len()`.<br>
> 
>  
> - **M2.2j) Als je naar de berekende correlaties kijkt wat valt dan op, wat voor verband zit er tussen de twee grootheden? Als je toch even als een Bioloog nadenkt, is dit dan wat je verwacht? Leg uit.**<br><br>

We gaan terug naar de kansberekeningen. 

<!--FOR2023: Schrijf hier in de opgave expliciet dat ze de fouten ook moeten berekenen-->
> - **M2.2k) Combineer nu de gegevens en bereken de kansen $${P(m_{\text{obs}}\text{ en }w_{\text{obs}} \mid \text{blauwe reiger})}$$ en $${P(m_{\text{obs}}\text{ en }w_{\text{obs}} \mid \text{purperreiger})}$$.**<br><br>
> 
> - **M2.2l) Welke vogel denk je nu dat het is? Beredeneer je antwoord.**

Na al deze berekeningen lopen we een eindje in de tuin. Op de plek waar we eerder de reiger aantroffen zit nu een andere reiger hartstochtelijk te schreeuwen. Aan de schreeuw hoor je direct dat dit een purperreiger is. Je schat in dat er een kans is van 90$$\%$$ dat deze purperreiger bij de andere reiger hoorde, en dat dat dus ook een purperreiger is. 

> - **M2.2m) Bereken nu de kans dat het inderdaad een purperreiger is geweest: $$P(\text{purperreiger} \mid m_\text{obs} \text{ en } w_{\text{obs}}).$$ Bereken hier alleen de centrale waarde. Geef hierbij ook je berekening.**<br>
> TIP: Maak hierbij gebruik van de [vergelijking](/module-2/extra-kansrekenregels) van Bayes. Om $$P(m_\text{obs} \text{ en }w_{\text{obs}})$$ te berekenen kun je gebruiken maken van de volgende formule: 
> $$P(C) = P(C \mid D)\cdot P(D) + P(C \mid \text{niet }D)\cdot P(\text{niet }D).$$

-----
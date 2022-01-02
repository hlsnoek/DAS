# Hypothese toetsen I
<!--REF\label{/module-3/hypothese-toetsen}-->

1. Ordered TOC
{:toc}

Als je een steekproef hebt genomen en je wil hiermee iets kunnen zeggen over de populatie dan moet er ook nagegaan worden in hoeverre de steekproef ons idee over de populatie ondersteund. 

Dit wordt hypothese toetsen genoemd. Bij hypothese toetsen doorloop je de volgende stappen:

1. Een hypothese opstellen.
2. Een significantieniveau kiezen.<br> (*Let op! Dit is iets anders dan de significantie waarin je een meetwaarde noteert.*)
3. De p-waarde bepalen.
4. Een conclusie trekken.

Deze vier stappen worden hieronder toegelicht.

## Een hypothese opstellen

Een hypothese is een uitspraak over een bepaalde eigenschap van een populatie. Je weet nog niet of deze uitspraak correct is. Een hypothese wordt geformuleerd als stelling.  

> **Voorbeeld: Verschillende hypotheses.**
>
> - 20% van de auto's in Nederland is blauw.
> - 50% van de Nederlanders heeft blauwe ogen.
> - De valversnelling heeft als waarde in Nederland $$9.81 \text{ ms}^{-2}.$$
> - Studenten in Amsterdam halen hogere cijfers dan studenten in Groningen.

Bij hypothese toetsen is er sprake van twee hypotheses. De zogenoemde *nulhypothese* en de *alternatieve hypothese*. 

Bij hypothese toetsen wordt eerst aangenomen dat de eigenschap die onderzocht wordt niet waar is. Dit wordt de *nulhypothese* genoemd. De stelling dat de gewenste eigenschap wel waar is wordt de *alternatieve hypothese* genoemd. De nulhypothese wordt aangegeven met $$H_0$$, de alternatieve hypothese met $$H_{\alpha}$$ (ook $$H_1$$ is veelvoorkomend). 

De procedure bij hypothese toetsen is dat je in eerste instantie aanneemt dat de eigenschap niet waar is (dus je houdt de nulhypothese aan) en dan onderzoekt of dit stand houdt in het kader van de gevonden resultaten. Uiteindelijk hoop je dat je de nulhypothese kunt verwerpen waardoor de alternatieve hypothese (en dus de gewenste waarde van de eigenschap) kunt aannemen.  

De term nulhypothese komt overigens uit het Engels van de 'null hypothesis' en de naamgeving slaat op de hypothese die verworpen (oftewel 'nullified') moet worden.


Dus:

- Alternatieve hypothese $$H_{\alpha}$$: De hypothese die zegt wat je verwacht te vinden in de dataset 
- Nulhypothese: Het omgekeerde van de alternatieve hypothese.

Onderstaand de eerdere hypothesen met bijbehorende nulhypothesen:

> **Voorbeelden van alternatieve hypothese en nulhypothese**
> 
> - $$H_{\alpha}$$: 20% van de auto's in Nederland is blauw.
> - $$H_0$$: Het percentage blauwe auto's in Nederland is geen 20%.

> - $$H_{\alpha}$$: Meer dan 20% van de auto's in Nederland is blauw.
> - $$H_0$$: Minder dan 20% van de auto's in Nederland is blauw.
 
> - $$H_{\alpha}$$: Het percentage Nederlanders met blauwe ogen is 50%.
> - $$H_0$$: Het percentage Nederlanders met blauwe ogen is geen 50%.
 
> - $$H_{\alpha}$$: De valversnelling heeft als waarde in Nederland $$9.81 \text{ ms}^{-2}.$$
> - $$H_0$$: De valversnelling in Nederland is niet gelijk aan $$9.81 \text{ ms}^{-2}.$$
 
> - $$H_{\alpha}$$: Studenten in Amsterdam halen hogere cijfers dan studenten in Groningen.
> - $$H_0$$: De studenten in Amsterdam halen lagere cijfers dan de studenten in Groningen.
 
> - $$H_{\alpha}$$: Het aantal katten in Nederland is groter dan 20 000.
> - $$H_0$$: Het aantal katten in Nederland is kleiner of gelijk aan 20 000.
 
> - $$H_{\alpha}$$: Het percentage mensen over de gehele wereld met een hond is kleiner dan 40%.
> - $$H_0$$: Het percentage mensen over de gehele wereld met een hond is groter of gelijk aan 40%.

In alle bovenstaande gevallen is het dus de procedure om te kijken of we genoeg bewijs hebben om de nulhypothese te kunnen verwerpen zodat we de alternatieve hypothese kunnen aannemen.



## Een significantieniveau kiezen

De volgende stap in hypothese toetsen is het kiezen van het significantieniveau. Dit houdt in dat we bepalen hoe zeker we ervan willen zijn dat we de correcte conclusie trekken, zonder precisie te verliezen.

Niet elke steekproef zal daadwerkelijk iets kunnen zeggen over de bijbehorende populatie. Als we bijvoorbeeld willen weten of het klopt dat 20% van de auto's in Nederland de kleur blauw heeft, maar in de steekproef kiezen we toevallig alleen auto's met een andere kleur, dan zouden we als conclusie kunnen trekken dat er in Nederland geen blauwe auto's rondrijden. Dit klopt echter niet met de daadwerkelijke populatie. Als je op de weg rijdt zie je namelijk wel degelijk blauwe auto's voorbij komen.

In het bovenstaande geval is de alternatieve hypothese dat 20% van de auto's in Nederland blauw is maar we trekken de conclusie dat de nulhypothese (het percentage blauwe auto's in Nederland is geen 20%) correct is.

Er bestaat dus de kans dat we de berekeningen op de juiste manier uitvoeren, maar alsnog de verkeerde conclusie trekken doordat de steekproef niet representatief is. Ook heeft de gemeten grootheid waarop we onze conclusies kunnen trekken altijd een meetonzekerheid. Ook binnen deze onzekerheid kan het net zo uitvallen dat we de verkeerde conclusie trekken.

De statistiek die we gebruiken om de hypothese mee te testen noemen we de **test-statistiek**. In het voorbeeld van de auto's is de test-statistiek het percentage blauwe auto's. Test-statistieken zijn meetbare grootheden waarvan we verwachten dat de uitkomst gevoelig is om de hypothese te kunnen toetsen. 

Er zijn twee manieren waarop we een verkeerde conclusie kunnen trekken: 

- Type I: De nulhypothese is correct maar we verwerpen hem. Dit noemen we ook wel een fout-positieve of vals-positieve uitkomst. De kans op het maken van een type-I fout noemen we $$\alpha.$$
- Type II: Het lukt niet om de nulhypothese te verwerpen maar deze is niet correct. We noemen deze fout ook wel fout-negatief. De kans op het maken noemen we $$\beta.$$

Het lukt nooit helemaal om de kans op een fout-positieve of een fout-negatieve uitkomst te voorkomen. Wel kun je de kans hierop verkleinen door de onzekerheden op de gemeten test-statistiek zo klein mogelijk te houden bijvoorbeeld door een zo groot mogelijke steekproef te nemen of door een meting nauwkeurig te verrichten. 

Voordat we de metingen uitvoeren om de waarde van onze test-statistiek te bepalen en de hypothese toets uit te voeren spreken we het zogenoemde  *significantieniveau* af. Dit is de kans die we maximaal toestaan om een type-I fout te maken. We kunnen bijvoorbeeld kiezen voor de waarde $$\alpha = 10\%$$ of $$\alpha = 1\%.$$

Als de overschrijdingskans van de waargenomen test-statiek kleiner is of gelijk aan het gekozen significantieniveau dan verwerpen we de nulhypothese. Is de waargenomen kans groter dan de gekozen waarde, dan verwerpen we de nulhypothese niet. De overschrijdingskans noemen we ook wel de p-waarde en leggen we in de volgende paragraaf uit. 

Kiezen we bijvoorbeeld een significantieniveau van $$\alpha=5\%$$ dan verwerpen we de nulhypothese zodra de waargenomen kans kleiner is dan $$5\%$$. Is de waargenomen kans groter dan $$5\%$$, dan verwerpen we de nulhypothese niet. 

Hoe kleiner de vooraf gekozen waarde van $$\alpha$$ is, des te zekerder we ervan kunnen zijn dat we de nulhypothese rechtmatig verwerpen. In principe wil je het significantieniveau daarom zo laag mogelijk kiezen. Maar het kiezen van een zeer kleine waarde van $$\alpha$$ heeft ook een nadeel. Hoe de lager we het significantieniveau kiezen, hoe meer gegevens we nodig hebben om de nulhypothese te kunnen verwerpen. De onzekerheid op de gemeten waarde van de test-statistiek zullen we heel nauwkeurig moeten bepalen. Dit betekent dat je langer moet meten of meer tests moet uitvoeren. In sommige onderzoeken is dit een groter probleem dan in andere. 

Denk maar eens aan de effectiviteit bepalen van een bepaald medicijn. Je moet dan veel patiënten vinden waar het medicijn voor zou moeten helpen. Als je de werking van paracetamol bij hoofdpijn wil onderzoeken is dit misschien geen groot probleem, maar wil je de werking van een medicijn testen die werkt bij een zeer zeldzame ziekte, dan is het gewoon erg lastig zo niet onmogelijk om hele grote groepen te testen. 

Ook binnen de natuur- en sterrenkunde verschilt het nogal of je grote datasets kunt verkrijgen. In een experiment in de deeltjesfysica is het bijvoorbeeld relatief eenvoudig om een grote dataset te verkrijgen in een bostingsexperiment zoals op CERN en zo de de onzekerheid op je test-statistiek te verkleinen met enorm grote steekproeven. Maar het onderzoek naar de smaak van neutrino die bij supernova's worden geprodueerd is lastig, er zijn niet heel veel supernova's. 

Het is dus altijd een afweging tussen het zo zeker mogelijk zijn van correctheid van het verwerpen van de nulhypothese, en de uitvoerbaarheid van het onderzoek.

## p-Waarde bepalen

Na het kiezen van het significantieniveau, bepalen (of meten) we de *p-waarde* behorende bij de gemeten test-statistiek. De p-waarde is de kans om de geobserveerde meetwaarden te vinden onder de aanname dat de nulhypothese correct is.

> **Voorbeeld** Stel we hebben de nulhypothese dat het percentage blauwe auto's in Nederland geen 20% is. 
> We doen een meting waarbij we gedurende een dag het aantal blauwe auto's tellen die op de A6 voorbij komen. De kans dat we een uitkomst kunnen hebben van 25% blauwe auto's, **onder de aanname dat de nulhypothese correct is** (geen 20% blauwe auto's), is de p-waarde. Hoe kleiner de p-waarde die we vinden des te meer grond we hebben om de nulhypothese te verwerpen.  

<!--De p-waarde is dus eigenlijk het laagste niveau van significantie waarop de nulhypothese verworpen kan worden. vinden we bijvoorbeeld een p-waarde van 10%-->   

Er zijn verscheidene methodes voor het hypothese toetsen. In deze sectie behandelen we het bepalen van de p-waarde voor een Normaal verdeelde dataset, middels de zogenoemde 
*z-toets*. 

Ook voor data met een andere distributie kan de p-waarde bepaald worden via de z-toets voor een Normale verdeling zolang de kansdichtheidsdistributie van de test-statistiek bekend is. 


Afhankelijk van de manier waarop de nulhypothese en alternatieve hypothese opgesteld zijn, bepalen we de *eenzijdige overschrijdingskans* of de *tweezijdige overschrijdingskans*. Is de nulhypothese opgesteld met de formulering 'is gelijk aan' of 'is ongelijk aan', dan bepalen we de tweezijdige overschrijdingskans. Is de nulhypothese opgesteld met de formulering 'groter/kleiner dan' of 'groter/kleiner of gelijk aan' dan is het noodzakelijk om de eenzijdige overschrijdingskans te bepalen. Dus:

|$$H_0$$ met | $$H_{\alpha}$$ met  |type overschrijding|
|---|---|---|
|$$=$$|$$\neq$$|tweezijdig|
|$$\neq$$|$$=$$|tweezijdig|
|$$\leq$$ | $$>$$ | eenzijdig|
|$$\geq$$|$$<$$|eenzijdig|

> **Voorbeelden van nulhypothesen waarbij er sprake is van het bepalen van de tweezijdige overschrijdingskans:**
>
>- $$H_0$$: Het percentage blauwe auto's in Nederland is geen 20%.
>- $$H_0$$: Het percentage Nederlanders met blauwe ogen is 50%.

 <br>

> **Voorbeelden van nulhypothesen waarbij er sprake is van het bepalen van de eenzijdige overschrijdingskans:**
>
>- $$H_0$$: De studenten in Amsterdam halen lagere cijfers dan de studenten in Groningen.
>- $$H_0$$: Het aantal katten in Nederland is kleiner of gelijk aan 20 000
>- $$H_0$$: Het percentage mensen over de gehele wereld met een hond, is groter of gelijk aan 40%

<!--De eenzijdige en tweezijdige overschreidignskansen kun je als volgt zien. Als we in de nulhypothese stellen dat een eigenschap gelijk is aan een bepaalde waarde,   
Hebben we bijvoorbeeld de nulhypothese dat het percentage mensen met blauwe ogen geen 50% is, dan -->

Zoals eerder vermeld geeft de p-waarde de kans dat waargenomen uitkomst gevonden kan worden onder de aanname dat de nulhypothese correct is. 
De p-waarde is dus gelijk aan een zeker oppervlak onder de Normaalkromme. Deze kun je berekenen met de $$z$$-score.


## Conclusie trekken

Tot nu toe hebben we de nulhypothese en de alternatieve hypothese opgesteld. Daarna hebben we bepaald welk significantieniveau we zullen aanhouden. Vervolgens hebben we de z-score en daarmee de p-waarde bepaald. Maar hoe trek je aan de hand hiervan nu een conclusie over de nulhypothese? 

Dit bekijken we aan de hand van een paar voorbeelden:

> **Voorbeeld 1:** We onderzoeken de staartlengte van volgroeide lapjeskatten in Nederland, en stellen de volgende hypotheses op:
>
> - $$H_{\alpha}$$: De lengte van de staart van een volgroeide lapjeskat in Nederland is groter dan 10 cm.
> - $$H_0$$: De lengte van de staart van een volgroeide lapjeskat in Nederland is kleiner of gelijk aan 10 cm.
>
> Bij voorbaat kiezen we als significantieniveau $$\alpha=5\%$$.
>
> We meten de staartlengte van 300 lapjeskatten in Nederland (met alle gevolgen van dien voor de onderzoekers), en zetten het resultaat uit in een histogram. Dit resulteert in een Normale verdeling met gemiddelde $$\mu=25$$ cm en een standaardafwijking $$5$$ cm.
>
> De nulhypothese stelde dat de lengte van de staart van een volgroeide lapjeskat kleiner is dan 10 cm. We bepalen dus de p-waarde die hierbij hoort:
>
> $$\begin{aligned}P(X<10) &= P\left( Z<\frac{10-25}{5} \right)\\ &= P(Z<-3) \end{aligned}$$
>
> Als we in de [tabel](https://www.ztable.net/) kijken dan hoort er een waarde van $$0.00135$$ bij deze Z-score. Dus:
>
> $$P(X<10) = P(Z<-3) = 0.00135$$
> 
> De p-waarde is dus 0.14%. Op grond van het eerder gekozen significantieniveau van 5% verwerpen we de nulhypothese. In dit geval is het zo dat we de nulhypothese ook hadden verworpen als we $$\alpha=10\%$$ of $$\alpha=1\%$$ hadden gekozen.

Is de p-waarde kleiner dan het gekozen significantieniveau dan verwerpen we de nulhypothese. Is de p-waarde groter dan het gekozen significantieniveau dan verwerpen we de nulhypothese niet.

Het is goed om te beseffen dat we **niet** kunnen zeggen dat onze alternatieve hypothese correct is of dat de nulhypothese fout is. De p-waarde geeft namelijk geen bewijs. Wel hebben we met de p-waarde een onderbouwing om de nulhypothese, met inachtname van het gekozen significantieniveau, wel/niet te verwerpen.

> **Voorbeeld 2:** We onderzoeken de gemiddelde lengte van alle vrouwen ($$> 18$$ jaar) in Nederland, en stellen de volgende hypotheses op:
>
> - $$H_{\alpha}$$: De gemiddelde lengte van alle vrouwen boven de 18 jaar is hoger dan 180 cm.
> - $$H_{0}$$: De gemiddelde lengte van alle vrouwen boven de 18 jaar is lager dan of gelijk aan 180 cm. 
>
> Bij voorbaat kiezen we als significantieniveau $$\alpha=5\%$$.
>
> We meten de lengte van 500 Nederlandse vrouwen boven de 18 jaar. De resultaten volgen een Normale verdeling met gemiddelde $$\mu=165$$ cm en een standaardafwijking $$10$$ cm.
>
> De nulhypothese stelde dat de gemiddelde lengte van de Nederlandse vrouwen hoger is dan 180 cm. We bepalen dus de p-waarde die hierbij hoort:
>
> $$\begin{aligned}P(X>180) &= 1-P(X<180) \\ &= 1-P(Z<\frac{180-165}{10})\\ &= 1-P(Z<1.5) \end{aligned}$$
>
> Als we in de [tabel](https://www.ztable.net/) kijken dan hoort er een waarde van $$0.93319$$ bij deze Z-score. Dus:
>
> $$P(X>180) = 1-P(Z<1.5) = 0.06681$$
> 
> De p-waarde is dus 6.7%. Op grond van het $$\alpha=5\%$$ significantieniveau verwerpen we de nulhypothese dus niet. 









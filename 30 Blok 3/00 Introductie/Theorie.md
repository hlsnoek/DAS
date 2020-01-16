# Hypothese toetsen

1. Ordered TOC
{:toc}

## Introductie

<!--We hebben het al eerder gehad over het onderzoeken van de eigenschappen van een steekproef om vervolgens iets te kunnen zeggen over de eigenschappen van de gehele populatie.-->

Als je een steekproef hebt genomen en je wilt hiermee iets kunnen zeggen over de populatie dan moet er ook nagegaan worden in hoeverre de steekproef ons idee over de populatie ondersteund.

Dit wordt hypothese toetsen genoemd. Bij hypothese toetsen doorloop je de volgende stappen:

1. Hypothese opstellen
2. Significantielevel bepalen 
    - Let op! Dit is iets anders dan de significantie waarin je een meetwaarde noteert.
3. p-waarde bepalen
4. Conclusie trekken

Deze stappen worden hieronder toegelicht.

### Hypothese opstellen

Een hypothese is een uitspraak over een bepaalde eigenschap van een populatie. Je weet nog niet of deze uitspraak correct is. Een hypothese wordt geformuleerd als stelling.  

> Voorbeelden van hypotheses:
>- 20% van de auto's in Nederland is blauw.
>- 50% van de Nederlanders heeft blauwe ogen
>- De valversnelling heeft als waarde in Nederland $$9.81 \text{ ms}^{-2}$$
>- Studenten in Amsterdam halen hogere cijfers dan studenten in Groningen 

Bij hypothese toetsen is er sprake van twee hypotheses. De zogenoemde *nulhypothese* en de *alternatieve hypothese*. 

Bij hypothese toetsen wordt eerst aangenomen dat de eigenschap die onderzocht wordt niet waar is. Dit wordt de *nulhypothese* genoemd. De stelling dat de gewenste eigenschap wel waar is wordt de *alternatieve hypothese* genoemd. De nulhypostese wordt aangegeven met $$H_0$$, de alternatieve hypothese met $$H_{\alpha}$$ (ook $$H_1$$ is veelvoorkomend). 

De procedure bij hypothese toetsen is dat je in eerste instantie aanneemt dat de eigenschap niet waar is (dus je houdt de nulhypothese aan) en dan onderzoekt of dit standhoudt in het kader van de gevonden resultaten. Uiteindelijk hoop je dat je de nulhypothese kunt verwerpen waardoor de alternatieve hypothese (en dus de gewenste waarde van de eigenschap) kunt aannemen.  

Dus:
- Alternatieve hypothese $$H_{\alpha}$$: De hypothese die zegt wat je verwacht te vinden in de dataset 
- Nulhypothese: Het omgekeerde van de nulhypothese 

Onderstaand de eerdere hypothesen met bijbehorende nulhypothesen:

> Voorbeelden van alternatieve hypothese en nulhypothese:
>- $$H_{\alpha}$$: 20% van de auto's in Nederland is blauw.
>- $$H_0$$: Het percentage blauwe auto's in Nederland is geen 20%.

>- $$H_{\alpha}$$: Meer dan 20% van de auto's in Nederland is blauw.
>- $$H_0$$: Minder dan 20% van de auto's in Nederland is blauw.

>- $$H_{\alpha}$$: 50% van de Nederlanders heeft blauwe ogen
>- $$H_0$$: Het percentage Nederlanders met blauwe ogen is geen 50%.

>- $$H_{\alpha}$$: De valversnelling heeft als waarde in Nederland $$9.81 \text{ ms}^{-2}$$.
>- $$H_0$$: De valversnelling in Nederland is niet gelijk aan $$9.81 \text{ ms}^{-2}$$.

>- $$H_{\alpha}$$: Studenten in Amsterdam halen hogere cijfers dan studenten in Groningen 
>- $$H_0$$: De studenten in Amsterdam halen lagere cijfers dan de studenten in Groningen.

In alle bovenstaande gevallen is het dus de procedure om te kijken of we genoeg bewijs hebben om de nulhypothese te kunnen verwerpen zodat we de alternatieve hypothese kunnen aannemen.

### Significantielevel bepalen

De volgende stap in hypothese toetsen is het bepalen van het significantielevel. Dit houdt in dat we bekijken of de steekproef een goede representatie is van de totale populatie.

Niet elke steekproef zal daadwerkelijk iets kunnen zeggen over de bijbehorende populatie. Als we bijvoorbeeld willen weten of het klopt dat 20% van de auto's in Nederland de kleur blauw heeft, maar in de steekproef kiezen we toevallig alleen auto's met een andere kleur, dan zouden we als conclusie kunnen trekken dat er in Nederland geen blauwe auto's rondrijden. Dit klopt echter niet met de daadwerkelijke populatie. Als je op de weg rijdt zie je namelijk wel degelijk blauwe auto's voorbij komen.

In het bovenstaande geval is de nulhypothese dat 20% van de Auto's in Nederland blauw is maar we trekken de conclusie dat de alternatieve hypothese (het percentage blauwe auto's in Nederland is geen 20%) correct is.

Er bestaat dus de kans dat we de berekeningen en statistiek op de juiste manier uitvoeren, maar alsnog de verkeerde conclusie trekken doordat de steekproef niet representatief is.

Er zijn twee manieren waarop de juiste conclusie wordt getrokken:
- De nulhypothese is correct en we concluderen ook daadwerkelijk vanuit de data dat deze correct is.
- De nulhypothese is niet correct en we concluderen ook daadwerkelijk vanuit de data dat we deze mogen verwerpen.

Omdat we de eigenschap alleen van de steekproef bekijken en niet van de gehele populatie weten we nooit helemaal zeker of we wel de juiste conclusie hebben getrokken (je weet immers niet of de nulhypothese in het echt correct/incorrect is).

Het zogenoemde *significantielevel* $$\alpha$$ geeft aan welk risico we willen lopen dat we de nulhypothese foutief verwerpen (d.w.z. de nulhypothese is eigenlijk wel waar maar we concluderen vanuit de data dat deze niet waar is).
<!--Een maat die aangeeft in hoeverre we er zeker van zijn dat we de nulhypothese op de juiste grond verwerpen wordt gegeven met het significantielevel $$\alpha$$. -->

Doorgaans wordt er voor het significantielevel gekozen uit de volgende drie waarden:
- $$\alpha = 10%$$
- $$\alpha = 5%$$
- $$\alpha = 1%$$

Als de waargenomen kans (zie p-waarde hierna) kleiner is of gelijk aan het gekozen significantielevel $$a$$  dan verwerpen we de nulhypothese. Is de waargenomen kans groter dan $$\alpha$$ dan verwerpen we de nulhypothese niet. 

Kiezen we bijvoorbeeld een significantielevel van $$\alpha=5%$$ dan verwerpen we de nulhypothese zodra de waargenomen kans kleiner is dan $$5%$$. Is de waargenomen kans groter dan $$5%$$, dan verwerpen we de nulhypothese niet. 

<!--Hoe kleiner de waarde van het significantielevel des te zekerder zijn we ervan dat we de nulhypothese mogen verwerpen.-->
Hoe kleiner de kans is op de nulhypothese des te zekerder we ervan kunnen zijn dat we deze rechtmatig verwerpen. In principe wil je het significantieleven daarom zo laag mogelijk kiezen. Maar het kiezen van $$\alpha=1%$$ heeft een nadeel. Hoe kleiner het significantielevel des te groter de meetonzekerheid op de gemeten eigenschap. Het is dus altijd een afweging tussen het zo zeker mogelijk zijn van correctheid van het verwerpen van de nulhypothese, en het zo klein mogelijk houden van de meetonzekerheid op de waarde van de eigenschap.

<!--Je wilt er altijd zo zeker mogelijk van zijn dat je de hypothese rechtmatig hebt verworpen, maar het kiezen van $$\alpha=1%$$ heeft een nadeel. Hoe kleiner het significantielevel des te groter de fout op de gemeten eigenschap. Het is dus altijd een afweging tussen het zo groot mogelijk houden van de kans dat we de nulhypothese correct verwerpen, en het zo klein mogelijk houden van de onzekerheid op de waarde van de eigenschap.-->


### p-waarde bepalen


Om de kans te berekenen op een toestand 

- normale verd (z waarde alleen bij mean & norm distr & n>30 & sigma known) (de andere formules niet nbehandelen.)
- one tailed (alleen als je een goed idee hebt van de directionality < of >)
- two tailed (altijd bij =, en ook als je geen goed idee hebt van de directionality)
- z waarde
- p waarde (+ tabel https://www.ztable.net/) ook wel student's t-distributie genoemd



### Kritieke waarden vinden

### Conclusie trekken

We hebben geen bewijs maar wel 'support'








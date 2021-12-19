# Hypothese toetsen II
<!--REF\label{/module-4/hypothese-toetsen-2}-->

1. Ordered TOC
{:toc}

<!--Verder introduceren chi-2 toets. Punten uitsluiten van grafiek. wanneer mag dat?-->


We hebben in module 3 een eerste stap gemaakt met hypothese toetsen. We hebben gezien dat er vier belangrijke stappen zijn. Eerst stellen we de hypothese op die we willen toetsen en ook de nulhypothese. Vervolgens is het belangrijk om een statistiek te vinden die gevoelig is voor de stelling. Met andere woorden, een statistiek waarmee we de hypothese kunnen toetsen. We kiezen van tevoren een significantieniveau ($$p$$-waarde) waarbij we $$H_0$$ of $$H_\alpha$$ kunnen verwerpen. We hebben ook gezien wat de $$z$$-score betekend. 

In dit hoofdstuk leggen we nu een bijzondere vorm van hypothese toetsen uit waarbij we gebruik maken van de kleinste kwadraten methode en de daarbij berekende $$\chi^2$$. 


## Wald test
De Wald test is een bijzondere test die kan worden gebruikt om met behulp van de kleinste kwadraten methode een hypothese te toetsen. 

Het idee is om aan een set meetwaardes twee functies te fitten. De eerste functie, $$f_0$$, beschrijft de dataset onder de hypothese $$H_0$$, de tweede functie, $$f_\alpha$$, beschrijft de dataset onder de alternatieve hypothese $$H_\alpha$$. Het verschil in de geminimaliseerde $$\chi^2$$ voor beide functies wordt gedefinieerd als 

$$\Delta \chi^2 = \chi^2_0 - \chi^2_\alpha.$$ 

Dit chi-kwadraat verschil ($$\Delta \chi^2$$) kan direct worden gebruikt om een p-waarde te berekenen met behulp van een opzoektabel. 

Er zijn hierbij strikte voorwaardes voor het opstellen van de twee functies. De functies mogen slechts in 1 parameter verschillen, verder moeten ze geheel identiek zijn. De $$H_0$$ hypothese wordt hierbij beschreven met het *minste* aantal vrije parameters. Alle parameters die $$H_0$$ kents, kent $$H_\alpha$$ ook.

> **Voorbeeld** Als de nulhypothese wordt beschreven door een functie $$f_0(x;a,b)$$ dan wordt de alternatieve hypothese beschreven door een functie $$f_\alpha(x;a,b,c)$$ waarbij de parameters $$a$$ en $$b$$ identiek zijn en ook de relatie tussen $$x$$ en deze twee parameters gelijk is. 

Alleen als aan de bovengenoemde voorwaarde wordt voldaan dan wordt de $$\Delta \chi^2$$ beschreven door een $$\chi^2$$ functie met vrijheidsgraad $$n=1$$. En zoals we in module 3 hebben beschreven is de $$\chi^2$$ zelf een kansdichtheidsverdeling. We kunnen in dat geval de $$\Delta \chi^2$$ direct omrekenen naar een waarschijnlijkheid en deze is gelijk aan de p-waarde.

> **Voorbeeld Wald test** Stel dat we een chemisch element willen traceren en gebruik maken van spectroscopie. Als het chemische element $$X$$ aanwezig is dan verwachten we een verhoogde intensiteit te zien bij de emissielijn van het specifieke element. We verwachten ook een achtergrondspectrum te zien. Dat wil zeggen we meten over alle golflengtes normaal gesproken een bepaalde intensiteit, ook zonder dat het chemische element aanwezig is. We kunnen nu de twee functies opstellen. Stel dat de achtergrond een lineaire functie volgt  
> $$ I_0(\lambda;a,b) = a+ b\cdot \lambda$$  
> Waarbij $$\lambda$$ de golflengte is.  
> De emissielijn van $$X$$, verwachten we rond 930 nm en de resolutie van de spectroscoop is 1 nm. De intensiteit van de emissielijn wordt dan beschreven door: <br>
> 
> $$ I_\alpha(\lambda;J,\lamda_0=930nm,\sigma=1nm) = J \cdot \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{\lambda - \lambda_0}{\sigma}\right)^2}$$<br>
> 
> We zien dat in principe er geen vrije parameters zijn in deze fit, behalve een schaalfactor $$J$$ die de hoeveelheid intensiteit van het signaal schaalt.  
> 
> De functie $$f_0$$ wordt in dit geval gelijk gesteld aan de functie die de achtergrond (of nulhypothese) beschrijft: $$f_0= I_0$$. De vrije parameters in deze fit zijn $$a$$ en $$b$$.  
> 
> De functie $$f_\alpha$$ die de alternatieve hypothese beschrijft is nu gelijk aan de achtergrond, plus het signaal: $$f_\alpha = I_0 + I_\alpha$$. De vrije parameters in deze fit zijn $$a,b$$ en $$J$$. We voldoen dus aan het criterium van de Wald methode.  
> 
> Het verschil in de geoptimaliseerde $$\chi^2$$'s voor de nul- en de alternatieve hypothese is gelijk aan $$\Delta \chi^2 = \chi^2_0 - \chi^2_\alpha$$. 
> 
> We spreken af dat we de nulhypthese mogen verwerpen als de p-waarde kleiner is dan $$1 \cdot 10^{-6}.$$
> 
> We gaan even naar de data kijken. We hebben het spectrum waargenomen dat hier<!--FIG in figuur \ref{fig:Spectrum}--> wordt getoond.  
> ![Het waargenomen spectrum met de gefitte lijn.](Spectrum.png){:width="60%"}
> 
> In de grafiek zien we een duidelijk piekje rond 930 nm, precies waar we het signaal van het chemische element $$X$$ door $$H_\alpha$$ voorspeld is. De fit resultaten van beide hypotheses zijn in het plaatje weergegeven. Met het verschil in $$\chi^2$$ kunnen we nu een p-waarde uitrekenen. In dit geval is die gelijk aan $$1.6\cdot 10^{-8}$$. Het is dus uitermate waarschijnlijk dat we het chemische element $$X$$ hebben aangetoond in de spectraal analyse.

De berekende p-waarde wordt vaak weer omgerekend in een $$z$$-score. De enige reden waarom dit gedaan wordt is omdat de waardes van de $$z$$-score over het algemeen wat makkelijker liggen. Het is zeg maar een handigere manier om een kans uit te drukken. In het voorbeeld hierboven komt de kans van $$1.6\cdot 10^{-8}$$ overeen met een $$z$$-score van 5.5. Ga maar na, het laatste spreekt een stuk makkelijker uit. 

In het voorbeeld hierboven hebben we een nulhypothese (waarbij alleen een achtergrondspectrum aanwezig is) vergeleken met alternatieve hypothese waarbij een element $$X$$ bestaat en we de emissielijn meten in het spectrum. We hebben een kans gevonden (de p-waarde) van $$1.6\cdot 10^{-8}$$ dat de geobserveerde dataset past bij de nulhypothese. Dit is een uitermate kleine kans en omdat deze kleiner is dan het vooraf afgesproken significantieniveau mogen we de nulhypothese verwerpen. 



## p-Waarde scan

In het voorbeeld hierboven is er een duidelijk stelling over de golflengte van de emissielijn van het element $$X$$, namelijk $$\lambda_0= 930$$ nm. Stel nu dat dat niet zo is, dan zouden we een extra vrije parameter hebben in de functie die $$H_\alpha$$ beschrijft. In dat geval kunnen we de Wald methode niet toepassen. Wat we in dat geval wèl kunnen doen is een zogeheten p-waarde scan uitvoeren. We fixeren dan telkens de waarde van de golflengte van de emissielijn en berekenen voor elk van deze golflengtes de p-waarde. Als er een emissielijn aanwezig is die sterk genoeg is zullen we op die locatie een dip zien in de p-waarde. 

We moeten ook bij deze toets van te voren bepalen bij welke p-waarde we de nulhypothese verwerpen.


> **Voorbeeld p-waarde scan** Hieronder zie je de spectraalfit waarbij we het
> spectrum hebben gefit met een centrale waarde van de spectraallijn op
> 932 nm, net rechts van het piekje op 930 nm. Zoals je in de figuur<!--FIG in figuur \ref{fig:Spectrum932}--> ziet is de waarde voor $$J$$ die de intensiteit van een eventuele emissielijn op 932 nm beschrijft, erg klein: De gefitte functie voor $$H_\alpha$$ wijkt nauwelijks af van de functie die de $$H_0$$ hypothese beschrijft. De berekende p-waarde zal voor deze golflengte dan ook niet heel klein zijn.  
> ![Het waargenomen spectrum met de gefitte lijn voor $$\lambda = 932$$ nm.](Spectrum932.png){:width="60%"}   
> Als we alle p-waardes van de scan nu grafisch weergeven dan krijgen we het hier <!--FIG in figuur \ref{fig:Emissiescan} --> getoonde resultaat.  
> ![De p-waarde scan van de emissiedata.](Emissiescan.png){:width="60%"}  
> Je ziet nu dat er op een aantal plekken in het spectrum een kleine afwijking van de $$H_0$$ hypothese te zien is. Deze komen allemaal overeen met golflengtes waar op het oog een piekje zichtbaar lijkt. Op slechts 1 locatie is er een heel duidelijke afwijking zichtbaar. Precies bij 930 nm. 

Eigenlijk hadden  we van tevoren ook bij deze een significantie moeten afspreken waarbij we de aanwezigheid van het chemische element kunnen aantonen. Zodra de gemeten p-waarde onder deze afgesproken significantie zakt in de p-waarde scan kunnen we claimen het element te hebben aangetoond. Als we hem weer bij een waarde van $$1 \cdot 10^{-6}$$ hadden afgesproken hadden we ook in de p-waarde scan het element $$X$$ kunnen claimen. 


De Wald test is een krachtige methode om hypotheses te toetsen. We gaan hem in opdracht M4.1 toepassen. 
#Oefenopgaves als voorbereiding voor tussentoets 3
Lees goed het [lijstje](/tussentoets-iii/inhoud) door ter voorbereiding voor de tussentoets. Niet voor alle elementen op het lijstje zijn oefenopgaves.

**Let op:** Voor alle opgaven in dit vak geldt dat je bij het noteren van resultaten je moet houden aan de regels. Kijk hiervoor goed naar het stukje 'significantie en notatie' in het hoofdstuk [Meetonzekerheid](/blok-1/meetonzekerheid).

### De centrale limietstelling

### Kleinste kwadraten

### Chi-2

### Hypothese toetsen

**1.** Stel de nulhypothese op bij de gegeven alternatieve hypotheses:
**a.** $$H_{\alpha:} $$De gemiddelde dikte van een vel papier is groter dan $$0.1$$ mm.
<br><br>
<span style = "color:blue"> $$H_0:$$ De gemiddelde dikte van een vel papier is kleiner of gelijk aan $$0.1$$ mm</span><br>
**b.** $$H_{\alpha:}$$ Het gemiddelde aantal kinderen per huishouden in Nederland is gelijk aan $$1.2$$.
<br><br>
<span style = "color:blue"> $$H_0:$$ Het gemiddelde aantal kinderen per huishouden in Nederland is niet gelijk aan $$1.2$$</span><br>
**c.** $$H_{\alpha:}$$ Het gewicht van een pingpongbal is kleiner of gelijk aan $$2.77$$ gram. 
<br><br>
<span style = "color:blue"> $$H_0:$$ Het gewicht van een pingpongbal is groter dan $$2.77$$ gram.</span><br>

-----

**2.** 
Bij een zekere stochast vinden we een p-waarde van 3% en we hebben een significantielevel gekozen van 5%.
**a.** Is de conclusie 'De nulhypothese is niet correct' een juiste conclusie? is de conclusie 'De alternatieve hypothese is correct' een juiste conclusie? Leg uit waarom wel/niet. Zo niet: hoe zou je deze hypothese anders kunnen formuleren?
<br><br>
<span style = "color:blue"> We weten niet wat de echte toestand is van de populatie die onderzocht wordt. Met een steekproef kunnen we de waarde van de eigenschap alleen benaderen. Om deze reden kunnen we nooit zeggen dat de nulhypothese correct dan wel incorrect is. Er bestaat altijd de kans dat de nulhypothese toch correct is zelfs als we hem hebben verworpen op basis van de p-waarde. De conclusie die we in dit geval wel kunnen trekken is dat we de nulhypothese verwerpen op basis van een significantielevel van $$\alpha=5\%$$ </span><br>

**b.** Hoe veranderd je conclusie als je een significantielevel van 10% had gekozen of van 1%?
<span style = "color:blue"> Als $$\alpha=10\%$$ dan is nog steeds $$p<\alpha$$. De conclusie blijft dat we de nulhypothese verwerpen maar nu op basis van het significantielevel van $$10\%$$. Als $$\alpha=1\%$$ dan is $$p>\alpha$$. Nu trekken we de conclusie dat we de nulhypothese niet verwerpen, op basis van een significantielevel van $$1\%$$.  </span><br>

-----

**3.** De productiechef bij een kleurpotlodenfabrikant heeft het vermoeden dat de zaagmachines niet meer zo goed werken. Als de gemiddelde lengte die wordt afgeleverd door de zaagmachines groter of gelijk is aan 177 mm dan zijn de machines aan vervanging toe.

Bij de fabrikant zijn de afgelopen maand 30000 kleurpotloden geproduceert met een gemiddelde lengte van 176 mm en een standaardafwijking van 1 mm. 

**a.** Stel de alternatieve hypothese op behorende bij dit probleem
<br><br>
<span style = "color:blue"> $$H_{\alpha}:$$ De gemiddelde lengte van kleurpotloden die wordt afgeleverd door de machines is groter of gelijk aan 177 cm</span><br>
**b.** Stel nu de nulhypothese op.
<br><br>
<span style = "color:blue"> $$H_{\0}:$$ De gemiddelde lengte van kleurpotloden die wordt afgeleverd door de machines is kleiner dan 177 cm</span><br>
**c.** Bereken de z-waarde behorende bij 177 mm.
<br><br>
<span style = "color:blue"> $$z=\frac{x-\mu}{\sigma} = \frac{177-176}{1} = 1$$</span><br>
**d.** Bereken de p-waarde en noteer je antwoord als een percentage met het juiste aantal significante cijfers. De tabel met z-waarden kun je [hier](https://www.ztable.net/) vinden.
<br><br>
<span style = "color:blue"> 

$$P(X< 177) = P(Z< 1) = 0.84134$$ 

Dus de p-waarde is 84%.

</span><br>
**e.** Als we een significantielevel van $$\alpha=5%$$ aannemen. Kun je op grond hiervan de nulhypothese dan verwerpen of niet?
<br><br>
<span style = "color:blue"> De gevonden p-waarde is 84%, dit is groter dan het gekozen significantielevel van 5%. Om deze reden verwerpen we de nulhypothese niet, op grond van het significantielevel van $$\alpha=5\%$$. Hoogstwaarschijnlijk zijn de machines dus niet aan vervanging toe. </span><br>

-----

**4.**
Een vliegtuig heeft op een bepaalde vlucht een gemiddeld brandstofverbruikt van 640 liter. Het brandstofverbruik is normaal verdeeld met een standaardafwijking van 15 liter. De eerste brandstoftank van het vliegtuig bevat 660 liter. Er is ook een reservetank. Bereken de kans dat het vliegtuig tijdens de vlucht brandstof uit de reservetank nodig heeft.
<br><br>
<span style = "color:blue"> De z-waarde behorende bij 660 Liter is:

$$Z=\frac{660-640}{15} = 1.33$$

Wat wordt gevraagd is de kans $$P(X>660)$$ dit is gelijk aan de kans:

$$P(X>660)= 1-P(X< 660) = 1-P(Z<1.33)$$

In de [tabel](https://www.ztable.net/) lezen we $$P(Z<1.33>)$$ af. Hiervoor kijken we in de rij bij '+1.3' en in de kolom '0.03'. Daaruit volgt dat 

$$P(Z<1.33>) = 0.90824$$

Dus

$$\begin{aligned}P(X>660) &= 1-P(X< 660) \\ &= 1-P(Z<1.33) \\ &= 1-0.90824 \\ &= 0.09176\end{aligned}$$

Er is dus een kans van 9.2% dat het vliegtuig zijn reservetank nodig zal hebben.

</span><br>








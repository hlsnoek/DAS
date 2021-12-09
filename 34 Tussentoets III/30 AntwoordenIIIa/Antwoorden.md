# Opgaves bij module 3
Lees goed het [lijstje](/tussentoets-iii/inhoud) door ter voorbereiding voor de tussentoets. Niet voor alle elementen op het lijstje zijn oefenopgaves.

**Let op:** Voor alle opgaven in dit vak geldt dat je bij het noteren van resultaten je moet houden aan de regels. Kijk hiervoor goed naar het stukje 'significantie en notatie' in het hoofdstuk [Notatie](/module-1/notatie).


## Kleinste kwadraten methode

**1** We hebben de volgende meetpunten voor {x,y}: <br>
{2.0,-1.1}, {4.0,-7.2}, {6.0,-13.3} <br>
De onzekerheden op de gemeten waardes y zijn $$\sigma_y = 1.0$$. <br>
De meetwaardes kunnen worden omschreven met de volgende functie:

  $$f(x;a,b) = a+bx$$ waarvan $$a=2.0$$. 
  
Vind de waarde voor $$b$$ die de dataset optimaal beschrijft.


<span style = 'color:blue'>We vinden de optimale waarde voor $$b$$ door de afgeleide van de $$\chi^2$$ op nul te stellen:
$${\displaystyle \frac{\partial \chi^2}{\partial b} = \sum_i^N \frac{1}{\sigma_y^2} \frac{\partial f(x_i;a,b)}{\partial b} \left(y_i - f(x_i;a,b)\right) = 0 }$$ <br>
$$\frac{\partial f(x_i;a,b)}{\partial b} = x$$<br>
geeft met a=2.0:<br>
$${\displaystyle \sum_i^N \frac{1}{1} x_i(y_i - (2.0 + \hat{b} x_i )) = 0}$$<br>
Invullen:
$$(2.0\cdot -1.1 - 2.0\cdot 2.0 - \hat{b} \cdot 2.0^2)$$ +  $$(4.0\cdot -5.4 - 2.0\cdot 4.0 - \hat{b} \cdot 4.0^2) + (6.0\cdot -13.3 - 2.0 \cdot 6.0 - \hat{b} \cdot 6.0^2) = 0$$ geeft $$\hat{b} = -2.35$$</span>

**2** We hebben een dataset met de volgende meetpunten voor {x,y}:<br>
{1.0,3.2}, {2.0,13.3}, {3.0,26.5} met meetonzekerheden $$\sigma_y = 0.5$$<br>
De dataset fitten we met de functie $$y = a\cdot x^2$$. Bereken de optimale waarde voor $$a$$.<br>
<span style = 'color:blue'> $${\displaystyle \frac{\partial \chi^2}{\partial a} = \sum_i^N \frac{1}{\sigma_y^2} \frac{\partial f(x_i;a)}{\partial a} \left(y_i - f(x_i;a)\right) = 0 }$$ <br>
$$\frac{\partial f(x_i;a)}{\partial a} = x^2$$<br>
geeft:<br>
$${\displaystyle \sum_i^N \frac{1}{4} x^2_i(y_i - \hat{a} x_i^2 ) = 0}$$<br>
Invullen:
$$(1.0^2 \cdot 3.2 - \hat{b} \cdot 1.0^3)$$ +  $$(2.0^2 \cdot 13.3 - \hat{b} \cdot 2.0^3) + (3.0^2 \cdot 26.5 - \hat{b} \cdot 3.0^3) = 0$$ geeft $$\hat{b} = 3.0$$</span>


-----


## Chi-2 en AIC
**3** Stel je hebt een dataset met 32 meetwaardes die je fit met de functie $$f(x;a,b,c,d)$$ waarbij je alle vier de variabelen optimaliseert. Hoeveel vrijheidsgraden heeft deze fit?<br>
<span style = 'color:blue'>df =32-4 = 28</span>

-----

**4** Stel je hebt een dataset met 45 meetwaardes gefit met een functie $$f(x;a,b)$$. De $$\chi^2$$ van de fit is bepaald op 98. Is dit een goede fit?<br>
<span style = 'color:blue'>df= 45-2 = 43, $$\chi^2/{df} = 98/43 =2.3$$. Dit is niet een goede fit, het lijkt erop dat de functie de dataset niet goed beschrijft.</span>

----

**5** Stel je hebt een dataset met 14 punten. Je fit deze met een functie $$f=a\cdot x^2$$. De $$\chi^2$$ van de fit is 10. Is dit een goede fit?<br>
<span style = 'color:blue'>df=14-1 = 13. $$\chi^2/{df} = 0.8$$ Dit is een redelijk goede fit.</span>

**6** Stel je hebt een dataset met 14 punten. Je fit deze met een functie $$f1 = a+ b\cdot x$$ en met een functie $$f2 = a+b\cdot x+ c\cdot x^2$$. Voor $$f1$$ vind je een $$\chi^2_{f1} = 15.2$$, voor $$f2$$ vind je een $$\chi^2_{f2} = 16.8$$. Vergelijk de twee fits, welke is het beste? 
<span style = 'color:blue'>Voor $$f1$$: <br>
$$df_1 = 14-2 = 12$$ <br>
$$\chi^2/df_1 = 15.2/12 = 1.3$$<br>
$$AIC_1 = 15.2 + 4 + 12/11 = 20.3$$<br>
Voor $$f2$$:<br>
$$df_2 = 14 -3 = 11$$<br>
$$\chi^2/df_2 = 1.53 $$ <br>
$$AIC_2 = 16.8 + 6 + 24/10 = 25.2$$ <br>
De $$AIC_1$$ is kleiner dan $$AIC_2$$ : fit 1 geeft het beste resultaat.</span>

----

## Hypothese toetsen

**7.** Stel de nulhypothese op bij de gegeven alternatieve hypotheses:<br><br>
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

**8.** 
Bij een zekere stochast vinden we een p-waarde van 3% en we hebben een significantielevel gekozen van 5%.<br><br>
**a.** Is de conclusie 'De nulhypothese is niet correct' een juiste conclusie? is de conclusie 'De alternatieve hypothese is correct' een juiste conclusie? Leg uit waarom wel/niet. Zo niet: hoe zou je deze hypothese anders kunnen formuleren?
<br><br>
<span style = "color:blue">We weten niet wat de echte toestand is van de populatie die onderzocht wordt. Met een steekproef kunnen we de waarde van de eigenschap alleen benaderen. Om deze reden kunnen we nooit zeggen dat de nulhypothese correct dan wel incorrect is. Er bestaat altijd de kans dat de nulhypothese toch correct is zelfs als we hem hebben verworpen op basis van de p-waarde. De conclusie die we in dit geval wel kunnen trekken is dat we de nulhypothese verwerpen op basis van een significantielevel van $$\alpha=5\%$$</span><br>

**b.** Hoe veranderd je conclusie als je een significantielevel van 10% had gekozen of van 1%?
<br><br>
<span style = "color:blue">Als $$\alpha=10\%$$ dan is nog steeds $$p<\alpha$$. De conclusie blijft dat we de nulhypothese verwerpen maar nu op basis van het significantielevel van $$10\%$$. Als $$\alpha=1\%$$ dan is $$p>\alpha$$. Nu trekken we de conclusie dat we de nulhypothese niet verwerpen, op basis van een significantielevel van $$1\%$$.</span><br>

-----

**9.** De productiechef bij een kleurpotlodenfabrikant heeft het vermoeden dat de zaagmachines niet meer zo goed werken. Als de gemiddelde lengte die wordt afgeleverd door de zaagmachines groter of gelijk is aan 177 mm dan zijn de machines aan vervanging toe.

Bij de fabrikant zijn de afgelopen maand 30000 kleurpotloden geproduceert met een gemiddelde lengte van 176 mm en een standaardafwijking van 1 mm. <br><br>

**a.** Stel de alternatieve hypothese op behorende bij dit probleem
<br><br>
<span style = "color:blue"> $$H_{\alpha}:$$ De gemiddelde lengte van kleurpotloden die wordt afgeleverd door de machines is groter of gelijk aan 177 cm</span><br>

**b.** Stel nu de nulhypothese op.
<br><br>
<span style = "color:blue"> $$H_{0}:$$ De gemiddelde lengte van kleurpotloden die wordt afgeleverd door de machines is kleiner dan 177 cm</span><br>

**c.** Bereken de z-waarde behorende bij 177 mm.
<br><br>
<span style = "color:blue"> $$z=\frac{x-\mu}{\sigma} = \frac{177-176}{1} = 1$$</span><br>
**d.** Bereken de p-waarde en noteer je antwoord als een percentage met het juiste aantal significante cijfers. De tabel met z-waarden kun je [hier](https://www.ztable.net/) vinden.
<br><br>
<span style = "color:blue"> $$P(X< 177) = P(Z< 1) = 0.84134$$ 
Dus de p-waarde is 84%.</span><br>

**e.** Als we een significantielevel van $$\alpha=5%$$ aannemen. Kun je op grond hiervan de nulhypothese dan verwerpen of niet?
<br><br>
<span style = "color:blue">De gevonden p-waarde is 84%, dit is groter dan het gekozen significantielevel van 5%. Om deze reden verwerpen we de nulhypothese niet, op grond van het significantielevel van $$\alpha=5\%$$. Hoogstwaarschijnlijk zijn de machines dus niet aan vervanging toe.</span><br>

-----

**10.**
Een vliegtuig heeft op een bepaalde vlucht een gemiddeld brandstofverbruikt van 640 liter. Het brandstofverbruik is normaal verdeeld met een standaardafwijking van 15 liter. De eerste brandstoftank van het vliegtuig bevat 660 liter. Er is ook een reservetank. Bereken de kans dat het vliegtuig tijdens de vlucht brandstof uit de reservetank nodig heeft.
<br><br>
<span style = "color:blue">De z-waarde behorende bij 660 Liter is:<br>
<br>
$$Z=\frac{660-640}{15} = 1.33$$<br><br>
Wat wordt gevraagd is de kans $$P(X>660)$$ dit is gelijk aan de kans:<br><br>
$$P(X>660)= 1-P(X< 660) = 1-P(Z<1.33)$$<br><br>
In de [tabel](https://www.ztable.net/) lezen we $$P(Z<1.33>)$$ af. Hiervoor kijken we in de rij bij '+1.3' en in de kolom '0.03'. Daaruit volgt dat <br><br>
$$P(Z<1.33>) = 0.90824$$<br><br>
Dus <br><br>
$$\begin{aligned}P(X>660) &= 1-P(X< 660) \\ &= 1-P(Z<1.33) \\ &= 1-0.90824 \\ &= 0.09176\end{aligned}$$<br><br>
Er is dus een kans van 9.2% dat het vliegtuig zijn reservetank nodig zal hebben.</span>








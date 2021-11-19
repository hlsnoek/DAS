# Opgaves bij Module 2
Lees goed het [lijstje](/tussentoets-ii/inhoud) door ter voorbereiding voor de tussentoets. Niet voor alle element op het lijstje zijn oefenopgaves.

**Let op:** Voor alle opgaven in dit vak geldt dat je bij het noteren van resultaten je moet houden aan de regels. Kijk hiervoor goed naar het stukje 'significantie en notatie' in het hoofdstuk [Notatie](/module-1/notatie).

## Foutenpropagatie 

**1.**
Als $$y = 2 x + 0.6$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{4 (\Delta x)^2}=2\Delta x}$$</span><br>

-----

**2.**
Als $$y = -3 x + 2  x^2$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${ \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(-3+4x)^2 (\Delta x)^2}= |{-3+4x}| \cdot \Delta x}.$$</span><br>

----

**3.**
Als $$y = \sin(x)$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${ \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(\cos x)^2 (\Delta x)^2}= \cos x \cdot \Delta x}.$$</span><br>

----
**4.**
Als $$y = \frac{1}{x^2}$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${ \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{\left( -\frac{2}{x^3} \right)^2 (\Delta x)^2}= \frac{2}{x^3} \cdot \Delta x}.$$</span><br>


----
**5.**
Als $$E = mc^2$$ en de fouten op ($$m$$,$$c$$) zijn ($$\Delta m$$,$$\Delta c$$), wat is dan de fout op $$E$$? <br><br>
<span style = "color:blue"> $$ \Delta E = \sqrt{\left(\frac{\partial E}{\partial m}\right)^2 (\Delta m)^2 + \left(\frac{\partial E}{\partial c}\right)^2 (\Delta c)^2 } = \sqrt{(c)^2(\Delta m)^2 + (2mc)^2 (\Delta c)^2}.$$</span>


----
**6.** 
Stel je wil de kinetische energie berekenen van een object. De formule is $$E_k = 1/2 m \cdot v^2$$. Je meet de massa van het object, deze is $$m=2.3 \pm 0.2$$ kg. De snelheid is $$v=0.20 \pm 0.05$$ m/s. <br>
Bereken de kinetische energie.<br>
<span style = 'color:blue'> $${E_k = 1/2 m \cdot v^2 = 0.046}$$ J<br>
$$\Delta E_k = \sqrt{\frac{\partial E_k}{\partial m})^2 ( \Delta m)^2 + \left(\frac{\partial E_k}{\partial v}\right)^2 \left( \Delta v \right)^2} = \sqrt{\left( \frac{1}{2}v^2 \Delta m\right)^2 + \left( mv \Delta m \right)^2 } = 0.02$$<br>
$$E_k =  0.046 \pm 0.02$$ J</span>

## De Wet van Grote aantallen

**7.**
We hebben een dataset met de gemeten massa van 80 kogels. Het gemiddelde van de massa-distributie is bepaald op 108.2 kg. De standaardafwijking van de massa-distributie is 11.2 kg. Wat is de fout op het berekende gemiddelde?<br>
<span style = 'color:blue'>De fout (onzekerheid) op het bepaalde gemiddelde is gelijk aan:<br>
$${ \Delta \mu = \frac{\sigma}{\sqrt{N}} = \frac{11.2}{\sqrt{80}}} \text{ kg} = 1.25\text{ kg}$$</span>

-----
**8.**
We combineren onafhankelijke datasets waarbij de spanwijdte van koolmeesjes zijn gemeten. Dataset A heeft informatie over 1100 koolmeesjes met een gemiddelde spanwijdte van 13.4 cm met een standaardafwijking van 2.0 cm. Dataset B heeft informatie over 2000 koolmeesjes met gemiddelde van 14.0 cm en een standaardafwijking van 1.8 cm.<br>
Wat is het gemiddelde van de gecombineerde dataset T?<br>
<span style = 'color:blue'> $${ \mu_A = \sum_a^{N_A=1100} \frac{x_a}{N_A} \text{ en } \mu_B = \sum_b^{N_B=2000} \frac{x_b}{N_B} \text{ ook geldt: }  \mu_T = \frac{\sum^{N_A} x_a + \sum^{N_B} x_b}{N_T}}$$<br>
$${ \mu_T =  \frac{N_A \cdot \mu_A + N_B \cdot \mu_B}{N_A + N_B}} = 13.8 \text{ kg}$$</span><br>

----
**9.**
Onder welke voorwaarde mogen we aannemen dat de onzekerheid op het berekende gemiddelde van een dataset kleiner wordt als we datapunten toevoegen?<br>
<span style = 'color:blue'>Dat mogen we doen als voor de onderliggende verdeling van de dataset een goed gedefinieerde variantie bestaat.</span>

---
**10.**
We hebben een dataset met metingen van een grootheid $$x$$ met precies 16 punten. Het gemiddelde waarde van $$\mu = 22$$ met een standaardafwijking van $$\sigma = 4 $$. <br>
**a.** Wat is de onzekerheid op het gemiddelde van deze dataset?<br>
<span style = 'color:blue'>De onzekerheid is: $$\sigma_\mu (=\Delta \mu)= \frac{\sigma}{\sqrt{N}} = 4/\sqrt{16} = 1 $$</span><br>
**b.** We voegen nog 9 extra waardes aan onze dataset toe. Wat is de onzekerheid op het gemiddelde nu?<br>
<span style = 'color:blue'>De onzekerheid is: $$\sigma_\mu (=\Delta \mu)= \frac{\sigma}{\sqrt{N}} = 4/\sqrt{25} = 0.8 $$</span><br>

## Meerdimensionale data
**11.**
Je hebt de volgende dataset met waardes van x en y: <br>
<center>{2,5}, {1,4}, {5,2}, {3,0} </center><br>
**a.** Bereken de covariantie.<br>
<span style = 'color:blue'> $$<{x}> = (2+1+5+3)/4 = 2.75$$ <br>
$$<{y}> = (5+4+2+0)/4 = 2.75$$<br>
$$\text{cov}(xy) = \frac{1}{n} \sum_n (x_i-<{x}>)\cdot (y_i - <{y}>) = $$<br>
$$\frac{1}{4}\cdot ((2-2.75)\cdot(5-2.75)  
+(1-2.75)\cdot(4-2.75)+(5-2.75)\cdot(2-2.75) +(3-2.75)\cdot(0-2.75)) $$ 
$$ = -1.6$$</span><br>
**b.** Bereken de correlatie.<br>
<span style = 'color:blue'> $$\sigma_x^2 = <{x^2}>-<{x}>^2 = (4+1+25+9)/4 - 2.75^2 = 2.1875$$ <br>
$$\sigma_y^2 = <{y^2}>-<{y}>^2 = (25+16+4+0)/4 - 2.75^2 = 3.6875$$ <br>
$$\sigma_x = 1.48$$, $$\sigma_y = 1.48$$
$$\rho = \frac{\text{cov}_{xy}}{\sigma_x \sigma_y} = \frac{-1.56}{1.48\times 1.92} = -0.55$$</span><br>

---

**12.**
Je hebt de volgende dataset met waardes van x en y: <br>
<center>{1,0}, {3,4}, {2,6}, {4,8} </center><br>
**a.** Bereken de covariantie.<br>
<span style = 'color:blue'>$$<{x}> = 2.5$$ <br>
$$<{y}> = 4.5$$<br>
$$\text{cov}(xy) = \frac{1}{n} \sum_n (x_i-<{x}>)\cdot (y_i - <{y}>) = 2.75$$<br></span><br>
**b.** Bereken de correlatie.<br>
<span style = 'color:blue'> $$\sigma_x^2 = <{x^2}>-<{x}>^2 = 1.118^2$$<br>
$$\sigma_y^2 = <{y^2}>-<{y}>^2 = 2.958^2$$<br>
$$\rho = \frac{\text{cov}_{xy}}{\sigma_x \sigma_y} = \frac{2.75}{1.118\times 2.958} = 0.83$$</span><br>


## Extra kansrekenregels 
**13.** 
Op een zomerse avond zie je rook en waar rook is is vuur. Op een zomerse avond is de kans dat je rook ziet (10%), meestal door gebruik van barbeques. Gevaarlijke branden zijn heel zeldzaam (1%) de kans dat rook bij een gevaarlijke brand vrijkomt is groot (90%). Wat is de kans dat de rook die je ziet van een een gevaarlijk brand afkomt?<br>

<span style = 'color:blue'>Gebruik Bayes theorema om dit uit te rekenen.<br>
$${ \text{P(gevaarlijke brand \mid rook)} = \frac{\text{P(rook \mid gevaarlijke brand)}\cdot{\text{P(gevaarlijke brand)}}}{\text{P(rook)}} = \frac{0.9 \times 0.01}{0.10} = 0.09}$$<br></span>

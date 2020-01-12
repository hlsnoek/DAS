#Oefenopgaves als voorbereiding voor tussentoets 2
Lees goed het [lijstje](/tussentoets-ii/inhoud) door ter voorbereiding voor de tussentoets. Niet voor alle element op het lijstje zijn oefenopgaves.

**Let op:** Voor alle opgaven in dit vak geldt dat je bij het noteren van resultaten je moet houden aan de regels. Kijk hiervoor goed naar het stukje 'significantie en notatie' in het hoofdstuk [Meetonzekerheid](/blok-1/meetonzekerheid).

### Foutenpropagatie 

**1.**
Als $$y = 2 x + 0.6$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{4 (\Delta x)^2}=2\Delta x}$$</span><br>

-----

**2.**
Als $$y = -3 x + 2  x^2$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(-3+4x)^2 (\Delta x)^2}= |{-3+4x}| \cdot \Delta x}.$$</span><br>

----

**3.**
Als $$y = \sin(x)$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(\cos x)^2 (\Delta x)^2}= \cos x \cdot \Delta x}.$$</span><br>

----
**4.**
Als $$y = \frac{1}{x^2}$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{\left( -\frac{2}{x^3} \right)^2 (\Delta x)^2}= \frac{2}{x^3} \cdot \Delta x}.$$</span><br>

----
**5.**
Als $$E = mc^2$$ en de fouten op ($$m$$,$$c$$) zijn ($$\Delta m$$,$$\Delta c$$), wat is dan de fout op $$E$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta E = \sqrt{\left(\frac{\partial E}{\partial m}\right)^2 (\Delta m)^2 + \left(\frac{\partial E}{\partial c}\right)^2 (\Delta c)^2 } = \sqrt{(c)^2(\Delta m)^2 + (2mc)^2 (\Delta c)^2}}.$$</span>

----
**6.**
Als $$E = mc^2$$ en de fouten op ($$m$$,$$c$$) zijn ($$\Delta m$$,$$\Delta c$$), wat is dan de fout op $$E$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta E = \sqrt{\left(\frac{\partial E}{\partial m}\right)^2 (\Delta m)^2 + \left(\frac{\partial E}{\partial c}\right)^2 (\Delta c)^2 } = \sqrt{(c)^2(\Delta m)^2 + (2mc)^2 (\Delta c)^2}}.$$</span>

----
**7.** 
Stel je wil de kinetische energie berekenen van een object. De formule is $$E_k = 1/2 m \cdot v^2$$. Je meet de massa van het object, deze is $$m=2.3 \pm 0.2$$ kg. De snelheid is $$v=0.20 \pm 0.05$$ m/s. <br>
Bereken de kinetische energie.<br>
<span style = 'color:blue'> $$\displaystyle{E_k = 1/2 m \cdot v^2 = 0.046}$$ J<br>
$$\displaystyle{ \Delta E_k = \sqrt{\left(\frac{\partial E_k}{\partial m}\right)^2 \left( \Delta m\right)^2 + \left(\frac{\partial E_k}{\partial v}\right)^2 \left( \Delta v \right)^2} = \sqrt{\left( \frac{1}{2}v^2 \Delta m\right)^2 + \left( mv \Delta m \right)^2 } = 0.02}$$<br>
$$E_k =  0.046 \pm 0.02$$ J</span>

### De Wet van Grote aantallen

**8.**
We hebben een dataset met de gemeten massa van 80 kogels. Het gemiddelde van de massa-distributie is bepaald op 108.2 kg. De standaard deviatie van de massa-distributie is 11.2 kg. Wat is de fout op het berekende gemiddelde?<br>
<span style = 'color:blue'> De fout (onzekerheid) op het bepaalde gemiddelde is gelijk aan:<br>
$${\displaystyle \Delta \mu = \frac{\sigma}{\sqrt{N}} = \frac{11.2}{\sqrt{80}}} \text{ kg} = 1.25\text{ kg}$$ </span>

-----
**9.**
We combineren onafhankelijke datasets waarbij de spanwijdte van koolmeesjes zijn gemeten. Dataset A heeft informatie over 1100 koolmeesjes met een gemiddelde spanwijdte van 13.4 cm met een standaard deviatie van 2.0 cm. Dataset B heeft informatie over 2000 koolmeesjes met gemiddelde van 14.0 cm en een standaard deviatie van 1.8 cm.<br>
Wat is het gemiddelde van de gecombineerde dataset T?<br>
<span style = 'color:blue'> $${\displaystyle \mu_A = \sum_a^{N_A=1100} \frac{x_a}{N_A} \text{ en } \mu_B = \sum_b^{N_B=2000} \frac{x_b}{N_B} \text{ ook geldt: }  \mu_T = \frac{\sum^{N_A} x_a + \sum^{N_B} x_b}{N_T}}$$<br>
$${\displaystyle \mu_T =  \frac{N_A \cdot \mu_A + N_B \cdot \mu_B}{N_A + N_B}} = 13.79 \text{ kg}$$  </span><br>

----
**10.**
Onder welke voorwaarde mogen we aannemen dat de onzekerheid op het berekende gemiddelde van een dataset kleiner wordt als we datapunten toevoegen?<br>
<span style = 'color:blue'> Dat mogen we doen als voor de onderliggende verdeling van de dataset een goed gedefinieerde variantie bestaat.</span>

---
**11.**
We hebben een dataset met metingen van een grootheid $$x$$ met precies 16 punten. Het gemiddelde waarde van $$\mu = 22$$ met een standaard deviatie van $$\sigma = 4 $$. <br>
**a.** Wat is de onzekerheid op het gemiddelde van deze dataset?<br>
<span style = 'color:blue'>De onzekerheid is: $$\sigma_\mu (=\Delta \mu)= \frac{\sigma}{\sqrt{N}} = 4/\sqrt{16} = 1 $$</span><br>
**b.** We voegen nog 9 extra waardes aan onze dataset toe. Wat is de onzekerheid op het gemiddelde nu?<br>
<span style = 'color:blue'>De onzekerheid is: $$\sigma_\mu (=\Delta \mu)= \frac{\sigma}{\sqrt{N}} = 4/\sqrt{25} = 0.8 $$</span><br>

### Meerdimensionale data
**12.**
<span style = 'color'blue'> </span><br>

### Extra kansrekenregels 

<span style = 'color'blue'> </span><br>
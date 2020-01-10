#Voorbeeld opgaves tussentoets II

----

Foutenpropagatie: 
Sommetjes met foutenpropagatie.
Afronden van getallen bij foutenpropagatie

Grote aantallen
De afleiding kennen van de wortel N wet.
De wortel N wet kunnen toepassen.
De wet van grote aantallen kennen en kunnen toepassen.
(ook de voorwaardes kennen van de wet van grote aantallen)


Meerdimensionale data
De covariantie definitie kennen.
de covariantie van een dataset met twee variabelen kunnen uitrekenen
De formule van de correlatie kennen 
De correlatie tussen twee waardes in een dataset kunnen uitrekenen


Extra Kansrekenregels
Alle kansrekenregels (ook uit blok 1) paraat hebben en kunnen toepassen.
De wiskundige notaties $$(A \cap B)$$, $$(A \cup B)$$ en $$(A|B)$$ begrijpen.
Bayes theorema kennen en kunnen toepassen


<span style = "color:blue"> </span><br>


#Oefenopgaves als voorbereiding voor tussentoets 2
Lees goed het [lijstje](/tussentoets-ii/inhoud) door ter voorbereiding voor de tussentoets. Niet voor alle element op het lijstje zijn oefenopgaves.

**Let op:** Voor alle opgaven in dit vak geldt dat je bij het noteren van resultaten je moet houden aan de regels. Kijk hiervoor goed naar het stukje 'significantie en notatie' in het hoofdstuk [Meetonzekerheid](/blok-1/meetonzekerheid).

## Foutenpropagatie 

**1**
Als $$y = 2 x + 0.6$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{4 (\Delta x)^2}=2\Delta x}$$</span><br>

-----

**2**
Als $$y = -3 x + 2  x^2$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(-3+4x)^2 (\Delta x)^2}= |{-3+4x}| \cdot \Delta x}.$$</span><br>

----

**3**
Als $$y = \sin(x)$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{(\cos x)^2 (\Delta x)^2}= \cos x \cdot \Delta x}.$$</span><br>

----
**4**
Als $$y = \frac{1}{x^2}$$ en de fout op $$x$$ is $$\Delta x$$, wat is dan de fout op $$y$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta y = \sqrt{\left(\frac{\partial y}{\partial x}\right)^2 (\Delta x)^2 } = \sqrt{\left( -\frac{2}{x^3} \right)^2 (\Delta x)^2}= \frac{2}{x^3} \cdot \Delta x}.$$</span><br>

----
**5**
Als $$E = mc^2$$ en de fouten op ($$m$$,$$c$$) zijn ($$\Delta m$$,$$\Delta c$$), wat is dan de fout op $$E$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta E = \sqrt{\left(\frac{\partial E}{\partial m}\right)^2 (\Delta m)^2 + \left(\frac{\partial E}{\partial c}\right)^2 (\Delta c)^2 } = \sqrt{(c)^2(\Delta m)^2 + (2mc)^2 (\Delta c)^2}}.$$</span>

----
**6**
Als $$E = mc^2$$ en de fouten op ($$m$$,$$c$$) zijn ($$\Delta m$$,$$\Delta c$$), wat is dan de fout op $$E$$? <br><br>
<span style = "color:blue"> $${\displaystyle \Delta E = \sqrt{\left(\frac{\partial E}{\partial m}\right)^2 (\Delta m)^2 + \left(\frac{\partial E}{\partial c}\right)^2 (\Delta c)^2 } = \sqrt{(c)^2(\Delta m)^2 + (2mc)^2 (\Delta c)^2}}.$$</span>

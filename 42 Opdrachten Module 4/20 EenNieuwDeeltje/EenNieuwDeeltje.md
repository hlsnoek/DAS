# M4.1 Een Nieuw Deeltje \*\*\*

We gaan op zoek naar een nieuw elementair deeltje $$X$$. Dit deeltje is gepostuleerd door een groep Natuurkundigen die daarmee het bestaan van de Donkere Materie in het heelal denken te kunnen verklaren. 

We kunnen het deeltje misschien maken bij botsingen bij de Large Hadron Collider op het [CERN](http://www.cern.ch) onderzoekscentrum. Als deze deeltjes $$X$$ bestaan dan zouden we dit moeten kunnen zien in de gereconstrueerde massaverdeling van de restproducten van de $$X$$-deeltjes in een heel precies geselecteerde dataset. 

We hebben een beschrijving van de data zoals hij eruit zou zien *zonder* het bestaan van het deeltje, dit noemen we de achtergrond data. En we weten hoe de fluctuatie eruit zou zien als er *wel* $$X$$-deeltjes zouden bestaan. 
Alleen hebben de theoreten geen enkel idee van de exacte massa is van het $$X$$ deeltje. We gaan in een massagebied de p-waarde scannen door deze voor elk punt te berekenen en kijken of we een significante afwijking vinden. 

In het vakgebied van de deeltjesfysica hanteren we de volgende normen: 

| z-waarde | p-waarde | statement |
|---|---|---|
| $$\geq$$ 3 $$\sigma$$ | $$\leq 0.003$$ |  observatie van afwijking|
| $$\geq$$ 5 $$\sigma$$ | $$\leq 1/(3.5 \cdot 10^6$$) | ontdekking|

<br>

> - **M4.1a) Wat is H0 en wat is de H1 hypothese in dit onderzoek? Postuleer de hele stelling.**

Haal de dataset op met het volgende statement

	m,events,events_err = ds.DeeltjesDataset()
	
De drie `list`'s die worden teruggegeven zijn:
	
	m - de berekende massa van de restproducten uitgedrukt in proton massa's [pm] 
	events - het aantal botsingen in de geselecteerde data
	events_err - de onzekerheid op het aantal events
	
	
Het aantal *events* (evenementen) is het geobserveerde aantal botsingen die aan de voorwaardes van de dataselectie voldoet. De data selectie zoekt tussen alle botsingen die we waarnemen met de detector de botsingen uit die specifieke kenmerken vertonen die we verwachten te zien als er Donkere Materie deeltjes zijn gemaakt in die specifieke botsing. Die noemen we ook wel een voorselectie van de data. 
	
De achtergrond data wordt beschreven met de volgende functie: 

$$\displaystyle f(m;N_0,c) = N_0 \cdot \left( \frac{1}{2} \right)^{m/c}$$

De massaverdeling van deeltje $$X$$ ziet er zo uit: 

$${\displaystyle g(m;m_0,\sigma, N_X) = N_X \cdot \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}(\frac{m-m_0}{\sigma})^2}}$$

We weten niet wat de waarde is van $$m_0$$ en ook niet hoeveel $$X$$-deeltjes we zouden kunnen hebben in onze dataset ($$N_X$$). Wel kennen   we de resolutie van onze meting ($$\sigma=5$$ [pm]) bepaald. Hiermee bedoelen we dat we op de massapiek van het $$X$$ deeltje een spreiding verwachten van ($$\sigma=5$$ [pm]).
De eenheid van $$m$$ drukken 
we uit in het aantal proton massa's omdat het anders wel onhandig wordt met de eenheid (1 proton massa is gelijk aan $$1.6726 \times 10^{-27}$$ kg).

> - **M4.1b) Zet eerst een fit op waarbij je alleen de achtergrond fit.  Maak een grafiek waarbij je de datapunten, de onzekerheden op de datapunten en de gefitte curve laat zien.**<br><br>
> 
> - **M4.1c) Hoeveel vrijheidsgraden, $$df$$ heeft deze fit?**<br><br>
> 
> - **M4.1d) Wat is de $$\chi^2$$ en de $$\chi^2$$/df voor deze fit?**
>

Nu gaan we een zogeheten p-waarde scan uitvoeren. Lees eerst de theorie van [Hypothese toetsen II](/module-4/hypothese-toetsen-2). Hiervoor fitten we het totaal van de achtergrondfunctie $$f$$ plus de functie die deeltje $$X$$ beschrijft $$g$$ aan de data. We kiezen steeds een waarde van $$m_0$$ en laten alleen de volgende parameters vrij in de fit: $$N_0, c$$ en $$N_x$$. De andere parameter $$\sigma$$ wordt vastgezet op 5 en $$m_0$$ wordt steeds op een andere gekozen waarde gefixeerd in **het gehele gebied die door de dataset wordt beschreven met stapjes van 1 proton massa**.

> - **M4.1c) Fit nu voor elke integer waarde van $$m_0$$ in het massagebied van $$m$$ de functie en bereken de $$\chi^2$$ van de fit met de totale functie ($$f+g$$).**<br><br>
> 
> - **M4.1d) Hoeveel vrijheidsgraden heeft deze totale fit?**
> * **TIP:** Als het helemaal niet lukt kun je even spieken wat de waarde is van $$m_0$$ door de volgende functie aan te roepen: 
> 		
> 		ds.SpiekenM0()
>
> Zorg dan eerst dat je de fit aan de praat krijgt voor die massa waarde. Let je goed op de startwaardes van de fit?


Voor elke waarde van $$m_0$$ kunnen we nu het verschil in $$\chi^2$$ tussen de achtergrond en de achtergrond+signaal fit uitrekenen. Dit verschil noteren we als: 

$${\displaystyle \Delta \chi^2 = \chi^2_{f} - \chi^2_{f+g}}$$

Deze $$\Delta \chi^2$$ kunnen we omrekenen naar een p-waarde. Lees hierover meer in het hoofdstuk [Hypothese toetsen II](/module-4/hypothese-toetsen-2). We kunnen de p-waarde nu berekenen met behulp van de berekende $$\Delta \chi^2$$.

Gebruik de volgende functie uit het scipy.stats pakket om de p-waarde te berekenen: 

  		from scipy import stats
		p_value = stats.chi2.sf(Delta_chisquare, 1)

Je kan nu ook de z-waarde uitrekenen op de volgende manier: 

	    z_waarde = -stats.norm.ppf(p_value)

> - **M4.1e) Bereken voor elke waarde van $$m_0$$ nu de p-waarde en representeer deze in een grafiek.** <br> 
> **Tip:** Gebruik hiervoor de volgende plot opties om de grafiek duidelijker te maken: 
> 
>			plt.yscale('log')
>			plt.grid(True)
>
> - **M4.1f) Bij welke waarde van $$m_0$$ vind je de beste p-waarde in jouw massa gebied?**<br><br>
> 
> - **M4.1g) Maak voor een grafiek met de dataset en de gefitte functies (achtergrond en achtergrond+signaal) voor deze waarde van $$\hat{m}_0$$.**<br><br>
> 
> - **M4.1h) Bereken voor $$\hat{m}_0$$ de p-waarde en de z-waarde.**<br><br>
> 
> - **M4.1i) Denk je dat je de achtergrond hypothese kunt verwerpen. Zo ja, redeneer waarom. Zo nee redeneer waarom niet.**

Voor al je resultaten in op je template en lever het samen met de resultaten van de andere opdracht in.
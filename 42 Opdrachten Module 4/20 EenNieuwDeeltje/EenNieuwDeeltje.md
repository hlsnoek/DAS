# M4.1 Een Nieuw Deeltje \*\*\*

We gaan op zoek naar een nieuw elementair deeltje $$X$$. Dit deeltje is gepostuleerd door een groep Natuurkundigen die daarmee het bestaan van de [Donkere Materie](https://nl.wikipedia.org/wiki/Donkere_materie) in het heelal denken te kunnen verklaren. 

We kunnen het deeltje misschien maken bij botsingen bij de Large Hadron Collider op het [CERN](http://www.cern.ch) onderzoekscentrum. Als deze deeltjes $$X$$ bestaan dan zouden we dit moeten kunnen zien in de gereconstrueerde massaverdeling van de restproducten van de $$X$$-deeltjes in een heel precies geselecteerde dataset. 

We hebben een beschrijving van de massaverdeling eruit zou zien *zonder* het bestaan van het deeltje, dit noemen we de achtergrond. En we weten hoe een massaverdeling eruit zou zien als er *wel* $$X$$-deeltjes zouden bestaan. 
Alleen hebben de theoreten geen enkel idee van de exacte massa is van het $$X$$ deeltje. We gaan in een massagebied de p-waarde scannen door deze voor elk punt te berekenen en kijken of we een significante afwijking vinden. 

In het vakgebied van de deeltjesfysica hanteren we de volgende normen: 

| z-waarde | p-waarde | statement |
|---|---|---|
| $$\geq$$ 3 $$\sigma$$ | $$\leq 0.003$$ |  observatie van afwijking|
| $$\geq$$ 5 $$\sigma$$ | $$\leq 2.87 \times 10^{-07}$$ | ontdekking|

<br>

> - **M4.1a) Wat is $$H_0$$ en wat is de $$H_1$$ hypothese in dit onderzoek? Postuleer de hele stelling.**

Haal de dataset op met het volgende statement

	m,events,events_err = ds.DeeltjesDataset()
	
De drie `list`'s die worden teruggegeven zijn:
	
	m - de berekende massa van de restproducten uitgedrukt in proton massa's (pm)
	events - het aantal botsingen in de geselecteerde data
	events_err - de onzekerheid op het aantal events
	
	
Het aantal *events* (aantal evenementen) is het geobserveerde aantal botsingen die aan de voorwaardes van de dataselectie voldoet. De data selectie zoekt tussen alle botsingen die we waarnemen met de detector de botsingen uit die specifieke kenmerken vertonen die we verwachten te zien als er Donkere Materie deeltjes zijn gemaakt in die specifieke botsing. Die noemen we ook wel een voorselectie van de data. 
	
De achtergrond data wordt beschreven met de volgende functie: 

$$\displaystyle f(m;N_0,c) = N_0 \cdot \left( \frac{1}{2} \right)^{m/c}$$

De massaverdeling van deeltje $$X$$ ziet er zo uit: 

$${\displaystyle g(m;m_0,\sigma, N_X) = N_X \cdot \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}(\frac{m-m_0}{\sigma})^2}}$$

We weten niet wat de waarde is van $$m_0$$ en ook niet hoeveel $$X$$-deeltjes we zouden kunnen hebben in onze dataset ($$N_X$$). Wel kennen   we de resolutie van onze meting ($$\sigma=5$$ pm) bepaald. Hiermee bedoelen we dat we op de massapiek van het $$X$$ deeltje een spreiding verwachten van ($$\sigma=5$$ pm).
De eenheid van $$m$$ drukken 
we uit in het aantal proton massa's omdat het anders wel onhandig wordt met de eenheid (1 proton massa is gelijk aan $$1.6726 \times 10^{-27}$$ kg).

We gaan weer fitten met het pakket [**lmfit**](https://lmfit.github.io/lmfit-py/model.html).

> - Schrijf eerst een functie die je **`achtergrond_functie(x,N0,c)`** noemt. Het is misschien logischer om in plaats de  `x` variabele `m` te gebruiken, maar later in het programma maken we gebruik van een standaard functie van `models` en hiervoor is het nodig om het nu alvast `x` te noemen. Het model noemen we `achtergrond_model`. 
> 
> 			achtergrond_model = models.Model(achtergrond_functie)
> 
> <br><br>
>   
> - **M4.1b) Zet eerst een fit op waarbij je alleen de achtergrond fit.  Maak een grafiek waarbij je de datapunten, de onzekerheden op de datapunten en de gefitte curve laat zien.**<br><br>
> **Tip 1.** Zoals je ziet lijkt de functie erg op de functie die gefit moest worden in opgave M3.2, je kan een deel van je code dus hergebruiken. <br>
> **Tip 2.** Het is voor deze fit erg belangrijk om de startwaardes goed mee te geven. Bekijk eerst eens de data goed en probeer af te schatten welke startwaardes voor `N0` en `c` je moet meegeven. De functie met startwaardes kun je op de volgende manier visualiseren. (Hiervoor moet je wel eerst het fit statement hebben uitgevoerd maar ook als de fit niet goed werkt zie je nog steeds of de startwaardes goed zijn ingeschat.)
>   
> 			plt.plot(m, result.init_fit, 'k--', label='initial fit')
> 
> 
> - **M4.1c) Hoeveel vrijheidsgraden, $$df$$ heeft deze fit?**<br><br>
> 
> - **M4.1d) Wat is de $$\chi^2$$ en de $$\chi^2/df$$ voor deze fit?**
>

Zoals je ziet wordt de massaverdeling van deeltje $$X$$ beschreven met een normaalverdeling. Deze normaalverdeling ligt, als het deeltje bestaat, als het ware op de achtergrond. We zullen dus een model moeten programmeren die de som is van de normaal verdeling die het 'signaal' beschrijft en de achtergrond functie. 

> - De functie die de massaverdeling van het deeltje $$X$$ beschrijft is een normaalverdeling. We kunnen hiervoor een eigen functie programmeren maar we kunnen ook gebruik maken van de standaard functies die het **`lmfit`** pakket bevat. Deze kunnen we aanroepen met:
> 
> 			normaal_model = models.GaussianModel()
> 

Als je een standaardfunctie gebruikt is het altijd even goed om uit te zoeken hoe die precies werkt. Je kan bijvoorbeeld even op de website van [lmfit](https://lmfit.github.io/lmfit-py/builtin_models.html) kijken en zoeken naar **`GaussianModel()`**. We bekijken in elk geval even hoe de vrije parameters en de variabele heten in dit model. Dit kun je doen met het volgende statement.

			print('De paramaters: ',normaal_model.param_names,' de variabele: ', normaal_model.independent_vars)

 We zien nu dat er drie variabelen zijn **`amplitude`**, **`center`** en **`sigma`**. Vergelijk de functie op de website met de normale verdeling voor het deeltje $$X$$. We zien nu dat de variabele **`x`** de variabele $$m$$ is. <br>

Met de informatie die we hierboven gegeven hebben weten we dat we een van deze parameters (namelijk de standaarddeviatie van de normaalfunctie) moeten *fixeren*. We bedoelen hiermee dat deze niet een vrije parameter in de fit mag zijn, hij moet constant worden gehouden in de optimalisatie van de $$\chi^2$$. <br>
We kunnen een parameter fixeren met het volgende statement: 
 
 			signaal_model.set_param_hint(par_name, vary=False)
 
waarbij `par_name` dus de naam van de variabele is waarvoor we dat willen doen. 
 
> - We gaan nu model voor het signaal maken dat dus bestaat uit de achtergrond component en de normaal component: 
> 
>  
>			 signaal_model = normaal_model + achtergrond_model
> 


We zijn nu klaar om de zogeheten p-waarde scan uitvoeren. Lees eerst de theorie van [Hypothese toetsen II](/module-4/hypothese-toetsen-2).  We kiezen steeds een waarde van $$m_0$$ en laten alleen de volgende parameters vrij in de fit: $$N_0, c$$ en $$N_x$$. De andere parameter $$\sigma$$ wordt vastgezet op 5 en $$m_0$$ wordt steeds op een andere gekozen waarde gefixeerd in **het gehele gebied die door de dataset wordt beschreven met stapjes van 1 proton massa**.


> - Fit nu voor elke integer waarde van $$m_0$$ in het massagebied van $$m$$ de functie en bereken de $$\chi^2$$ van de fit met het signaal model. Controleer of alle parameters die moeten worden gefixeerd in de fit, dat ook daadwerkelijk zijn. Kijk hiervoor naar het fit resultaat.<br><br>
> 	**Tip 1:** Zorg dat je de juiste startwaardes meegeeft.<br>
>  **Tip 2:** Je kunt de $$\chi^2$$ opvragen van het fit resultaat met het statement: 
> 			result.chisqr
>	
>  
> - **M4.1fe) Hoeveel vrijheidsgraden heeft deze totale fit? Schrijf de formule helemaal uit.**


Voor elke waarde van $$m_0$$ kunnen we nu het verschil in $$\chi^2$$ tussen de fit met het achtergrond model en het de $$\chi^2$$ en de fit van het signaal model bij die waarde van $$m_0$$. Dit verschil noteren we als: 

$${\displaystyle \Delta \chi^2 = \chi^2_{a} - \chi^2_{s}}$$

Waarbij Deze $$\Delta \chi^2$$ kunnen we omrekenen naar een p-waarde. Lees hierover meer in het hoofdstuk [Hypothese toetsen II](/module-4/hypothese-toetsen-2). We kunnen de p-waarde nu berekenen met behulp van de berekende $$\Delta \chi^2$$.

> - Gebruik de volgende functie uit het scipy.stats pakket om de p-waarde te berekenen: 
> 
>  			from scipy import stats
>			p_value = stats.chi2.sf(Delta_chisquare, 1)
>

>
> - **M4.1f) Bereken voor elke waarde van $$m_0$$ nu de p-waarde en representeer deze in een grafiek waarbij je de p-waarde uitzet tegen $$m_0$$.** <br> 
> **Tip:** Gebruik hiervoor de volgende plot opties om de grafiek duidelijker te maken: 
> 
>			plt.yscale('log')
>			plt.grid(True)
>
> - **M4.1g) Bij welke waarde van $$m_0$$ vind je de beste p-waarde in jouw massa gebied?**<br><br>
> 
> - **M4.1h) Maak een grafiek met de dataset en de gefitte modellen (achtergrond en signaal) voor deze waarde van $$\hat{m}_0$$.**<br><br>
> 
> 
> - **M4.1i) Bereken voor $$\hat{m}_0$$ de p-waarde en de z-waarde. De z-waarde kun je met het volgende statement uitrekenen:**
>
>		    z_waarde = -stats.norm.ppf(p_waarde)
>
>
> - **M4.1j) Denk je dat je de achtergrond hypothese kunt verwerpen. Zo ja, redeneer waarom. Zo nee redeneer waarom niet. Kijk even naar de afspraken die hierover zijn gemaakt in de deeltjefysica.**


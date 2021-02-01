## M3.2 Halfwaardedikte III \*\*\*

In opgave M2.3 hebben we gezien dat de meetmethode die we gebruikten om de halfwaardedikte te bepalen niet optimaal was. Er was zeker sprake van een onzuivere meting doordat we stelselmatig een te hoge waarde van $${d_{half}}$$ terugkregen. 

In deze opgave zullen we zien dat de onzuiverheid te maken heeft met de methode waarop we de halfwaardedikte hebben bepaald. Het heeft niets te maken met de opstelling van de meting of met de verzamelde datapunten. Het is de analyse techniek die zorgt voor de onzuiverheid.

In deze opdracht gaan we een fit gebruiken om de waarde van $$d_{half}$$ te achterhalen. In opdracht M3.1 hebben we onze eigen lineaire regressie methode geprogrammeerd met behulp van de kleinste kwadraten methode. In deze opdracht gebruiken we een fit pakket **`lmfit`**. Dit programma rekent de $$\chi^2$$ uit en minimaliseert deze voor ons. Dat scheelt op zich een hoop werk, maar je zal in deze opdracht zien dat het toch ook weer niet helemaal vanzelf gaat. 

Om dit fit pakket te kunnen gebruiken moet het volgende import statement gebruiken: 

	from lmfit import models

Maak nu een dataset aan met de standaard waardes zoals je dat in M2.3 ook hebt gedaan: 

	counts, diktes, dtrue = ds.DataSetHalfwaardeDikteVariatie()


<!--
Maak nu een lijst aan met de fouten op de counts.
We gaan nu de fit opzetten. De roep je op deze manier aan: 

	par_opt, par_cov = curve_fit(functie,diktes,counts,sigma=N_err,p0=start,absolute_sigma=True)

Je ziet dat de functie **`curve_fit`** verschillende opties nodig heeft en twee variabelen teruggeeft. We gaan even door het lijstje.

	functie : is de functie die de relatie tussen diktes en counts beschrijft
	diktes : de lijst met waardes langs de horizontale as
	counts : de lijst met waardes langs de verticale as
	sigma=N_err : N_err is de lijst met onzekerheden op de counts
	p0=start : de start parameters voor de fit in dezelfde volgorde as in f
	absolute_sigma=True : de fit gaat de opgegeven foutenvlaggen gebruiken
	par_opt : de lijst met geoptimaliseerde parameters
	par_cov : de covariantie matrix - deze bevat informatie over de onzekerheid op par_opt
-->


We hebben eerst een functie nodig die de datapunten beschrijft en een set met startwaardes voor de parameters. We kijken eerst nog even naar de formule die in M1.1 is gegeven:

$${\displaystyle I(d; N_0, d_{half}) = I_0 \times \left( \frac{1}{2} \right) ^{d/d_{half}}}$$

We zien dat de functie uiteindelijk afhangt van twee parameters: $$I_0$$ en $$d_{half}$$. De waardes $$I_0$$ en $$I(d)$$ zijn natuurlijk direct gerelateerd aan de gemeten waardes voor $$N_0$$ en $$N(d)$$. In principe is $$N_0$$ en dus $$I_0$$ gemeten, maar hier zit een (bekende) onzekerheid op en om die reden wil je hem 'vrijlaten' in de fit.

De functie **`functie`** die we straks gebruiken voor de fit ziet er in het algemeen als volgt uit: 

	def functie(x,par1,par2) :
		y = een formule
		return y

De parameters die hier worden meegegeven zijn de parameters die worden geschat (of geoptimaliseerd) in de fit. Voor deze twee waardes zullen we straks ook de startwaardes moeten meegeven.

> 1. Schrijf nu eerst de code voor de functie **`functie(d, N0, dhalf)`** die de relatie tussen dikte d en de counts aangeeft. Controleer  of die goed werkt. 
> 2. Voor de fit hebben we ook een lijst met gewichten nodig, noem deze **`N_inv_err`**. Dit zijn de reciproke waardes van de fouten op de counts. Maak hiervoor een lijst aan. Als de onzekerheid op $$N$$, $$\Delta N$$ is, dan is het gewicht $$1/\Delta N$$.

Als we onze functie en de lijst met gewichten hebben gedefinieerd dan kunnen we de fit uitvoeren. 

	ons_model = models.Model(functie)
	result= ons_model.fit(counts, d=diktes, weights =N_inv_err, N0=startwaarde,dhalf=startwaarde)

We definiëren eerst **`ons_model`** en vervolgens fitten we deze. Je moet een aantal opties meegeven:
	
	result   : deze vangt het fit resultaat op
	counts   : de lijst met counts 
	d=diktes : d is de eerste parameter van functie, diktes is de lijst met diktes
	weights = N_inv_err : hier geef je de lijst met gewichten mee
	N0= startwaarde : hier moet je de startwaarde voor de fit meegeven op N0
	dhalf = startwaarde : hier moet je de startwaarde voor dhalf meegeven

Je ziet dat je nog zelf twee startwaardes mee moet geven voordat de fit kan werken.  
Met het volgende commando kun je de fitresultaten uitprinten: 

	print(result.fit_report())

> - **M3.2a) Voer de fit uit en bekijk het resultaat. Als je tevreden bent met de fit kopieer dan je resultaat op het inlevertemplate. Het kan zijn dat je de startwaardes van de parameters nog iets moet aanpassen als de fit niet convergeert.**

De gefitte curve kunnen we ook weergeven in een grafiek. Maak zoals gebruikelijk een grafiek met foutenvlaggen. Het fitresultaat kun je dan als volgt toevoegen: 

	plt.plot(diktes, result.init_fit, 'k--', label='initial fit')
	plt.plot(diktes, result.best_fit, 'r-', label='best fit')
	plt.legend(loc='best')

> - **M3.2b) Maak een grafiek met de datapunten, foutenvlaggen en het gefitte resultaat. Maak de grafiek netjes af.** <br><br>
> 
> - **M3.2c) Bekijk de gereduceerde $$\chi^2/df$$. Ziet deze waarde er goed uit? Beredeneer je antwoord. Wat is het aantal vrijheidsgraden in de fit?**<br><br>
>
> - **M3.2d) Wat is de geschatte waarde $$\hat{d}_{half}$$? Vergelijk deze met de 'true' waarde 'dtrue'.**<br><br> 
> 
> - **M3.2e) De correlatiecoëfficiënt $$\rho$$ wordt ook uitgeprint. Hoe groot is deze en wat zegt dat?**<br><br>
> 

Definieer nu een polynoom met de volgende code: 

	def poly(d,N0,a,b) :
  		y = N0 + a*d + b*d*d
  		return y

Fit deze functie aan de datapunten, zorg dat de startwaardes zo worden ingesteld dat de fit convergeert.

> - **M3.2f) Maak een grafiek met de datapunten, foutenvlaggen en het gefitte resultaat. Maak de grafiek netjes af.** <br><br>
>
> - **M3.2g) Presenteer de fitresultaten van de poly fit op het inlevertemplate.**<br><br>
> 
> - **M3.2h) Vergelijk nu de twee fits met elkaar. Bekijk de uitkomsten van de gefitte exponentiele functie met de gefitte polynoom. Welke functie beschrijft de data het beste? Op basis van welke variabelen trek je deze conclusie? Beargumenteer je antwoord.**




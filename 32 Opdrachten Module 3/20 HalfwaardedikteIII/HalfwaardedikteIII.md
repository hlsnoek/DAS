#M3.2 Halfwaardedikte III \*\*\*

In opgave M2.3 hebben we gezien dat de meetmethode die we gebruikten om de halfwaardedikte te bepalen niet optimaal was. Er was zeker sprake van een onzuivere meting doordat we stelselmatig een te hoge waarde van $$\text{d_half}$$ terugkregen. 

In deze opgave zullen we zien dat de onzuiverheid te maken heeft met de methode waarop we de halfwaardedikte hebben bepaald. Het heeft niets te maken met de opstelling van de meting of met de verzamelde datapunten. Het is de analyse techniek die zorgt voor de onzuiverheid.

In deze opdracht gaan we een fit gebruiken om de waarde van $$\text{d_half}$$ te achterhalen. In opdracht M3.1 hebben we onze eigen lineaire regressie methode geprogrammeerd met behulp van de kleinste kwadraten methode. In deze opdracht gebruiken we een fit pakket van python *scipy*. Dit programma rekent de $$\chi^2$$ uit en minimaliseert deze voor ons. Dat scheelt op zich een hoop werk, maar je zal in deze opdracht zien dat het toch ook weer niet helemaal vanzelf gaat. 

Om dit fit pakket te kunnen gebruiken moet het volgende import statement gebruiken: 

	from scipy.optimize import curve_fit

Maak nu een dataset aan met de standaard waardes zoals je dat in M2.3 ook hebt gedaan: 

	counts, diktes, dtrue = ds.DataSetHalfwaardeDikteVariatie()

Maak nu een lijst aan met de fouten op de counts.
We gaan nu de fit opzetten. De roep je op deze manier aan: 

	par_opt, par_cov = curve_fit(functie,diktes,counts,sigma=N_err,p0=start,absolute_sigma=True)

Je ziet dat de functie **`curve_fit`** verschillende opties nodig heeft en twee variabelen teruggeeft. We gaan even door het lijstje.

	functie : is de functie die de relatie tussen diktes en counts beschrijft
	diktes : de lijst met waardes langs de horizontale as
	counts : de lijst met waardes langs de verticale as
	sigma=std : std is de lijst met onzekerheden op de counts
	p0=start : de start parameters voor de fit in dezelfde volgorde as in f
	absolute_sigma=True : de fit gaat de opgegeven foutenvlaggen gebruiken
	par_opt : de lijst met geoptimaliseerde parameters
	par_cov : de covariantie matrix - deze bevat informatie over de onzekerheid op par_opt

We hebben dus een functie nodig die de datapunten beschrijft en een set met startwaardes voor de parameters. We kijken eerst nog even naar de formule die in M1.1 is gegeven:

$${\displaystyle I(d) = I_0 \times \left( \frac{1}{2} \right) ^{d/d_{half}}}$$

We zien dat de functie uiteindelijk afhangt van twee parameters: $$I_0$$ en $$d_{half}$$. Dit zijn de twee parameters die de fit zal proberen te optimaliseren. Voor deze twee waardes zullen we straks ook de startwaardes moeten meegeven. De functie **`functie`** die we straks moeten gebruiken in **`curve_fit`** ziet er in het algemeen als volgt uit: 

	def functie(x,par1,par2) :
		y = een formule
		return y


> * Schrijf nu de code en fit de dataset.
> **Tip**: Kijk goed naar de start waardes die je meegeeft en het gebied waar je de parameters gaat optimaliseren.
> * Maak een plot met de datapunten, foutenvlaggen en het gefitte resultaat.  
> * Bereken de absolute $$\chi^2$$ van de fit en de gereduceerde $$\chi^2/{df}$$.

We kijken nog even naar het resultaat van de fit. De covariantie matrix ziet er zo uit: 

	pcov = [[ var(par1) covar(par1,par2)]
	 [covar(par1,par2)  var(par2)]]

> * Wat is de onzekerheid op de gefitte $$\hat{d}_{half}$$? 
> * Zijn de twee parameters gecorreleerd?  Wat betekent dat?
> * Is de gefitte $$\hat{d}_{half}$$ zuiver of onzuiver? 
> * Noteer de geoptimaliseerde waardes van $$\hat{d}_{half}$$, $$\hat{N_0}$$ en hun onzekerheden.

Bedenk nu zelf een methode om te onderzoeken of de schatter zuiver is of onzuiver. 


> * Beschrijf de methode.
> * Voer de methode uit en presenteer je resultaten.

## M3.1 Grote Aantallen III *\*\*\*
<!--REF\label{/opdrachten-module-3/groteaantalleniii}-->

In deze opdracht gaan we het eindresultaat van M2.1 'fitten' met de kleinste kwadraten methode. 

We hebben gezien dat er verband is tussen de grootte van onze steekproef en de onzekerheid op het bepaalde gemiddelde. Deze volgt de $$\sqrt{n}$$-[wet](/module-2/wet-van-grote-aantallen). We gaan in deze opdracht een lineaire regressie (ofwel een fit) aan de data punten maken met behulp van de kleinste kwadraten methode. 

We gaan eerst even terug naar het experiment om te kijken wat we ook alweer aan het bepalen waren. 
We hebben een ton met kogels en een heel nauwkeurige weegschaal. We kunnen ons verschillende vragen stellen over de massa van de kogels. 

- Als we een kogel uit de ton pakken: "Wat is de massa van deze kogel?". 
	De massa van een enkele kogel weten we in dit experiment met bijna oneindige precisie. In ons voorbeeld zelfs bijvoorbeeld: $$m_{kogel} = 85.07426079254506 \pm 0.0000000000001 $$ gram.

- Wat is de massa van een ***typische*** kogel. Wat we hiermee bedoelen is: Als ik een *willekeurige* kogel uit de ton pak, wat is dan de massa? Het antwoord op deze vraag kun je vinden als je het gemiddelde weet van de kogels in de ton en de spreiding (standaardafwijking) van de kogelmassa's. Stel dat het gemiddelde van de populatie 25.0 gram is en de standaardafwijking 2.5 gram dan zeg je in dat geval dat een **typische** massa: $$m_{\text{kogel}} = 25.0 \pm 2.5$$ gram is. Je moet dan dus wel het gemiddelde en de spreiding weten, of bepalen. De standaardafwijking is hier dus een maat voor de onzekerheid.

- Om de bovenstaande vraag te kunnen beantwoorden moet je dus weten wat het gemiddelde van de kogel massa's is en wat de spreiding op deze massa's is. De derde vraag die je kunt stellen is dus: Wat is het gemiddelde van de kogel massa's. Om die vraag te beantwoorden kunnen we een steekproef nemen uit de ton. We zien dan al snel een spreiding ontstaan. Bij de eerste kogel kunnen we nog heel weinig zeggen over het populatie gemiddelde en zeker niets over de spreiding. Bij twee kogels heb je al wat meer informatie. Mocht je de standaardafwijking $$\sigma_m$$ kennen dan kun je uitrekenen wat de onzekerheid is op het steekproef gemiddelde met de $$\sqrt{n}$$ wet. Als je steekproef redelijk groot is, dan kun je ook de spreiding $$s_n$$ hiervoor gebruiken. De onzekerheid waar we hier over hebben gaat dus niet over de onzekerheid op de massa van een enkele kogel, maar over de onzekerheid op de centrale waarde van het kogelmassagemiddelde zelf.


We willen dus weten wat de een **typische** kogel uit de ton weegt, we nemen een steekproef om het gemiddelde van de kogels in de ton te bepalen en we onderzoeken hoe de onzekerheid op de centrale waarde van dit gemiddelde afhangt van de grootte van de steekproef. We focussen dus op de spreiding van de bepaalde gemiddeldes. In M2.1 hebben we een lineair verband gezien tussen de spreiding van de bepaalde gemiddeldes en de grootte van de steekproef. In deze opdracht gaan we deze nu 'fitten' met behulp van de kleinste kwadraten methode.. 

<!--Download allereerst een nieuwe [DAS_DatasetGenerator.py](DAS_DatasetGenerator.py) en voer weer je studentnummer in. 
-->
We gaan eerst datapunten fitten met gelijke fouten. Later kijken we naar meer realistische onzekerheden op de datapunten.
Met de volgende instructie kun je de datapunten opvragen: 

	inv_sqrt_n,std_n,std_n_err = ds.GroteAantallenFitSetGenerator() 

De **`inv_sqrt_n`** punten zijn de waardes van $$1/\sqrt{n}$$ waarbij $$n$$ de grootte is van de steekproef zoals je die in M2.1 hebt gedaan, **`std_n`** is de onzekerheid $$s_{g_{n}}$$ en **`std_n_err`** zijn de onzekerheden op de waardes van $$s_{g_n}$$. In deze opdracht noteren we $$s_{g_n}$$ als $$s_n$$ en de onzekerheid op deze standaardafwijking als $$\Delta s_n$$. 

Voor deze dataset zijn de waardes van $$\Delta s_n$$ dus nog allemaal gelijk, later in deze opdracht zullen we met meer realistische onzekerheden gaan werken. Maar eerst gaan we de fit opzetten.

Naar aanleiding van de $$\sqrt{n}$$-wet verwachten dat de relatie tussen $$n$$ en $$s_{n}$$ er als volgt uitziet:<br>
$${\displaystyle s_{n} = \sigma/\sqrt{n}.}$$


De parameter $$\sigma$$ is nu de standaardafwijking van de originele verdeling van de massa van de kogels, dus van de gehele populatie. De variabele $$\hat{\sigma}$$ is de geschatte waarde van $$\sigma$$ die we proberen te vinden met de fit. 

> * Maak eerst een grafiek waarbij je **`std_n`** tegen **`inv_sqrt_n`** uitzet met de foutenvlaggen. Gebruik hier niet de code voor uit M2.1 maar maak gebruik van de dataset die je met het commando dat hier boven beschreven staat verkrijgt. Kijk goed naar de punten en probeer alvast voor jezelf in te schatten welke waarde je verwacht voor $$\sigma$$.
>
>
> * Vind nu de meest optimale waarde van $$\sigma$$ door gebruik te maken van [de kleinste-kwadraten](/module-3/kleinste-kwadraten) methode. <br>
> 	1. Schrijf eerst een functie die voor een waarde van **`inv_sqrt_n`** en een gegeven waarde voor $$\sigma$$ een waarde teruggeeft voor de voorspelling van **`std_n`**. Gebruik hierbij de formule die hierboven gegeven is.  
> 
>	2. Schrijf een functie die de $$\chi^2$$ uitrekent volgens de formule die je vindt in het hoofdstuk [de kleinste-kwadraten](/module-3/kleinste-kwadraten). 
> 
>	3.  Schrijf een loop die over verschillende waardes van $$\sigma$$ loopt voor het optimalisatie proces en voor elke waarde van $$\sigma$$ de $$\chi^2$$ uitrekent.
> 
>	4. Vind nu voor welke waarde van $$\sigma$$ de laagste waarde van $$\chi^2$$ voorkomt. Dit is je schatting $$\hat{\sigma}$$.  
> **Tip:** Weet je zeker dat de waarde van $$\sigma$$  in het gebied ligt waar je probeert te optimaliseren? Probeer met de grafiek die je eerder maakte af te schatten welke waarde voor $$\sigma$$ je verwacht te vinden.<br>
> 
> - **M3.1a) Welke waarde voor $$\sigma$$ geeft de beste fit? Met andere woorden wat is, na het optimaliseren met de kleinste kwadraten methode, je geschatte $$\hat{\sigma}$$?** <br>
> 
> - **M3.1b) Maak een grafiek waarin je de waarde voor $$\chi^2$$ uitzet tegen $$\sigma$$.**
> 
> - **M3.1c) Maak een grafiek met de datapunten, de foutenvlaggen en het fit resultaat.**<br>
>  **Tip:** De gefitte functie kun je het makkelijkste plotten door met behulp van de **`inv_sqrt_n`** lijst een bijbehorende lijst te maken met behulp van de functie die je in stap 1 hebt gemaakt.<br><br>


Met de functie:
	
	s_true = ds.GroteAantallenStdTrue()

Kun je de werkelijke 'true'-waarde van $$\sigma$$ terugvragen. 

> - **M3.1d) Controleer of jouw gefitte waarde van $$\hat{\sigma}$$ overeen komt met je uitkomst met je uitkomst voor `s_true`. Je verwacht altijd nog wel wat verschillen te zien - vooral omdat de onzekerheden op de waardes van `s_n` niet realistisch waren.** 

We gaan nu de fit uitvoeren met realistische onzekerheden op de datapunten. Deze datapunten genereer je met de volgende functie: 

	 inv_sqrt_n,std_n,std_n_err = ds.GroteAantallenStdGenerator()
 
> - **M3.1e) Vind nu de meest optimale waarde van $$\hat{\sigma}$$ door gebruik te maken van de realistische foutenvlaggen. Bij welke $$\chi^2$$ ligt deze optimale waarde?**  <br><br>
>
> - **M3.1f) Maak nu een grafiek met de datapunten, de foutenvlaggen en het fit resultaat voor de dataset met reële foutenvlaggen.**  <br><br>
>
> - **M3.1g) Vergelijk nu de gevonden $$\hat{\sigma}$$ met de 'true' waarde van $$\sigma$$. Komt deze nu meer of minder overeen in vergelijking met je eerste fit?**  <br><br>
>
> - **M3.1h) Bereken nu de gereduceerde $$\chi^2$$, dat wil zeggen corrigeer de gevonden $$\chi^2$$ voor het aantal vrijheidsgraden van de fit. Interpreteer nu deze $$\chi^2_\nu$$. Is deze beter of slechter dan een $$\chi^2_\nu= 0.1$$? Zoals gebruikelijk, beredeneer je antwoord.**

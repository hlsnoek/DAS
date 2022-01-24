## M3.1 Grote Aantallen III *\*\*\*
<!--REF\label{/opdrachten-module-3/groteaantalleniii}-->

In deze opdracht gaan we het eindresultaat van M2.1 'fitten' met de kleinste kwadraten methode. 

We hebben gezien dat er verband is tussen de grootte van onze steekproef van kogels en de onzekerheid op het bepaalde gemiddelde. Deze volgt de $$\sqrt{n}$$-[wet](/module-2/wet-van-grote-aantallen). We gaan in deze opdracht een lineaire regressie (ofwel een functie fitten) aan de data punten maken met behulp van de kleinste kwadraten methode. 

We gaan eerst even terug naar het experiment om te kijken welke statistiek we eigenlijk proberen te bepalen.
We hebben een ton met kogels en een heel nauwkeurige weegschaal. We kunnen ons verschillende vragen stellen over de massa van de kogels. 

- Als we een kogel uit de ton pakken: "Wat is de massa van deze kogel?". 
	De massa van deze enkele kogel weten we in dit experiment met bijna oneindige precisie. In ons voorbeeld zelfs bijvoorbeeld: $$m_{kogel} = 85.07426079254506 \pm 0.0000000000001 $$ gram.

- Wat is de massa van een ***willekeurige*** kogel uit de ton? Wat we hiermee bedoelen is: Als ik een *willekeurige* kogel uit de ton pak, wat is dan de massa? Het precieze getal kunnen we niet van tevoren voorspellen, maar we weten wel ongeveer wat we kunnen verwachten als we het populatiegemiddelde en de standaardafwijking van de populatie kennen.  Stel dat het gemiddelde van de populatie 25.0 gram is en de standaardafwijking 2.5 gram dan zeg je in dat geval dat een **typische** massa: $$m_{\text{kogel}} = 25.0 \pm 2.5$$ gram is. De standaardafwijking is hier dus een maat voor de onzekerheid op de massa die we kunnen verwachten te meten.

- De derde vraag die je kunt stellen is: Wat is het gemiddelde van de kogel massa's? Om die vraag te beantwoorden kunnen we een steekproef nemen uit de ton. We zien dan al snel een spreiding ontstaan. Bij de eerste kogel kunnen we nog heel weinig zeggen over het populatiegemiddelde en zeker niets over de spreiding. Bij twee kogels heb je al wat meer informatie. Mocht je de standaardafwijking $$\sigma_m$$ van de populatie kennen dan kun je zelfs al uitrekenen wat de onzekerheid is op het steekproefgemiddelde met behulp van de $$\sqrt{n}$$ wet. Als je steekproef redelijk groot is, dan kun je ook de gemeten spreiding van de steekproef, $$s_n$$,  hiervoor gebruiken. De onzekerheid waar we hier over hebben gaat dus niet over de onzekerheid op de massa van een enkele kogel, maar over de onzekerheid op de centrale waarde van het kogelmassagemiddelde zelf.


We willen bepalen  wat een **gemiddelde** kogel uit de ton weegt, en om dit in te schatten  nemen we een steekproef van kogels uit de ton. We onderzoeken hoe de onzekerheid op de centrale waarde van dit gemiddelde afhangt van de grootte van de steekproef. We focussen dus op de spreiding van de berekende gemiddeldes. In M2.1 hebben we een verband gezien tussen de spreiding van de bepaalde gemiddeldes en de grootte van de steekproef. In deze opdracht gaan we deze nu 'fitten' met behulp van de kleinste kwadraten methode. 


We beginnen met het fitten van datapunten met gelijke fouten. Later gebruiken we meer realistische onzekerheden op de datapunten.
Met de volgende instructie kun je de datapunten opvragen: 

	inv_sqrt_n,std_n,std_n_err = ds.GroteAantallenFitSetGenerator() 

De **`inv_sqrt_n`** punten zijn de waardes van $$1/\sqrt{n}$$ waarbij $$n$$ de grootte is van de steekproef zoals je die in M2.1 hebt genomen, **`std_n`** is de onzekerheid $$s_{g_{n}}$$ en **`std_n_err`** zijn de onzekerheden op de waardes van $$s_{g_n}$$. In deze opdracht noteren we $$s_{g_n}$$ als $$s_n$$ en de onzekerheid op deze standaardafwijking als $$\Delta s_n$$. 

Voor deze dataset zijn de waardes van $$\Delta s_n$$ dus nog allemaal gelijk, later in deze opdracht zullen we met meer realistische onzekerheden gaan werken en kijken we naar het effect van de fouten op het fit resultaat. Maar eerst gaan we de fit opzetten.

Naar aanleiding van de $$\sqrt{n}$$-wet verwachten we dat de relatie tussen $$n$$ en $$s_{n}$$ er als volgt uitziet:<br>
$${\displaystyle s_{n} = \sigma/\sqrt{n}.}$$


De parameter $$\sigma$$ is nu de standaardafwijking van de originele verdeling van de massa van de kogels, dus van de populatie. De variabele $$\hat{\sigma}$$ is de geschatte waarde van $$\sigma$$ die we proberen te bepalen met de fit. 

> * Maak eerst een grafiek waarbij je **`std_n`** tegen **`inv_sqrt_n`** uitzet met de foutenvlaggen. Gebruik hier niet de code voor uit M2.1 maar maak gebruik van de dataset die je met het commando dat hier boven beschreven staat verkrijgt. Kijk goed naar de punten en probeer alvast voor jezelf in te schatten welke waarde je verwacht voor $$\sigma$$.
>
>
> * Vind nu de meest optimale waarde van $$\sigma$$ door gebruik te maken van [de kleinste-kwadraten](/module-3/kleinste-kwadraten) methode. 
> 
> 	1. Schrijf eerst een functie die voor een waarde van **`inv_sqrt_n`** en een gegeven waarde voor $$\sigma$$ een waarde teruggeeft voor de voorspelling van **`std_n`**. Gebruik hierbij de formule die hierboven gegeven is.  
> 
>	2. Schrijf een functie die de $$\chi^2$$ uitrekent volgens de formule die je vindt in het hoofdstuk [de kleinste-kwadraten](/module-3/kleinste-kwadraten). 
> 
>	3.  Schrijf een loop die over verschillende waardes van $$\sigma$$ loopt voor het optimalisatie proces en voor elke waarde van $$\sigma$$ de $$\chi^2$$ uitrekent.
> 
>	4. Vind nu voor welke waarde van $$\sigma$$ de laagste waarde van $$\chi^2$$ voorkomt. Dit is je schatting $$\hat{\sigma}$$.  
> **Tip:** Weet je zeker dat de waarde van $$\sigma$$  in het gebied ligt waar je probeert te optimaliseren? Probeer met de grafiek die je eerder maakte af te schatten welke waarde voor $$\sigma$$ je verwacht te vinden.<br>
> 
> - **M3.1a) Welke waarde voor $$\sigma$$ geeft de beste fit? Met andere woorden wat is, na het optimaliseren met de kleinste kwadraten methode, je geschatte $$\hat{\sigma}$$?**<br><br>
> 
> - **M3.1b) Wat is de waarde voor de geminimaliseerde $$\chi^2$$? Noteer ook hoeveel vrijheidsgraden er zijn en bereken de $$\chi^2_\nu.$$**<br><br>
> 
> - **M3.1c) Maak een grafiek waarin je de waarde voor $$\chi^2$$ uitzet tegen $$\sigma$$.**<br><br>
> 
> - **M3.1d) Maak een grafiek met de datapunten, de foutenvlaggen en het fit resultaat.**<br>
>  **Tip:** De gefitte functie kun je het makkelijkste plotten door met behulp van de **`inv_sqrt_n`** lijst een bijbehorende lijst te maken met behulp van de functie die je in stap 1 hebt gemaakt.<br><br>

Nadat we de fit hebben uitgevoerd bekijken we of het resultaat overeenkomt met de standaardafwijking van de populatie.

Met de functie:
	
	s_true = ds.GroteAantallenStdTrue()

Kun je de werkelijke 'true'-waarde van $$\sigma$$ terugvragen. 

> - **M3.1e) Controleer of jouw gefitte waarde van $$\hat{\sigma}$$ overeenkomt met je uitkomst voor `s_true`. Je verwacht altijd nog wel wat verschillen te zien - vooral omdat de onzekerheden op de waardes van `s_n` niet realistisch waren.** 

We gaan nu de fit uitvoeren met realistische onzekerheden op de datapunten. Deze datapunten genereer je met de volgende functie: 

	 inv_sqrt_n,std_n,std_n_err = ds.GroteAantallenStdGenerator()
 
> - **M3.1f) Vind nu de meest optimale waarde van $$\hat{\sigma}$$ door gebruik te maken van de realistische foutenvlaggen. Bij welke $$\chi^2$$ ligt deze optimale waarde?**<br><br>
>
> - **M3.1g) Maak nu een grafiek met de datapunten, de foutenvlaggen en het fit resultaat voor de dataset met reële foutenvlaggen.**<br><br>
>
> - **M3.1h) Vergelijk nu de gevonden $$\hat{\sigma}$$ met de 'true' waarde van $$\sigma$$. Komt deze nu meer of minder overeen in vergelijking met je eerste fit?**<br><br>
>
> - **M3.1i) Bereken nu de gereduceerde $$\chi^2$$, dat wil zeggen corrigeer de gevonden $$\chi^2$$ voor het aantal vrijheidsgraden van de fit. Is deze beter of slechter dan de gevonden waarde in opgave b. Geef hiervoor een verklaring.**

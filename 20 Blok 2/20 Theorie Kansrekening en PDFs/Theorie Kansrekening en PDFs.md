# Kansrekening en probability distribution functions

1. Ordered TOC
{:toc}

In de eerdere stof hebben we het al gehad over de kansdefinitie en de 'EN-regel' en de 'OF-regel' zie ['Basisbegrippen'](/blok-1/theorie-basisbegrippen). In deze sectie gaan we dieper in op kansrekening en zullen ook de zogenoemde probability distribution functions aan bod komen.

## Kansrekening vervolg

Bij kansrekening spelen begrippen zoals ordenen en kiezen een rol. Hieronder bespreken we de bijbehorende formules kort.  

### Ordenen

Het aantal manieren om $$n$$ verschillende objecten te *ordenen* is gelijk aan $$n!$$.
Hierbij kun je bijvoorbeeld denken aan het aantal manieren om drie ballen van verschillende kleur op een rij te leggen. Op de eerste plek kunnen we kiezen uit alledrie de ballen. Zodra we er daar eentje hebben gekozen kunnen we op de volgende plek nog uit twee ballen kiezen. Op de laatste plek is er dan nog 1 bal over. Het aantal mogelijkheden is dan dus $$3\cdot 2\cdot 1 = 3!$$.

Meer algemeen is het aantal manieren om $$n$$ objecten te ordenen, waarbij er groepjes $$k_1$$, $$k_2$$, $$\dots$$, $$k_n$$ zijn van niet van elkaar te onderscheiden objecten gelijk aan:

$$\frac{n!}{k_1!k_2!\dots k_n!}$$

Deze formule is ook toepasbaar op het bovenstaande voorbeeld waarbij de 'groepen van niet van elkaar te onderscheiden objecten' bestaan uit 1 bal van de ene kleur, 1 bal van de tweede kleur en 1 bal van de derde kleur. Met bovenstaande formule wordt het aantal manieren van ordenen dan $$\frac{3!}{1!1!1!} = 3!$$

Stel we hebben 5 rode ballen (R), 2 witte ballen (W) en 8 groene ballen (G). Het aantal manieren om deze ballen te ordenen (het aantal mogelijke volgordes) is dan gelijk aan $$\frac{15!}{5!2!8!} = 135135$$. 

### Kiezen

Het aantal manieren om te kiezen uit $$n$$ objecten speelt ook een rol in de statistiek.

Hierin onderscheiden we verschillende situaties:

 * Je kiest $$k$$ keer uit $$n$$ objecten en....
 	* het herhaaldelijk kiezen van hetzelfde object is *wel* mogelijk 
      * Aantal manieren van kiezen: $$n^k$$
 	* het herhaaldelijk kiezen van hetzelfde object is *niet* mogelijk
      * Volgorde van kiezen maakt *wel* uit: \frac{n!}{(n-k)!}
 	  * Volgorde van kiezen maakt *niet* uit: $$\frac{n!}{k!(n-k)!}=\binom{n}{k}$$
 
De situatie waarbij het *wel* mogelijk is om hetzelfde object meerdere keren te kiezen is bijvoorbeeld het aantal mogelijke pincodes met 4 cijfers gekozen uit de getallen 1 t/m 9. 

Het herhaaldelijk kiezen van hetzelfde 'object' is bijvoorbeeld niet mogelijk in het geval van een dataset met discrete meetwaarden of het kiezen van een steekproef uit een populatie.
Als er consequenties aan de volgorde van kiezen hangen dan maakt de volgorde van kiezen *wel* uit en anders niet. Zo maakt de volgorde van kiezen wel uit als we uit een groep van 10 mensen random drie mensen kiezen waarvan de 1e persoon die we kiezen heeft gewonnne, de tweede persoon staat op de tweede plaats en de derde staat op de derde plaats. Als we uit die groep van 10 personen random drie personen kiezen en er zijn geen consequenties aan verbonden dan maakt de volgorde van kiezen *niet* uit.


### Vaasmodellen

Voor situaties waarbij we een set van voorwerpen/situaties/meetwaarden hebben, en we willen de kans berekenen op $$a$$ keer situatie 1 (vanaf nu $$S_1$$ genoemd), $$b$$ keer $$S_2$$, etc. dan wordt de kans gegeven door het totale aantal mogelijke volgordes maal de kans op één volgorde.
Dit schrijven we bijvoorbeeld op als:

$$P(a\times S_1, b\times S_2,\dots,n\times S_n) = \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde})$$

Om te leren omgaan met dit soort kansen worden vaak de zogenoemde 'vaasmodellen' gebruikt. Hierbij wordt eerst gewerkt met het berekenen van kansen in het geval van een denkbeeldige vaas gevuld met ballen van verschillende kleuren. Er zitten bijvoorbeeld $$a$$ rode ballen, $$b$$ blauwe ballen en $$c$$ witte ballen in de vaas. Veel situaties in de kansrekening kunnen worden teruggeleid tot een vaasmodel.

Voorbeelden van situaties die te beschrijven zijn met een vaasmodel zijn o.a.: Het trekken van een aantal kaarten uit een pak, meerdere keren gooien met een dobbelsteen, een loterij met meerdere prijzen, een bepaald aantal keer kop en munt gooien, de kans dat een bepaald percentage Z-bosonen naar een e+e- paar is vervallen, een binomiale verdeling.

We onderscheiden de zogenoemde 'vaasmodellen met terugleggen' en de 'vaasmodellen zonder terugleggen'. 

### Vaasmodel zonder terugleggen

Bij een vaasmodel zonder terugleggen wordt een $$x$$ aantal ballen uit de vaas getrokken. Zonder de voorgaande bal terug in de vaas te doen, wordt de volgende bal uit de vaas getrokken. Dit kan in één greep gebeuren maar ook één voor één. Dit is een model met kansen die per trekking veranderen omdat de populatie dan niet meer hetzelfde is als voorheen.

Stel we hebben een vaas met 10 rode (R) ballen, 5 witte (W) ballen en 3 bruine (B) ballen. We trekken drie keer een bal uit deze vaas zonder terugleggen en willen de kans berekenen op twee witte ballen en één rode bal.

We schrijven de gevraagde kans op:

$$P(2W \text{ en } 1R) = \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde})$$

Omdat het bij deze situatie om een klein aantal gaat kunnen we ook al meteen beredeneren dat er in totaal drie volgordes zijn om twee witte ballen en één rode bal op te leggen:

- WWR
- WRW
- RWW

Dit kunnen we ook berekenen met de formule voor het aantal manieren om $$n$$ objecten t ordenen waarbij er groepjes $$k_1$$, $$k_2$$, etc. niet van elkaar te onderscheiden objecten zijn. In dit geval bestaat de eerste groep van niet van elkaar te onderscheiden objecten uit de twee witte ballen. Of we nu W1W2 of W2W1 trekken maakt niet uit, in beide gevallen hebben we twee witte ballen. De tweede groep van niet van elkaar te onderscheiden objecten bestaat uit de ene rode bal.

$$\Text{Aantal mogelijke volgordes} = \frac{3!}{2!1!} = 3$$

Nu moeten we de kans op één volgorde bepalen. Kies bijvoorbeeld de volgorde 'WWR', nu hebben we de EN-regel nodig:

$$P(WWR) = P(\text{1e bal }W\text{ en }\text{2e bal }W\text{ en 3e bal}R) = P(\text{1e bal }W)\cdot  P(\text{2e bal }W) P(\text{3e bal }R)$$

De kans om als eerste een witte bal te trekken is gelijk aan:

$$P(\text{1e bal }W) = \frac{5}{18}$$ 

We leggen de bal niet terug dus daarna zijn er nog 17 ballen aanwezig in de vaas. De kans om dan nog eens een witte bal te trekken is gelijk aan:

$$P(\text{2e bal }W) = \frac{4}{17}$$

Dan zijn er nog 16 ballen over in de vaas waarvan 10 rode. De kans om vervolgens een rode bal te trekken is dan ook:

$$P(\text{3e bal }R) = \frac{10}{16}=\frac{5}{8}$$

Dus de kans op de volgorde 'WWR' is:

$$P(WWR) = \frac{5}{18}\cdot\frac{4}{17}\cdot\frac{5}{8}$$

De kans op twee witte en één rode bal is dan:

$$\begin{aligned}P(2W \text{ en } 1R) &= \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde}) \\ 
&= 3\cdot \frac{5}{18}\cdot\frac{4}{17}\cdot\frac{5}{8} \\
&\approx 0.12\end{aligned}$$

### Vaasmodel met terugleggen

Bij een vaasmodel met terugleggen wordt er één voor één een bal uit de vaas gehaald, er wordt gekeken welke kleur is gepakt en daarna wordt de bal weer terug in de vaas gedaan voordat de volgende bal wordt gepakt. Dit is een model met kansen die elke keer gelijk blijven omdat de gehele populatie na de trekking weer aanwezig is in de vaas.  

Stel we hebben een vaas met 6 rode (R) ballen, 3 witte (W) ballen en 1 bruin (B) bal. We trekken drie keer een bal uit deze vaas zonder terugleggen en willen de kans berekenen op 1 rode bal, 1 witte bal en 1 bruine bal.

We schrijven de gevraagde kans op:

$$P(1R \text{ en } 1W \text{ en }1B) = \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde})$$

Het aantal mogelijke volgordes op 1 rode, 1 witten en 1 bruine bal op te leggen is gelijk aan:

$$\Text{Aantal mogelijke volgordes}=\frac{3!}{1!1!1!} = 3!=6$$

Nu moeten we de kans op één volgorde bepalen. Kies bijvoorbeeld de volgorde 'RWB', nu hebben we de EN-regel nodig:

$$P(RWB) = P(\text{1e bal }R\text{ en }\text{2e bal }W\text{ en 3e bal}B) = P(\text{1e bal }R)\cdot  P(\text{2e bal }W) P(\text{3e bal }B)$$

De kans om als eerste een rode bal te trekken is gelijk aan:

$$P(\text{1e bal }R) = \frac{6}{10}=\frac{3}{5}$$ 

Daarna leggen we de bal terug, dus er zijn weer 10 ballen in de vaas aanwezig.
De kans om daarna een witte bal te trekken is gelijk aan::

$$P(\text{2e bal }W) = \frac{3}{10}$$

We leggen de bal weer terug en de kans om dan als derde een (de) bruine bal te trekken is in dit geval: 

$$P(\text{3e bal }B) = \frac{1}{10}$$

Dus de kans op de volgorde 'RWB' is:

$$P(RWB) = \frac{3}{5}\cdot\frac{3}{10}\cdot\frac{1}{10} = \frac{9}{500}$$

De kans op één rode, één witte en één bruine bal is dan:

$$\begin{aligned}P(1R \text{ en } 1W \text{ en }1B) &= \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde}) \\ 
&= 6\cdot \frac{9}{500} \\
&\approx 0.11\end{aligned}$$


## Probability distribution functions

Een propability distribution function (PDF) ...
eventueel P-waarden nu hier al.
Dus gewoon wat uitleg, plaatje en de formule erbij. (Zie sullabus Hella)

algemeen PDF
kans altijd positief. integraal = 1.

### Binomiale verdeling

per verdeling uitleg, de formule, gemiddelde etc.

### Poisson verdeling


Poisson formule
poisson wordt gauss bij hoge waarden van lambda. De breedte is dan gedefinieerd. voor lage waarden van lambda is de verdeling niet-symmetrisch. Normaal ga je op symmetrische data een gauss toepassen en geen poisson (gauss is makkelijker).

### Normale verdeling 

### Uniforme verdeling

## P-value berekenen bij PDF's

### Binomiaal

### Poisson

### Normale verdeling 

### Uniforme verdeling





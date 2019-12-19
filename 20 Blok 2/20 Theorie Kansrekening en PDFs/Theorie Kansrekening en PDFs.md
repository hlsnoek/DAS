# Kansrekening en probability distribution functions

1. Ordered TOC
{:toc}

In de eerdere stof hebben we het al gehad over de kansdefinitie en de 'EN-regel' en de 'OF-regel' zie ['Basisbegrippen'](/blok-1/theorie-basisbegrippen). In deze sectie gaan we dieper in op kansrekening en zullen ook de zogenoemde probability distribution functions aan bod komen.

## Kansrekening vervolg

### Tellen

### Ordenen

### Kiezen

### Vaasmodellen

Voor situaties waarbij we een set van voorwerpen/situaties/meetwaarden hebben, en we willen de kans berekenen op $$a$$ keer situatie 1 (vanaf nu $$S_1$$ genoemd), $$b$$ keer $$S_2$$, etc. dan wordt de kans gegeven door het totale aantal mogelijke volgordes maal de kans op één volgorde.
Dit schrijven we bijvoorbeeld op als:

$$P(a\times S_1, b\times S_2,\dots,n\times S_n) = \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde})$$

Om te leren omgaan met dit soort kansen worden vaak de zogenoemde 'vaasmodellen' gebruikt. Hierbij wordt eerst gewerkt met het berekenen van kansen in het geval van een denkbeeldige vaas gevuld met ballen van verschillende kleuren. Er zitten bijvoorbeeld $$a$$ rode ballen, $$b$$ blauwe ballen en $$c$$ witte ballen in de vaas. Veel situaties in de kansrekening kunnen worden teruggeleid tot een vaasmodel.

We onderscheiden de zogenoemde 'vaasmodellen met terugleggen' en de 'vaasmodellen zonder terugleggen'. 

### Vaasmodel zonder terugleggen

Bij een vaasmodel zonder terugleggen wordt één voor één een $$x$$ aantal ballen uit de vaas getrokken. Zonder de voorgaande bal terug in de vaas te doen wordt de volgende bal uit de vaas getrokken.

Stel we hebben een vaas met 10 rode (R) ballen, 5 witte (W) ballen en 3 bruine (B) ballen. We trekken drie keer een bal uit deze vaas zonder terugleggen en willen de kans berekenen op twee witte ballen en één rode bal.

We schrijven de gevraagde kans op:

$$P(2W \text{ en } 1R) = \text{Aantal mogelijke volgordes}\cdot P(\text{één volgorde})$$

Omdat het bij deze situatie om ene klein aantal gaat kunnen we ook al meteen beredeneren dat er in totaal drie volgordes zijn om twee witte ballen en één rode bal op te leggen:

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

Voorbeelden van situaties die te beschrijven zijn met een vaasmodel zonder terugleggen zijn o.a.: Het trekken van een aantal kaarten uit een pak, meerdere keren gooien met een dobbelsteen, een loterij met meerdere prijzen, een bepaald aantal keer kop en munt gooien, de kans dat een bepaald percentage Z-bosonen naar een e+e- paar is vervallen.

Ook binomiale verdelingen worden beschreven met een vaasmodel. We zullen het later over binomiale verdelingen hebben.

### Vaasmodel met terugleggen


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





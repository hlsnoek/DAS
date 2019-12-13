
Even een test om te kijken of git nog werkt.

# Werkcollege 1

Vandaag gaan we aan de slag met het gemiddelde, de mediaan, de modus, de varantie, de standaardafwijking en de coëfficient van variatie. Daarnaast zullen we data als histogram plotten en hierbij een conclusie trekken over het optimale aantal bins.

## Opdracht 1 - waarden berekenen kleine dataset

Gegeven de volgende dataset:

$$33, 35, 40, 42, 47, 50, 51, 54, 59$$

#### Onderdeel a

Bepaal van deze dataset met de hand: 

- Het gemiddelde
- De mediaan
- De modus
- De range
- De variantie
- De standaardafwijking
- De coëfficient van variatie

#### Onderdeel b

Er zijn meer metingen gedaan en de dataset ziet er nu als volgt uit:

$$33, 35, 40, 42, 43, 44, 45, 47, 50, 51, 54, 59$$

Bepaal nogmaals de waarden uit onderdeel a met de hand. Welk van de waarden zijn nu verandert? Hoeveel zijn deze waarden verandert? Zijn er waarden gelijk gebleven?

## Opdracht 2 - Python: waarden berekenen grote dataset

Open Python en voer de volgende code uit om een random dataset te genereren met 200 waarden tussen de 0 en de 100. 

    import random
    import statistics as stat

    random.seed(30)
    randomData = [random.randint(0,100) for x in range(1, 200)]

Bepaal met behulp van Python:

- Het gemiddelde
- De mediaan
- De modus
- De range
- De variantie
- De standaardafwijking
- De coëfficient van variatie

Definieer ZELF de benodigde functies in Python. Gebruik hierbij de formules voor het gemiddelde, de mediaan etcetera zoals deze zij gegeven in de lesstof ['Basisbegrippen'](/blok-1/theorie-basisbegrippen)


Opdracht B1a.A : ['B1a.A_MooiPlotten'](B1a.A_MooiPlotten) 


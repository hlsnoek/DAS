
## De $$\chi^2$$ distributie

De $$\chi^2$$ distributie is een maat voor het verschil tussen de voorspelde waardes en het kwadraat van het verschil. Als de functie $$f$$ de data goed beschrijft zal de $$\chi^2$$ klein zijn. Als de $$\chi^2$$ dus groot blijft na het optimaliseren van de parameters van $$f$$ dan is er duidelijk iets misgegaan. Het kan zijn dat de functie $$f$$ de datapunten niet goed *kan* beschrijven, maar het kan ook zijn dat als je minimalisatie uitvoert met een computer deze het minimum niet goed heeft weten te vinden. 
Als daarentegen de $$\chi^2$$ heel klein is gaat er ook iets mis. Waarschijnlijk heb je de onzekerheden op de datapunten heel erg onderschat. 
Hoe groot je verwacht dat de waarde van $$\chi^2$$ is na het optimaliseren van de kleinste kwadraten methode kun je bepalen. We gaan hieronder daar verder op in.

We hebben gezien in het hoofdstuk over de kleinste kwadraten methode, dat de $$\chi^2$$ gedefinieerd is als het kwadratische gewogen verschil tussen de meetwaardes en de voorspelde waardes: <br>

<center>$${\displaystyle  \chi^2 = \sum^N_{i=1} \left( \frac{y_i-f(x_i;\hat{a},\hat{b},..)}{\sigma_i} \right)^2.}$$ </center>

Let op dat we hier de geoptimaliseerde parameters $$\hat{a}$$ van de functie hebben ingevuld. Deze waarde voor $$\chi^2$$ is dus al geminimaliseerd.




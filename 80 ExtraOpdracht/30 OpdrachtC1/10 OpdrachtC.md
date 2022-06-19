##Herkansingsopdracht C


Presenteer je antwoorden en je berekeningen in een pdf document. Let hierbij op het volgende: 

- Volg de definities, regels en instructies zoals in het DAS vak gegeven zijn. 
- Presenteer de data en de resultaten volgens de wetenschappelijke methode die uitgelegd is tijdens het vak.
- Als je formules en/of berekeningen gebruikt om tot antwoorden te komen dan vermeld je deze expliciet. **Voor enkel het numerieke antwoord worden meestal geen punten gegeven.** Vermeld dus **altijd** volgens welke methode/berekening het antwoord is gevonden.
- Voeg alle code toe die je gebruikt hebt om je antwoorden te genereren. **Antwoorden op vragen die met behulp van code zijn gemaakt maar waarvan geen code is ingeleverd krijgen nul punten.**

Nadat het werk is ingeleverd **volgt er een zoom-meting** waarbij vragen worden gesteld over het werk.

Als je tussendoor vast loopt neem dan contact met me op.

Succes!

##Opdracht 1 - Lange en Korte leerlingen [5 punten]
Gegeven zijn [metingen](lengtesVanLeerlingen.txt) van lengtes in cm van leerlingen van de middelbare school. In het bestand vind je de klas en de opgemeten lengte van alle leerlingen van de school.

**[a]** Presenteer de lengtes van alle leerlingen van de school in een histogram.<br>
**[b]** Bereken het gemiddelde, de mediaan en de standaard deviatie van de distributie.<br> 
**[c]** Als je een willekeurige leerling van de school om zijn of haar lengte vraagt, wat is dan de kans dat deze langer is dan 1,78 m?<br>
**[d]** Als je een willekeurige leerling uit de zesde klas haalt, wat is dan de kans dat de leerling langer is dan 1,78 m?<br>
**[e]** Wat is de kans dat een leerling met lengte kleiner dan 1,70 m in klas 6 zit? <br>

Stel nu dat blijkt dat er een probleem is met het meetlint dat gebruikt is voor de metingen. Het meetlint is gekrompen en als je 90 cm afleest op het meetlint dan is het eigenlijk maar 100cm,  dit is niet opgevallen tijdens het meten. 

**[f]** Hoe noem je dit type fout?<br>
**[g]** Wat gebeurt er met het gemiddelde, de mediaan en de standaard deviatie?<br>

 Op een **andere school** is bekend dat: 

 - 	exact 15% van de leerlingen van de school in klas 2 zit, 
 -  dat 25% van de leerlingen die in klas 2 zit langer is dan 1,75 meter,
 -  van alle leerlingen op de school 60% langer is dan 1,75 meter
 
**[h]** Wat is de kans dat een willekeurige leerling van deze andere school die langer is dan 1,75 meter in klas 2 zit?  
**[i]** Wat is de kans dat een willekeurige leerling van deze andere school die kleiner, of precies gelijk is aan 1,75 meter in groep 2 zit?		


## Opdracht 2 - Meten van de halfwaardetijd van een element [2.5 punten]
In deze opdracht krijg je data die genomen is met een Geiger Muller telbuis waarmee de radioactiviteit van een bron is gemeten. 
[Hier](dataOpdracht2.txt) vind je een dataset waarbij het aantal gemeten counts en de tijd in minuten is gegeven. Voor elke meetwaarde is 60 seconde lang gemeten, het aantal counts in dit tijdsinterval van 60 secondes is genoteerd in de dataset.

**[a]** Bereken voor elk van de gemeten punten de onzekerheid op de meting. Leg uit welke formules je hiervoor gebruikt. <br>
**[b]** Stel dat je berekent dat je op een bepaald tijdstip verwacht nog maar 10 counts te meten. Wat is dan de kans dat je er geen 10 maar 15 meet? Laat hierbij, net als voor alle andere opdrachten, je berekening zien en presenteer de formules die je gebruikt. <br>
**[c]** Bepaal uit de dataset de halfwaardetijd door de volgende functie te fitten aan de dataset. Gebruik hiervoor de volgende formule voor de halfwaarde tijd: 
   
   $$N(t) = N_0 \left(\frac{1}{2}\right)^{t/t_{half}}$$

Presenteer de meetresultaten en de fit in een grafiek. <br>
**[d]** Wat is de gereduceerde $$\chi^2$$ van de fit? Hoeveel vrijheidsgraden heeft de fit?<br>


## Opdracht 3 - Correlatie en Covariantie [2.5 punten]
In deze opdracht krijg je een dataset met de massa en de lengte van een 
set onbekende voorwerpen. De massa is steeds gegeven in gram, de lengte is gegeven in meter. [Hier](dataOpdracht3.txt) vind je de dataset.

**[a]** Maak een grafische presentatie van de data. <br>
**[b]** Bereken de correlatie en de covariantie van de dataset. Presenteer ook al je tussenresultaten.<br>
**[c]** Bereken de gemiddelde massa van de objecten en de geef de onzekerheid op dit berekende gemiddelde. <br>
**[d]** Stel nu dat ik de volgende vergelijking heb waarbij de ratio $$R$$ wordt gedefinieerd: 

$$R = \frac{M}{L}$$ 

en ik wil de gemiddelde van ratio,  $$\overline{R}$$ bepalen. Van een andere, vergelijkbare, dataset heb de volgende gemiddeldes bepaald: $$\overline{M} = 230 \pm 32$$ gram en $$\overline{L} = 23 \pm 5$$ meter.  Bereken voor deze waardes de ratio $$\overline{R}$$ en de onzekerheid hierop $$\Delta \overline{R}$$. Schrijf de hele berekening uit.

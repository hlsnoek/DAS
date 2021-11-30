# Python op je eigen computer


In dit vak gaan we met Python werken. We werken met scripts en macro's. 
Waarschijnlijk heb je eerder al, bijvoorbeeld bij Inleiding Programmeren, je eigen versie van python geïnstalleerd met Anaconda en heb je al een programma, zoals Visual Studio code waarin je de scripts kunt schrijven. 

Hieronder staan instructies om een nieuwe python omgeving te maken in anaconda waarin we in dit vak gaan werken. Hierbij hoort ook een testfile om te kijken of alle pakketten goed zijn geïnstalleerd. 

Mocht je nog helemaal geen installatie hebben dan vind je onderaan de pagina instructies om Anaconda en Visual Studio code te installeren. Hou er wel rekening mee dat we voor dit vak voorkennis van programmeren verwachten. 

## De DAS omgeving
Als je nog geen Anaconda hebt geïnstalleerd, doe dat dan eerst met de instructies onderaan de pagina, en kom dan hier terug. 

> 1. **Start een terminal**<br> 
> Je moet eerst een terminal openen. Dit kan op verschillende manieren. 
>  - Open Visual Studio Code en type de sneltoets combinatie  Ctrl + \` (tegelijk de Ctrl of command toets met een \`). Je kan ook een terminal openen vanuit het menu.
> 
>  - MacOS: Applications -> Utilities -> Terminal
> 
>  - Windows: Start -> Anaconda3 -> Anaconda Prompt
>
> 2. **Maak een nieuwe conda omgeving voor DAS**<br>
>  Type het volgende commando in: 
>
> 			conda create -n das matplotlib numpy lmfit -c conda-forge 
> Met dit commando heb je een nieuwe python omgeving gemaakt speciaal voor dit vak. 
> 
> 3. **Activeer je nieuwe conda omgeving**<br>
>  - Als je in Visual Studio werkt dan activeer je de conda omgeving door eerst een *Command Palette* te openen met (⇧⌘P) in MacOS en (Ctrl+Shift+p) in windows. Je typt dan *Python: Select Interpreter*. Scroll dan in de lijst naar beneden om je net gemaakte **das** omgeving te vinden (waarschijnlijk onderaan).
> 
>  - Als je in een terminal werkt, dan type je 
> 
> 			conda activate das
>

Controleer nu of je omgeving werkt door een testfile te draaien. Download de [testfile](AllePakketten.py), voeg hem toe aan een werkfolder voor dit vak en probeer hem te draaien. Je hoort, na een tijdje, de volgende output te zien: 

	Even controleren of je installatie helemaal werkt... 
    ... Je bent geslaagd!

Als je deze output niet ziet, dan is er een probleem met je installatie. Neem dan contact op met de assistent.


## Verse python/editor installatie

Volg deze instructie alleen als je nog geen Anaconda of editor hebt geïnstalleerd.

### Stap 1: Anaconda

Dit pakket kunt je downloaden op de [website](https://www.anaconda.com/download/). 
Kies daar voor de “Anaconda Individual Edition”. De download is vrij groot, het kan dus even duren voordat het klaar is!

Zodra de download klaar is, moet je het gedownloade bestand uitvoeren (dubbelklik?). Volg dan de installatieinstructies en kies waar nodig voor “Install for me only”; als het goed is hoef je verder niks te veranderen.

Let op: kies op Windows altijd de “advanced” installatie en kruis onderstaande vinkje aan! Als je dit niet hebt gedaan moet je het verwijderen en opnieuw installeren!



### Stap 2: Visual Studio Code

Dit pakket kun je downloaden op de website van [Microsoft](https://code.visualstudio.com/). Ook hier geldt dat je het bestand nog moet uitvoeren en installeren. Je hoeft niks aan te passen aan de installatie-opties. Heb je een Mac? Dan wordt het programma in je Downloads-map gezet. Je kunt het vanuit daar gewoon opstarten, maar je kan het ook even naar de Applications folder verplaatsen.

## Proefrit

Nu je zowel Anaconda als Visual Studio Code hebt geïnstalleerd, kunnen we gaan kijken of alles werkt. Volg de voorbeelden uit de video:



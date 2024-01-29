# SmartGrid

Veel huizen produceren tegenwoordig zelf energie, bijvoorbeeld via zonnepanelen. Wanneer een huis meer energie produceert dan nodig is voor eigen consumptie, kan het overschot aan energie worden verkocht aan de energieleverancier. Hiervoor is infrastructuur (het grid) nodig, waarbij batterijen de verschillen in consumptie en productie managen. 
In de SmartGrid case wordt een poging gedaan om de kosten van de grid, gebaseerd op de kabelsegmenten tussen de huizen en de batterijen op het grid te minimaliseren. Hiervoor wordt de data van drie districten gebruikt. We hebben drie algoritmes getest: baseline (randomise), greedy en hillclimber.

Baseline: ...
Greedy: ...
Hillclimber: ...

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python 3.7. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -r requirements.txt
```

Of via conda:

```
conda install --file requirements.txt
```

### Gebruik

De code wordt gerund door het aanroepen van:

```
python main.py
```

Het bestand geeft een voorbeeld voor gebruik van de verschillende functies.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren

## Auteurs
- Luc Mahieu
- Ayse Acar
- Dita van Leeuwen

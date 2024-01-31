# SmartGrid Tesla Engineers

Tegenwoordig produceren veel huizen zelf groene energie, bijvoorbeeld via zonnepanelen. Wanneer een huis meer energie produceert dan nodig is voor eigen gebruik, kan het overschot aan energie worden opgeleverd aan een energieleverancier. Hiervoor is infrastructuur (het grid) nodig. Op het grid staan huizen en batterijen, die verbonden worden via kabels. De capaciteit van een batterij mag niet overschreden worden door de gecombineerde outputs van de gekoppelde huizen. Ook mogen batterijen niet aan elkaar verbonden zijn, ook niet via een huis. Verder mag een huis niet aan meerdere batterijen verbonden zijn. 

In de SmartGrid case wordt een poging gedaan om de kosten van het grid, gebaseerd op de prijs van kabelsegmenten en batterijen, te minimaliseren. Het voordelig als huizen een kabel kunnen delen, aangezien dit het aantal benodigde kabelsegmenten minimaliseert en dit dus de kosten drukt. Er wordt data van drie districten gebruikt. We hebben drie algoritmes getest: baseline (randomise), greedy en hillclimber.

In het baseline algoritme, worden de huizen in een willekeurige volgorde afgegaan en gekoppeld aan een willekeurige batterij die nog genoeg capaciteit voor deze connectie over heeft. Vervolgens wordt de kabel gelegd op basis van de Manhattan distance, waarbij batterijen niet aan elkaar verbonden mogen worden. Het proces wordt herhaald totdat een valide oplossing is gevonden.

Het greedy algoritme volgt dezelfde stappen als baseline, met als verschil dat een huis wordt gekoppeld aan de dichtsbijzijnde batterij i.p.v. een willekeurige batterij die capaciteit over heeft. Er is geen verschil in het leggen van de kabel, dit gebeurt nog steeds op basis van de Manhattan distance.

In het hillclimber algoritme worden eerst een aantal heuristieken toegepast om clusters te vormen. 

Resultaten staan in output.json

## Aan de slag

### Vereisten

Voor het schrijven van de code hebben we Python 3.7 gebruikt. In requirements.txt staan alle benodigde packages. Deze kunnen geinstalleerd worden via pip dmv. de volgende instructie:

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

- **/code**: bevat alle code die geschreven is voor het oplossen van de case
  - **/code/algorithms**: bevat de algoritme classes; greedy, baseline en hillclimber
  - **/code/classes**: bevat de classes batterij, huis en grid
  - **/code/visualisation**: bevat de visualisatie van het grid en de kosten
- **/data**: bevat de data van de huizen en batterijen in de drie districten
- **/docs**: 
- **/experiments**: 

## Auteurs
- Luc Mahieu
- Ayse Acar
- Dita van Leeuwen

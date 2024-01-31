# SmartGrid Tesla Engineers

Tegenwoordig produceren veel huizen zelf groene energie, bijvoorbeeld via zonnepanelen. Wanneer een huis meer energie produceert dan nodig is voor eigen gebruik, kan het overschot aan energie worden opgeleverd aan een energieleverancier. Hiervoor is infrastructuur (het grid) nodig. Op het grid staan huizen en batterijen, die verbonden worden via kabels. De capaciteit van een batterij mag niet overschreden worden door de gecombineerde outputs van de gekoppelde huizen. Ook mogen batterijen niet aan elkaar verbonden zijn, ook niet via een huis. Verder mag een huis niet aan meerdere batterijen verbonden zijn. 

In de SmartGrid case is het doel om de kosten van het grid, gebaseerd op de prijs van kabelsegmenten en batterijen, te minimaliseren. Het is voordelig als huizen een kabel kunnen delen, aangezien dit het aantal benodigde kabelsegmenten minimaliseert en dit dus de kosten drukt. Er wordt data van drie districten gebruikt. We hebben drie algoritmes getest: baseline (randomise), greedy en hillclimber.

#### Baseline
In het baseline algoritme, worden de huizen in een willekeurige volgorde afgegaan en gekoppeld aan een willekeurige batterij die nog genoeg capaciteit voor deze connectie over heeft. Vervolgens wordt de kabel gelegd op basis van de Manhattan distance, waarbij batterijen niet aan elkaar verbonden mogen worden. Het proces wordt herhaald totdat een valide oplossing is gevonden.

#### Greedy
Het greedy algoritme volgt dezelfde stappen als baseline, met als verschil dat een huis wordt gekoppeld aan de dichtsbijzijnde batterij i.p.v. een willekeurige batterij die capaciteit over heeft. Er is geen verschil in het leggen van de kabel, dit gebeurt nog steeds op basis van de Manhattan distance.

#### Hill Climber
Het hill climber algoritme past andere heuristieken toe om zo weinig mogelijk kabels neer te leggen en zoveel mogelijk kabels te delen.Om te bepalen welke huizen bij welke batterij horen, wordt het greedy algoritme gebruikt. De optimalisatie die de hill climber toevoegt is gefocust op de manier waarop de huizen, die horen bij een batterij, met elkaar verbonden zijn. Het idee is dat er telkens de kortste route tussen het bestaande kabel netwerk en potentiele nieuwe onderdelen van het netwerk bepaald wordt om er vervolgens een kabel tussen te leggen. Daarbij worden eerst de huizen met elkaar verbonden, waardoor er kleine clusters van verbonden huizen ontstaan. Deze clusters worden vervolgens weer verbonden met elkaar door de kortste afstand tussen de kabels van clusters te bepalen en alleen de kortste routes per cluster aan te leggen. Dit proces herhaalt zich tot alle clusters van huizen met elkaar verbonden zijn, waarna de batterij op de kortst mogelijke manier verbonden wordt met het uiteindelijke cluster aan verbonden huizen. Het eindresultaat is een soort slinger van huizen die met de batterij verbonden zijn.

De resultaten staan in output.json

### Visualisatie
Voor elk district wordt elk algoritme gerund en wordt de kostendistributie gevisualiseerd. De runtime is gebaseerd op de ingevoerde duur, en dit zal ook het aantal iteraties bepalen. Dit is een histogram van de kosten per iteratie.
Vervolgens wordt de grid gevisualiseerd, met daarop de kabelsegmenten, batterijen en huizen zichtbaar. 

## Aan de slag

### Vereisten

Voor het schrijven van de code hebben we Python 3.9.18 gebruikt. Alle benodigde packages staan genoemd in requirements.txt en kunnen geïnstalleerd worden d.m.v het volgende commando: 

```
pip install -r requirements.txt
```

### Gebruik

De code wordt gerund door het aanroepen van:

```
python main.py
```

### Structuur

- **/code**: bevat code die geschreven is voor het oplossen van de case
  - **/code/algorithms**: bevat de algoritme classes; greedy, baseline en hillclimber
  - **/code/classes**: bevat de classes batterij, huis en grid
  - **/code/visualisation**: bevat de visualisatie van het grid en de kosten
- **/data**: bevat de data van de huizen en batterijen in de drie districten
- **/docs**: UML van de case
- **/experiments**: code om experimenten uit te voeren
- **/results**: resultaten van de verschillende experimenten

## Auteurs
- Luc Mahieu
- Ayse Acar
- Dita van Leeuwen

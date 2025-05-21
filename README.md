# SmartGrid Tesla Engineers

Nowadays, many homes generate their own green energy, for example through solar panels. When a home produces more energy than it needs for personal use, the surplus energy can be supplied to an energy provider. This requires infrastructure (the grid). On the grid, homes and batteries are connected via cables. The capacity of a battery may not be exceeded by the combined outputs of the connected houses. Also, batteries may not be connected to each other, not even indirectly via a house. Furthermore, a house may not be connected to multiple batteries.

In the SmartGrid case, the goal is to minimize the cost of the grid, based on the price of cable segments and batteries. It is advantageous if houses can share a cable, as this minimizes the number of required cable segments and therefore reduces costs. Data from three districts is used. We tested three algorithms: baseline (randomize), greedy, and hill climber.

#### Baseline

In the baseline algorithm, houses are processed in a random order and connected to a randomly chosen battery that still has enough capacity for the connection. The cable is then laid based on Manhattan distance, with the constraint that batteries cannot be connected to each other. The process is repeated until a valid solution is found.

#### Greedy

The greedy algorithm follows the same steps as the baseline, with the difference that a house is connected to the nearest battery instead of a random one with available capacity. Cable placement is still based on Manhattan distance.

#### Hill Climber

The hill climber algorithm uses different heuristics to lay as few cables as possible and to share cables wherever possible. To determine which houses belong to which battery, the greedy algorithm is used. The optimization that the hill climber adds focuses on how the houses assigned to a battery are interconnected. The idea is to repeatedly determine the shortest route between the existing cable network and potential new parts of the network, and then lay a cable between them. Initially, houses are connected to each other, creating small clusters of connected houses. These clusters are then connected by determining the shortest distance between cables from different clusters and laying only the shortest routes for each cluster. This process repeats until all house clusters are connected, after which the battery is connected in the shortest possible way to the final cluster of connected houses. The end result is a kind of chain of houses connected to the battery.

The results are available in `output.json`.

## Getting Started

### Requirements

We used Python 3.9.18 to write the code. All required packages are listed in `requirements.txt` and can be installed using the following command:

```
pip install -r requirements.txt
```

### Usage

The code is run by executing:

```
python main.py
```

### Structure

* **/code**: contains code written to solve the case

  * **/code/algorithms**: contains the algorithm classes; greedy, baseline, and hill climber
  * **/code/classes**: contains the classes for battery, house, and grid
  * **/code/visualisation**: contains the visualization of the grid and costs
* **/data**: contains data for houses and batteries in the three districts
* **/docs**: UML of the case
* **/experiments**: code for running experiments
* **/results**: results of the different experiments

## Authors

* Luc Mahieu
* Ayse Acar
* Dita van Leeuwen

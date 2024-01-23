from algorithms.randomize import Random_algo
from algorithms.euclidean_distance import Greedy_algo
from classes.district import District
from export_json import export_json
# from visualization.visualizegrid import visualize_grid
from algorithms.hill_climber import HillClimber
# from visualization.visualize_costs import visualize_costs


if __name__ == "__main__":
    #create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv", grid_size=50)
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    # connect houses with batteries in a district
    # R = Random_algo()
    # R.run(district1)

    hillclimber = HillClimber()
    number_of_iterations = 1
    hillclimber.run_experiment(district1, number_of_iterations)

    # # connect houses with batteries in a district
    # R = Greedy_algo()
    # R.run(district1)
    
    
    # district1.shared_costs()
    # print(district1.district_cost_shared)

    # district1.own_costs()
    # print(district1.district_cost_seperate)

    # export the results to a json file
    # output = export_json(district1)


    #visualize_grid(output)
            
    #print(District.own_costs())

    #visualize_grid(output)
    #visualize_costs(output)    
    


from algorithms.randomize import Random_algo
from algorithms.euclidean_distance import Greedy_algo
from classes.district import District
from export_json import export_json
from visualization.visualizegrid import visualize_grid

if __name__ == "__main__":
    #create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    # connect houses with batteries in a district
    R = Random_algo()
    R.run(district1)
    
    # # check if the cable routes indeed connect the houses with the batteries and if the cable stays on the grid
    # for battery in district1.batteries:
    #     for house in district1.battery_houses_connections[battery]:
    #         # print house and battery positions and the cable route between them
    #         print('\n\n\n')
    #         # print(f'House: {house.pos_x, house.pos_y} \nCable route: {house.cables}')
    #         #print(f'Battery: {battery.pos_x, battery.pos_y}')

    # # connect houses with batteries in a district
    # R = Greedy_algo()
    # R.run(district1)
    
    # # check if the cable routes indeed connect the houses with the batteries and if the cable stays on the grid
    # for battery in district1.batteries:
    #     for house in district1.battery_houses_connections[battery]:
    #         # print house and battery positions and the cable route between them
    #         print('\n\n\n')
    #         print(f'House: {house.pos_x, house.pos_y} \nCable route: {house.cables}')
    #         print(f'Battery: {battery.pos_x, battery.pos_y}')
    
    # district1.shared_costs()
    # print(district1.district_cost_shared)

    # district1.own_costs()
    # print(district1.district_cost_seperate)

    # export the results to a json file
    output = export_json(district1)

<<<<<<< HEAD
    #visualize_grid(output)
            
    #print(District.own_costs())
=======
    visualize_grid()
    
>>>>>>> 6ac88a3 (update)

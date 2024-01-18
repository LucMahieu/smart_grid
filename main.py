from algorithms.randomize import Random_algo
from classes.district import District
from export_json import export_json
from visualization.visualizegrid import visualize_grid

if __name__ == "__main__":
    # create districts from files with batteries and houses
    district1 = District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv")
    district2 = District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv")
    district3 = District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")

    # connect houses with batteries in a district
    R = Random_algo()
    R.run(district1)
    
    # print the connections between batteries and houses 
    # for battery in district1.batteries:
    #     for house in district1.battery_houses_connections[battery]:
            # print(battery.pos_x, house.pos_x, battery.pos_y, house.pos_y)

    # export the results to a json file
    output = export_json(district1)

    #visualize_grid(output)

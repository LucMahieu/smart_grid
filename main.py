import tqdm # progress bar
from classes.district import District
from export_json import export_json
from visualization.visualizegrid import visualize_grid
from algorithms.randomize_connections import random_assignment

if __name__ == "__main__":
    # create districts from files with batteries and houses
    districts = [
        District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv"),
        District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv"),
        District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")
    
    # connect houses with batteries in a district
    for district in districts:
        random_assignment(district)
    
    # # print the connections between batteries and houses 
    # for battery in district1.batteries:
    #     for house in district1.battery_houses_connections[battery]:
    #         print(battery.pos_x_batt, house.pos_x_house)

    # # print list of connected houses for each battery
    # for battery in district1.batteries:
    #     print(battery, district1.battery_houses_connections[battery])

    # call export_json function to get output
    output = export_json(districts)

    visualize_grid(output)

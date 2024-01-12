from classes.district import District
from export_json import export_json
from visualization.visualizegrid import visualize_grid

if __name__ == "__main__":
    districts = [District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv"),
                 District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv"),
                 District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")]

    # call export_json function to get output
    output = export_json(districts)

    visualize_grid(output)
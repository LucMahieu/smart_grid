from district import District
from collections import OrderedDict
import json

def house_to_dict(house):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(house.pos_x) + "," + str(house.pos_y)
    output["output"] = house.max_output
    output["cables"] = house.cables
    return output

def battery_to_dict(battery):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(battery.pos_x) + "," + str(battery.pos_y)
    output["capacity"] = battery.capacity
    output["houses"] = [house_to_dict(house) for house in battery.connected_houses]
    return output

def district_to_dict(district):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["district"] = district.name
    output["costs-shared"] = district.costs_shared
    output["batteries"] = [battery_to_dict(battery) for battery in district.batteries]
    return output

def export_json(districts):
    """Exports the districts to a json file."""
    output = [district_to_dict(district) for district in districts]
    with open("output.json", "w") as outfile:
        json.dump(output, outfile, indent=4, sort_keys=True)


if __name__ == "__main__":
    districts = [District(1, "data/district_1/district-1_batteries.csv", "data/district_1/district-1_houses.csv"),
                 District(2, "data/district_2/district-2_batteries.csv", "data/district_2/district-2_houses.csv"),
                 District(3, "data/district_3/district-3_batteries.csv", "data/district_3/district-3_houses.csv")]
    
    export_json(districts)
from collections import OrderedDict
import json

def house_to_dict(house):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(house.pos_x) + "," + str(house.pos_y)
    output["output"] = house.max_output
    output["cables"] = []
    for cable in house.cables:
        pos_x, pos_y = cable
        cable_as_string = str(pos_x) + "," + str(pos_y)
        output["cables"].append(cable_as_string)
    return output

def battery_to_dict(battery, district):
    """Converts the attributes of a class to a dictionary."""
    output = OrderedDict()
    output["location"] = str(battery.pos_x) + "," + str(battery.pos_y)
    output["capacity"] = battery.max_capacity
    output["houses"] = [house_to_dict(house) for house in district.houses]
    return output

def district_to_dict(district):
    """Converts the attributes of a class to a dictionary."""
    output_list = []
    district_description = {}
    district_description["district"] = district.name
    district_description["costs-shared"] = district.district_cost_shared
    output_list.append(district_description)
    for battery in district.batteries:
        output_list.append(battery_to_dict(battery, district))
    return output_list

def export_json(district):
    """Exports the districts to a json file."""
    district.shared_costs()
    output = district_to_dict(district)
    with open("output.json", "w") as outfile:
        json.dump(output, outfile, indent=4, sort_keys=False)

    return output
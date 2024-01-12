import district
import house

def house_to_dict(house):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["location"] = str(house.x_position) + "," + str(house.y_position)
    output["output"] = house.max_output
    output["cables"] = house.cables
    return output

def battery_to_dict(battery):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["location"] = str(battery.position_x) + "," + str(battery.position_y)
    output["capacity"] = battery.capacity
    output["houses"] = [house_to_dict(house) for house in battery.connected_houses]
    return output

def district_to_dict(district):
    """Converts the attributes of a class to a dictionary."""
    output = {}
    output["district"] = district.name
    output["costs-shared"] = district.costs_shared
    output["batteries"] = [battery_to_dict(battery) for battery in district.batteries]



{
    "district": 1,
    "costs-shared": 10198,
    "batteries": [
        {
            "location": "38,12",
            "capacity": 1507.0,
            "houses": [
                {
                    "location": "33,7",
                    "output": 39.45690812,
                    "cables": [
                        "33,7",
                        "33,8",
                        "33,9",
                        "33,10",
                        "33,11"
                    ]
                },
                {
                    "location": "30,12",
                    "output": 66.05341632,
                    "cables": [
                        "30,12",
                        "31,12",
                        "32,12",
                        "33,12",
                        "34,12"
                    ]
                }
            ]
        },
        {
            "location": "42,3",
            "capacity": 1507.0,
            "houses": [
                {
                    "location": "48,4",
                    "output": 58.90934923,
                    "cables": [
                        "48,4",
                        "48,3",
                        "47,3",
                        "46,3"
                    ]
                }
            ]
        }
    ]
}
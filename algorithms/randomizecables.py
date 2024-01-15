from classes.cable import Cable


# function that randomizes cables
def random_cables(district, connections):
    cables = []
    for connection in connections:
        house = connection['house']
        battery = connection ['battery']

        # generate and lay the cable
        cable_route = {
            'start_x': house.pos_x,
            'start_y': house.pos_y,
            'end_x': battery.pos_x,
            'end_y': battery.pos_y
        }

        #lay cables and save info
        cable = Cable(


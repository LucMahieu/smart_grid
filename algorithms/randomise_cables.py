import random
from classes.district import District 

# function that randomizes cables
def random_cables(houses):
    '''
    Randomly lay cable from house to selected battery
    '''
    for house in houses:

        # cable starts at house and ends at battery
        cable_start_x = house.pos_x
        cable_start_y = house.pos_y
        cable_end_x = house.battery.pos_x
        cable_end_y = house.battery.pos_y

        # generate random route 
        cable_x = cable_start_x
        cable_y = cable_start_y
        for ... in range ...:
            if ...:
                cable_x += 1
            else:
                cable_x -= 1
        
        for ... in range ...:
            if ...: 
                cable_y += 1
            else:
                cable_y -= 1

        #lay cables and save info
        cable = Cable((cable_route['start_x'], cable_route['start_y']),
            (cable_route['end_x'], cable_route['end_y']))

        

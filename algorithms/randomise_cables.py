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
        cable_route = [cable_start_x, cable_start_y]
        cable_x = cable_start_x
        cable_y = cable_start_y

        # kaying cable untill battery is reached 
        while (cable_x, cable_y) != (cable_end_x, cable_end_y):
            if ...:
                cable_x += 1
            else:
                cable_x -= 1
        
            if ...: 
                cable_y += 1
            else:
                cable_y -= 1

            cable_route.append(cable_x, cable_y)
            
        # #lay cables and save info
        # cable = Cable((cable_route['start_x'], cable_route['start_y']),
        #     (cable_route['end_x'], cable_route['end_y']))

  ### KIJK HIER###      

    #         if move_horizontally:
    #             cable_x += 1 if random.choice([True, False]) else -1
    #         elif move_vertically:
    #             cable_y += 1 if random.choice([True, False]) else -1

    #         # lay cables and save info
    #         cable = Cable((cable_start_x, cable_start_y), (cable_x, cable_y))
    #         cables.append(cable)

    # return cables

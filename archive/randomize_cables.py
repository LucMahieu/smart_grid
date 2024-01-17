import random
from classes.district import District 

def random_segment(current, end):
    '''
    Randomly choosing where to lay a single cablesegment within 50 x 50 grid until battery is reached
    '''
    if current == end:
        return 0
    elif current == 0:
        return random.choice([0, 1])
    elif current == 50:
        return random.choice([0, -1])
    else:
        return random.choice([-1, 0, 1])

def random_cables(houses):
    '''
    Lay cable from house to selected battery
    '''
    for house in houses:

        # cable starts at house and ends at battery
        cable_start_x = house.pos_x
        cable_start_y = house.pos_y
        cable_end_x = house.battery.pos_x
        cable_end_y = house.battery.pos_y

        # generate random route 
        cable_route = [(cable_start_x, cable_start_y)]
        cable_x = cable_start_x
        cable_y = cable_start_y

        # laying cable untill battery is reached 
        while (cable_x, cable_y) != (cable_end_x, cable_end_y):
            cable_x += random_segment(cable_x, cable_end_x)
            cable_y += random_segment(cable_y, cable_end_y)

            cable_route.append((cable_x, cable_y))
                
            house.cables = cable_route
                
        return house.cables
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

def laying_cables(houses):
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
            
            # if cable_x == 50:
            #     cable_x += random.choice([0, -1])
            # elif cable_x == 0:
            #     cable_x += random.choice([0, 1])
            # else:
            #     cable_x += random.choice([-1, 0, 1])

            # if cable_y == 50:
            #     cable_y += random.choice([0, -1])
            # elif cable_y == 0:
            #     cable_y += random.choice([0, 1])
            # else:
            #     cable_y += random.choice([-1, 0, 1])

            # cable_route.append((cable_x, cable_y))

            # cable_x += 1 if random.choice([True, False]) and cable_x < 50 else -1 if cable_x > 0 else 0
            # cable_y += 1 if random.choice([True, False]) and cable_y < 50 else -1 if cable_y > 0 else 0

            # if ...:
            #     cable_x += 1
            # else:
            #     cable_x -= 1
        
            # if ...: 
            #     cable_y += 1
            # else:
            #     cable_y -= 1

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

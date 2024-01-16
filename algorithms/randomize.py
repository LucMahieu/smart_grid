import random

class Random():
    def __init__(self):
        pass

    def run(self, district):
        '''
        Runs random algorithm; randomizes which battery a house is connected to and cableroute.
        '''
        # add batteries to connections dict with empty list for connected houses
        for battery in district.batteries:
            district.battery_houses_connections[battery] = []

        for house in district.houses:
            house.battery = self.random_assignment(district.batteries, house)
            house.cables = self.random_cables(house)
    
        return district 
    
    def random_assignment(self, district, batteries, house):
        '''
        Randomly assigns each house a battery that meets the requirements.
        '''
        # make copy of batteries list to keep track of batteries that have been tried
        batteries_copy = batteries.copy()

        # set enough_capacity to False to start while loop
        enough_capacity = False

        # keep selecting random battery until a battery with enough capacity is found
        while enough_capacity == False:

            if len(batteries_copy) == 0:
                print("No battery has enough capacity")
                break

            # select random battery from shrinking list of batteries
            selected_battery = random.choice(batteries_copy)

            # check if battery has enough capacity
            enough_capacity = selected_battery.capacity_check(house)

            # remove battery from list of batteries because it doesn't have enough capacity
            batteries_copy.remove(selected_battery)

        # add current house to the list of houses that are connected to the selected battery
        district.battery_houses_connections[selected_battery].append(house)

    def random_segment(self, current, end):
        '''
        Chooses randomly where to lay a single new cablesegment within 50 x 50 grid
        '''
        if current == end:
            return 0
        elif current == 0:
            return random.choice([0, 1])
        elif current == 50:
            return random.choice([0, -1])
        else:
            return random.choice([-1, 0, 1])

    def random_cables(self, house):
        '''
        Lay cable from house to selected battery
        '''

        # Cable starts at house and ends at battery
        cable_start_x = house.pos_x
        cable_start_y = house.pos_y
        cable_end_x = house.battery.pos_x
        cable_end_y = house.battery.pos_y
        cable_route = [(cable_start_x, cable_start_y)]
        cable_x = cable_start_x
        cable_y = cable_start_y

        # Keep laying cable untill battery is reached 
        while (cable_x, cable_y) != (cable_end_x, cable_end_y):
            # Generate random route 
            cable_x += self.random_segment(cable_x, cable_end_x)
            cable_y += self.random_segment(cable_y, cable_end_y)

            cable_route.append((cable_x, cable_y))
            
        return cable_route 
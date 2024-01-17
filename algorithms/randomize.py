import random
from algorithms.random_steps import determine_next_step

class Random_algo():
    def __init__(self):
        pass

    def run(self, district):
        '''
        Runs random algorithm; randomizes which battery a house is connected to and cableroute.
        '''
        for house in district.houses:
            district.battery_houses_connections
            house.battery = self.random_assignment(district, house)
            # house.cables = self.random_cables(house)
            house.cables = self.random_cables_v2(house)
    
        return district 

    def random_assignment(self, district, house):
        '''
        Randomly assigns each house to a battery that meets the requirements (e.g. enough capacity).
        '''
        # Make copy of batteries list to keep track of batteries that have been tried
        batteries_copy = district.batteries.copy()

        # Set enough_capacity to False to start while loop
        enough_capacity = False

        # Keep selecting random battery until a battery with enough capacity is found
        while enough_capacity == False:
            print(len(batteries_copy))

            if len(batteries_copy) == 0:
                print("No battery has enough capacity")
                break

            # Select random battery from shrinking list of batteries
            selected_battery = random.choice(batteries_copy)

            # Check if battery has enough capacity
            enough_capacity = selected_battery.capacity_check(house)

            # Remove battery from list of batteries because it doesn't have enough capacity
            batteries_copy.remove(selected_battery)

        # Add current house to the list of houses that are connected to the selected battery
        district.battery_houses_connections[selected_battery].append(house)

        return selected_battery

    def random_segment(self, current, end):
        '''
        Chooses randomly where to lay a single new cablesegment within 50 x 50 grid.
        '''
        # Stay in same position if battery is reached
        if current == end:
            return 0
        
        # Go forward or stay in same position at start of grid
        elif current == 0:
            return random.choice([0, 1])
        
        # Go backward or stay in same position at end of grid
        elif current == 50: 
            return random.choice([0, -1])
        
        # Move in any direction
        else:
            return random.choice([-1, 0, 1])

    def random_cables(self, house):
        '''
        Lay cable from house to selected battery.
        '''
        # Cable starts at house and ends at battery
        cable_start_x = house.pos_x
        cable_start_y = house.pos_y
        cable_end_x = house.battery.pos_x
        cable_end_y = house.battery.pos_y
        cable_route = [(cable_start_x, cable_start_y)]

        # starting position of cable
        cable_x = cable_start_x
        cable_y = cable_start_y

        # Keep generating and adding cable segments untill battery is reached
        while (cable_x, cable_y) != (cable_end_x, cable_end_y):
            # Generate random segment (step)
            cable_x += self.random_segment(cable_x, cable_end_x)
            cable_y += self.random_segment(cable_y, cable_end_y)

            # Add segment to cable route
            cable_route.append((cable_x, cable_y))
            
        return cable_route 
    


# ---------------------------------------------------------------------------------------------
    # new version of random_cables

    def random_cables_v2(self, house):
        '''
        Lay cable from house to selected battery.
        '''
        # Cable starts at house and ends at battery
        cable_end_x = house.battery.pos_x
        cable_end_y = house.battery.pos_y
        cable_route = [(house.pos_x, house.pos_y)]

        # starting position of cable is the house position
        current_x = house.pos_x
        current_y = house.pos_y

        # initialize fictitious previous position to determine direction of next step
        prev_x = current_x - 1
        prev_y = current_y

        # initialize new position
        new_x = current_x
        new_y = current_y

        # keep generating and adding cable segments untill battery is reached
        while (current_x, current_y) != (cable_end_x, cable_end_y):
            # Generate random segment (step)
            new_x, new_y = determine_next_step(prev_x, prev_y, current_x, current_y)

            # Add segment to cable route
            cable_route.append((new_x, new_y))

            # after the step, the current position becomes the previous position
            prev_x = current_x
            prev_y = current_y

            # after the step, the new position becomes the current position
            current_x = new_x
            current_y = new_y
            
        return cable_route
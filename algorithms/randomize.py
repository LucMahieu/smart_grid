import random
from classes.district import District 

class Random():
    def __init__(self):
        ""
        pass

    def run(self, district):
        '''
        Runs random algorithm; randomizes which battery a house is connected to and cableroute
        '''
        for house in houses:
            house.battery = self.random_assignment(batteries, houses)
            house.cables = self.random_cables(houses)
    
        return district 

    def random_assignment(self, batteries, house):
        '''
        Assigns each house a battery that meets the requirements
        '''
        # Randomly select battery from list
        selected_battery = random.choice(batteries)
            
        # If selected battery does not have capacityleft, keep selecting random battery from list
        while self.capacity_check(selected_battery, house) == False:
            selected_battery = random.choice(batteries)

        return selected_battery


    def capacity_check(self, battery, house):
        '''
        Checks if assigned battery has capacity left to be connected to new house based on its output
        '''
        if battery.capacity >= house.max_output:
            # updating battery capacity
            battery.capacity -= house.max_output
            return True 
        
        else:
            return False

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
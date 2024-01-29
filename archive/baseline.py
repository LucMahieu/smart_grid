import random

class Baseline():
    def __init__(self):
        pass


    def run(self, district):
        """
        Makes connections between random batteries and houses and lays cable routes between them based on Manhattan distance.
        """
        # Random order of houses
        random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to random battery with enough capacity left
            self.random_connection(district, house)
            
            # If no battery available with enough capacity, break
            if house.battery == None:
                print("Invalid solution")
                break 
            
            # If solution is valid, start laying cable route based on Manhattan distance 
            self.lay_cable_route(house)

        return district
    

    def random_connection(self, district, house):
        """
        Assigns random battery to current house and adds it to the connections dictionary.
        """
        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # Check if battery has enough capacity to connect to house
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:
            # Select random battery from the list of batteries with enough capacity
            random_battery = random.choice(batteries_with_capacity)

            # Connect selected battery to the current house
            house.battery = random_battery

            # Update battery capacity
            house.battery.update_capacity(house)

            # Add current house to the list of houses that are connected to the selected battery
            district.battery_houses_connections[random_battery].append(house)


    def lay_cable_route(self, house):
        """
        Lays cable route from current house to randomly selected battery.
        """
        # Starting of the current position at the house coordinates
        self.current_pos = [house.pos_x, house.pos_y]
        house.cables = [tuple(self.current_pos)]

        # End position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # Keep adding cable segments until the x-coordinate of the end position is reached
        while self.current_pos[0] != cable_end_pos[0]:
            # If current position is to the left of the end, move right
            if self.current_pos[0] - cable_end_pos[0] < 0:
                self.current_pos[0] += 1
                house.cables.append(tuple(self.current_pos))

            # If current position is to the right of the end, move left
            else:
                self.current_pos[0] -= 1
                house.cables.append(tuple(self.current_pos))

        # Keep adding cable segments until the y-coordinate of the end position is reached
        while self.current_pos[1] != cable_end_pos[1]:

            # If current position is below the end, move up
            if self.current_pos[1] - cable_end_pos[1] < 0:
                self.current_pos[1] += 1
                house.cables.append(tuple(self.current_pos))

            # If current position is above the end, move down
            else:
                self.current_pos[1] -= 1
                house.cables.append(tuple(self.current_pos))
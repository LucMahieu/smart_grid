import random

class Greedy_algo2():
    def __init__(self):
        self.prev_pos = ()

    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''
        # Random order of houses
        random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to random battery with capacity
            self.closest_connection(house, district)
            
            # If no battery available with enough capacity
            if house.battery == None:
                print("Invalid solution")
                break 
            
            else:
                # Lays cable route based on manhattan distance 
                self.lay_cable_route(house)

        return district
    
    def manhattan_distance(self, beginning, end):
        '''
        Calculates Manhattan distance between two points.
        '''
        x1, y1 = beginning[0], beginning[1]
        x2, y2 = end[0], end[1]

        distance = abs(x1 - x2) + abs(y1 - y2)
        
        return distance
    
    def min_distance(self, selected_batteries, house):
        '''
        Selects the battery closest to the selected house with enough capacity left.
        '''
        distance_dict = {}
        beginning = house.pos_x, house.pos_y

        # Calculate manhattan distance for all batteries with enough capacity
        for option in selected_batteries:
            end = option.pos_x, option.pos_y
            distance = self.manhattan_distance(beginning, end)
            distance_dict[option] = distance

        # Check if there are any batteries left with enough capacity
        if distance_dict:
            # Saving closest battery 
            best_battery = min(distance_dict, key = distance_dict.get)

            return best_battery
        
        else:
            # Invalid solution; no batteries left
            print("No valid batteries found")
            
            return None

    def closest_connection(self, house, district):
        '''
        Connects a house to the closest battery with enough capacity left.
        '''
        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in district.batteries:
            # Check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        if batteries_with_capacity:
            # Connecting to closest battery with capacity
            selected_battery = self.min_distance(batteries_with_capacity, house)

            # Update the house's battery attribute
            house.battery = selected_battery

            # Update battery capacity
            house.battery.update_capacity(house)

    def lay_cable_route(self, house):
        '''
        Lays cable route from house to selected battery.
        '''
        # Starting position of current pos and cable route is the house position
        self.current_pos = [house.pos_x, house.pos_y]
        house.cables = [tuple(self.current_pos)]

        # end position of cable is the battery position
        cable_end_pos = (house.battery.pos_x, house.battery.pos_y)

        # keep generating and adding cable segments until the battery is reached
        for _ in range(abs(self.current_pos[0] - cable_end_pos[0])):
            # If current position is to the left of the end, move right
            if self.current_pos[0] - cable_end_pos[0] < 0:
                self.current_pos[0] += 1
                house.cables.append(tuple(self.current_pos))

            # If current position is to the right of the end, move left
            else:
                self.current_pos[0] -= 1
                house.cables.append(tuple(self.current_pos))

        # Keep adding cable segments until the y-coordinate of the end position is reached
        for _ in range(abs(self.current_pos[1] - cable_end_pos[1])):

            # If current position is below the end, move up
            if self.current_pos[1] - cable_end_pos[1] < 0:
                self.current_pos[1] += 1
                house.cables.append(tuple(self.current_pos))

            # If current position is above the end, move down
            else:
                self.current_pos[1] -= 1
                house.cables.append(tuple(self.current_pos))
            

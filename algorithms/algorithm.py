import random 

class Algorithm():
    def __init__(self):
        self.prev_pos = ()
        self.invalid = 0

    def run(self, district):
        '''
        Makes connections between batteries and houses and lays cable routes between them.
        '''
        # Random order of houses
        random.shuffle(district.houses)

        for house in district.houses:
            
            # Connect house to closest battery with capacity
            self.closest_connection(house, district)
            
            # If no battery available with enough capacity
            if house.battery == None:
                self.invalid += 1
                print("Invalid solution")
                return False 
            
            else:
                # Lays cable route based on steps that minimize distance
                self.lay_cable_route(house)
                choose_step_randomly()
                choose_step_greedily()

        return district
    
class Battery():
        
    def __init__(self, pos_x_batt, pos_y_batt, capacity):
        self.pos_x_batt = pos_x_batt
        self.pos_y_batt = pos_y_batt
        self.capacity = capacity
        self.price = 5000
    
    def capacity_check(self, house):
        '''
        Checks if assigned battery has capacity left to be connected to new house
        '''
        if self.capacity >= house.max_output:
            # updating battery capacity
            self.capacity -= house.max_output
            return True 
        
        else:
            return False

            

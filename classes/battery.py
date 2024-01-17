class Battery():
        
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        self.price = 5000

    def update_capacity(self, house):
        '''
        Updates capacity of battery after connecting house
        '''
        self.capacity -= house.max_output
    
    def check_capacity(self, house):
        '''
        Checks if assigned battery has capacity left to be connected to new house
        '''
        if self.capacity >= house.max_output:
            return True 
        else:
            return False

            

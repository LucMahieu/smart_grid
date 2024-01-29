class Battery():   
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        self.max_capacity = capacity # Added to keep track of original capacity to create export_json output
        self.original_capacity = capacity
        self.price = 5000

    def reset_capacity(self):
        '''
        Resets the battery's capacity to its original capacity.
        '''
        self.capacity = self.original_capacity

    def update_capacity(self, house):
        '''
        Updates capacity of battery after connecting house
        '''
        self.capacity -= house.max_output
    
    def check_capacity(self, house):
        '''
        Checks if assigned battery has capacity left to be connected to new house
        '''
        return self.capacity >= house.max_output

            

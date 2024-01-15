import random
from classes.district import District  

def random_assignment(batteries, houses):
    '''
    Randomly assign each house to batteryi now want 
    '''
    for house in houses:
        # randomly select battery
        selected_battery = random.choice(batteries)
        
        # if battery does not have capacity left based on output selected house, keep selecting a random house
        while capacity_check(selected_battery, house) == False:
            selected_battery = random.choice(batteries)

        house.battery = selected_battery


def capacity_check(battery, house):
    '''
    Checks if assigned battery has capacity left to be connected to new house
    '''
    if battery.capacity >= house.max_output:
        # updating battery capacity
        battery.capacity -= house.max_output
        return True 
    
    else:
        return False


import math
from algorithms.randomize.py import Random_algo() 

def eucledian_distance(house, battery):
    '''
    Calculates Euclidean distance between battery and house
    '''
    x1, y1 = house.pos_x, house.pos_y
    x2, y2 = battery.pos_x, battery.pos_y

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return distance

def min_distance(batteries, houses):
    '''
    '''
    best_option_dict = {}
    for house in houses:
        distance_dict = {}
        for battery in batteries:
            distance = eucledian_distance(house, battery)
            distance_dict[battery] = distance

        # Only saving shortest distance 
        best_battery = min(distance_dict, key = distance_dict.get)
        best_option_dict[house] = best_battery

    return best_option_dict

def greedy_distance(batteries, houses):
    '''
    '''
    min_distance_dict = min_distance(batteries, houses)

    for house in houses:
        
        capacity_check_passed = False

        while capacity_check_passed == False:
            house.battery = min_distance_dict[house]
        
            if capacity_check(house) == True:
                house.cables = random_cables(house)
                capacity_check_passed = True  

            else:
                # Remove selected battery from dictionary
                min_distance_dict[house].pop()

    
        

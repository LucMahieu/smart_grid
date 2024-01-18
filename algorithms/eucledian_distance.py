import math
import random
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
    Saves dictionary with closest battery option for each house
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

def closest_connection(batteries, houses):
    '''
    Connects a house to the closest battery with enough capacity left
    '''
    #min_distance_dict = min_distance(batteries, houses)
    houses_copy = copy.deepcopy(houses)
    
    # Shuffle the copied list
    random.shuffle(houses_copy)

    for house in houses_copy:

        # Create a new list to store batteries with enough capacity
        batteries_with_capacity = []

        for battery in batteries:
            
            # Check if battery has enough capacity
            enough_capacity = battery.check_capacity(house)

            if enough_capacity:
                batteries_with_capacity.append(battery)

        # Use batteries with enough capacity to calculate distance
        # for battery in batteries_with_capacity
        if batteries_with_capacity:
        
            # Connecting to closest battery
            min_distance_dict = min_distance(batteries_with_capacity, houses)
            house.battery = min_distance_dict[house]

            # Updating capacity
            house.battery.update_capacity(house)

        # # Updating capacity if there is enough for new connection
        # if house.battery.check_capacity(house) == True:
        #     house.battery.update_capacity(house)

        # # Removing battery as option if not enough capacity and repeating process
        # else:
        #     batteries_copy = copy.deepcopy(batteries)
        #     batteries_copy.pop(batteries_copy.index(house.battery))
        #     min_distance_dict = min_distance(batteries_copy, houses)
        #     house.battery = min_distance_dict[house]
        
        # capacity_check_passed = False

        # while capacity_check_passed == False:
        #     house.battery = min_distance_dict[house]
        
        #     if capacity_check(house) == True:
        #         house.cables = random_cables(house)
        #         capacity_check_passed = True  
        #         house.battery.capacity = update_capacity(house):

        #     else:
        #         # Remove selected battery from dictionary
        #         min_distance_dict[house].pop()

    
        
# def min_distance(batteries, houses):
#     '''
#     Saves dictionary with closest battery option for each house
#     '''
#     best_option_dict = {}
#     for house in houses:
#         distance_dict = {}
#         for battery in batteries:
#             distance = eucledian_distance(house, battery)
#             distance_dict[battery] = distance

#         # Saving order of distances
#         sorted_batteries = sorted(distance_dict, key=distance_dict.get)
#         best_option_dict[house] = sorted_batteries 

#     return best_option_dict
            
# def closest_connection(batteries, houses):
#     '''
#     Connects a house to the closest battery with enough capacity left
#     '''
#     min_distance_dict = min_distance(batteries, houses)
#     houses_copy = copy.deepcopy(houses)
    
#     # Shuffle the copied list
#     random.shuffle(houses_copy)

#     for house in houses_copy:
#         for battery in min_distance_dict[house]:

#             # Updating capacity if there is enough for new connection
#             if house.battery.check_capacity(house) == True:
#                 house.battery.update_capacity(house)
                
#                 # Connecting to closest battery
#                 house.battery = min_distance_dict[house]

#             # Removing battery as option if not enough capacity and repeating process
#             else:
#                 batteries_copy = copy.deepcopy(batteries)
#                 batteries_copy.pop(batteries_copy.index(house.battery))
#                 min_distance_dict = min_distance(batteries_copy, houses)
#                 house.battery = min_distance_dict[house]
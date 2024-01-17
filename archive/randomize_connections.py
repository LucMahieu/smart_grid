import random

def random_assignment(district):
    '''
    Randomly assign each house to a battery that meets the requirements
    '''

    for house in district.houses:        
        # make copy of batteries list to keep track of batteries that have been tried
        batteries = district.batteries.copy()

        # set enough_capacity to False to start while loop
        enough_capacity = False

        # keep selecting random battery until a battery with enough capacity is found
        while enough_capacity == False:

            if len(batteries) == 0:
                print("No battery has enough capacity")
                break

            # select random battery from shrinking list of batteries
            selected_battery = random.choice(batteries)

            # check if battery has enough capacity
            enough_capacity = selected_battery.capacity_check(house)

            # remove battery from list of batteries because it doesn't have enough capacity
            batteries.remove(selected_battery)

        # add current house to the list of houses that are connected to the selected battery
        district.battery_houses_connections[selected_battery].append(house)

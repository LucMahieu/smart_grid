import csv
from classes.cable import Cable
from classes.battery import Battery
from classes.house import House


class District():
    def __init__(self, name, battery_file, house_file, grid_size=50):
        self.name = name
        self.houses = []
        self.batteries = []
        self.add_houses(house_file)
        self.add_batteries(battery_file)
        self.district_cost_seperate = 0
        self.district_cost_shared = 0
        self.cable_price = 9
        self.grid_size = grid_size


    def add_houses(self, house_file):
        """
        This function reads the given file, and adds the house attributes to the list of houses.
        """
        with open(house_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            # Add coordinates and output house
            for row in csv_reader:
                pos_x, pos_y, max_output = row
                self.houses.append(House(int(pos_x), int(pos_y), float(max_output)))
        
    def add_batteries(self, battery_file):
        """
        This function reads the given file, and adds the battery attributes to the list of battries.
        """        
        with open(battery_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            # Add coordinates and capacity battery
            for row in csv_reader:
                capacity = row[1]
                pos_x, pos_y = row[0].split(",")
                self.batteries.append(Battery(int(pos_x), int(pos_y), float(capacity)))

    def own_costs(self):
        '''
        Calculates cost when cables are not shared.
        '''
        cablesegment_counter = 0

        for house in self.houses:

            # Counting amount of segments based on list of cable coordinates
            cablesegment_counter += len(house.cables) - 1

        # Calculating price of district based on amount of cablesegments and batteries
        self.district_cost_seperate = cablesegment_counter * self.cable_price + len(self.batteries) * house.battery.price

    def shared_costs(self):
        '''
        Calculates cost when cables are shared.
        '''
        cablecoordinates_list = []

        for house in self.houses:

            # Creating list of all cablecoordinates
            cablecoordinates_list.append(house.cables)
            
        # Turning list of cablecoordinates into list of cablesegments
        cablesegment_list = [tuple(cablecoordinates_list[i] + cablecoordinates_list[i+1]) for i in range(len(cablecoordinates_list)-1)]

        # Excluding duplicates where cable is shared
        cablesegment_counter = len(set(cablesegment_list))
            
        # Calculating price of district based on amount of cablesegments and batteries
        self.district_cost_shared = cablesegment_counter * self.cable_price + len(self.batteries) * house.battery.price
import csv
from classes.cable import Cable
from classes.battery import Battery
from classes.house import House


class District():
    def __init__(self, name, battery_file, house_file):
        self.name = name
        self.houses = []
        self.batteries = []
        self.add_houses(house_file)
        self.add_batteries(battery_file)
        self.district_price_seperate = 0
        self.district_price_shared = 0
        self.cablesegment_price = 9
        self.battery_houses_connections = {battery: [] for battery in self.batteries}

    def add_houses(self, house_file):
        """
        This function reads the given file, loads the information about houses, and creates a list
        """
        with open(house_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            for row in csv_reader:
                pos_x, pos_y, max_output = row
                self.houses.append(House(int(pos_x), int(pos_y), float(max_output)))
        
    def add_batteries(self, battery_file):
        """
        This function reads the given file, loads information about batteries, and creates a list
        """        
        with open(battery_file, 'r') as input_file:
            # Read csv file and split 
            csv_reader = csv.reader(input_file, delimiter=',')

            # Skipping header
            next(csv_reader, None)
            
            for row in csv_reader:
                capacity = row[1]
                pos_x, pos_y = row[0].split(",")
                self.batteries.append(Battery(int(pos_x), int(pos_y), float(capacity)))

    def own_costs(self):
        '''
        Calculates price when cables are not shared.
        '''
        cablesegment_counter = 0

        for battery in self.batteries:
            for house in battery.houses:
                # Counting amount of segments based on list of cable coordinates
                cablesegment_counter += len(house.cables) - 1

            # Calculating price of district based on cablesegments and batteries
            self.district_price_seperate += cablesegment_counter * self.cablesegment_price + len(self.batteries) * battery.price

    def shared_costs(self):
        '''
        Calculates costs when cables are shared.
        '''
        cablecoordinates_list = []

        for battery in self.batteries:
            for house in battery.houses:
                # Adding segments to list, excluding final battery coordinate
                cablecoordinates_list.append(house.cables[:-1])
            
            # Turning list of cablecoordinates into list of cablesegments
            cablesegment_list = [cablecoordinates_list[i] + cablecoordinates_list[i+1] for i in range(len(cablecoordinates_list)-1)]

            # Excluding duplicates where cable is shared
            cablesegment_counter = len(set(cablesegment_list))
            
            # Calculating price of district based on cablesegments and batteries
            self.district_price_shared += cablesegment_counter * self.cablesegment_price + len(self.batteries) * battery.price

    def total_costs(self):
        '''
        Calculates total cost.
        '''
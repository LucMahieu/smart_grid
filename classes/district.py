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
        self.costs_shared = 0
        self.battery_houses_connections = {battery: [] for battery in self.batteries}

    def add_houses(self, house_file):
        """
        This function reads the given file, loads the information about houses, and creates a list
        """
        with open(house_file, 'r') as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')

            # skipping header
            next(csv_reader, None)
            
            for row in csv_reader:
                pos_x, pos_y, max_output = row
                self.houses.append(House(int(pos_x), int(pos_y), float(max_output)))

        
    def add_batteries(self, battery_file):
        """
        This function reads the given file, loads information about batteries, and creates a list
        """        
        with open(battery_file, 'r') as input_file:
            # read csv file and split on commas
            csv_reader = csv.reader(input_file, delimiter=',')

            # skipping header
            next(csv_reader, None)
            
            for row in csv_reader:
                capacity = row[1]
                pos_x, pos_y = row[0].split(",")
                self.batteries.append(Battery(int(pos_x), int(pos_y), float(capacity)))
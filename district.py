import csv
from battery import Battery
from house import House

class District():
    def __init__(self, battery_file, house_file):
        self.houses = []
        self.batteries = []
        self.houses = self.add_houses(house_file)
        self.batteries = self.add_batteries(battery_file)

    def add_houses(self, house_file):
        """
        This function reads the given file, loads the information about houses and creates a list
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
        This function reads the given file, load information about batteries and creates a list
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
    

import csv
from battery import Battery
from house import House

class District():
    def _init_(self, battery_file, house_file):
        self.houses = self.add_houses(house_file)
        self.batteries = self.add_batteries(battery_file)

    def add_houses(self, house_file):
        """
        This function reads the given file, loads the information about houses and creates a list
        """
        with open(house_file, 'r') as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')

            for row in csv_reader:
                row = row.split(',')
                self.houses.append(house.House(int(row[0]), int(row[1]), float(row[2])))

        
    def add_batteries(self, battery_file):
        """
        This function reads the given file, load information about batteries and creates a list
        """        
        with open(battery_file, 'r') as input_file:
            # read csv file and split on commas
            csv_reader = csv.reader(input_file, delimiter=',')

            for row in csv_reader:
                position, capacity = row.split(',')
                pos_x, pos_y = int(position.split(","))
                self.batteries.append(battery.Battery(pos_x, pos_y, float(capacity)))
    


import csv
from classes.cable import Cable
from classes.battery import Battery
from classes.house import House
from classes.cable import Cable


class District():
    def __init__(self, battery_file, house_file):
        self.houses = []
        self.batteries = []
        self.battery_houses_connections = {}
        self.add_houses(house_file)
        self.add_batteries(battery_file)
        self.costs_shared = 0
        self.cables = self.create_cables()

    def add_houses(self, house_file):
        """
        This function reads the given file, loads the information about houses, and creates a list
        """
        with open(house_file, 'r') as input_file:
            csv_reader = csv.reader(input_file, delimiter=',')

            # skipping header
            next(csv_reader, None)
            
            for row in csv_reader:
                pos_x_house, pos_y_house, max_output = row
                self.houses.append(House(int(pos_x_house), int(pos_y_house), float(max_output)))

        
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
                pos_x_batt, pos_y_batt = row[0].split(",")
                self.batteries.append(Battery(int(pos_x_batt), int(pos_y_batt), float(capacity)))


    def create_cables(self):
        """
        This function creates cables based on the connection between houses and batteries
        """
        cables = []
        for house in self.houses:
            # Check if the house has a battery
            if house.battery:
                cable = Cable(
                    (house.pos_x, house.pos_y),
                    (house.battery.pos_x, house.battery.pos_y)
                )
                cables.append(cable)

                # Update connected_cables in Battery
                house.battery.connected_cables.append(cable)

        return cables


if __name__ == "__main__":
    pass

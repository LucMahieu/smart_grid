import csv
from code.classes.battery import Battery
from code.classes.house import House


class District():
    def __init__(self, name, battery_file, house_file):
        self.name = name
        self.houses = []
        self.batteries = []
        self.add_houses(house_file)
        self.add_batteries(battery_file)
        self.district_cost_shared = 0
        self.cable_price = 9 
        self.battery_houses_connections = {battery: [] for battery in self.batteries}
        self.invalid = 0

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
        This function reads the given file, and adds the battery attributes to the list of batteries.
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
    
    def shared_costs(self):
        """
        Calculates cost when cables are shared.
        """
        for battery in self.battery_houses_connections:
            # Creating new list to store all cable coordinates per battery
            cablecoordinates_list = []

            for house in self.battery_houses_connections[battery]:
                if house.battery is None:
                    # Exit immediately if any house is not connected to a battery
                    return   

                for cable in house.cables:
                    cablecoordinates_list.append(cable)

            # Count shared cablesegments per battery and remove duplicates
            cablesegment_list = [tuple(cablecoordinates_list[i] + cablecoordinates_list[i+1]) for i in range(len(cablecoordinates_list)-1)]
            cablesegment_counter = len(set(cablesegment_list))

            # Calculate price of shared cablesegments 
            self.district_cost_shared += cablesegment_counter * self.cable_price 
        
        # Add battery price to calculated cost
        self.district_cost_shared += len(self.batteries) * self.batteries[0].price

        return self.district_cost_shared

    def reset_state(self):
        """
        Resetting variables.
        """
        for house in self.houses:
            house.reset()

        for battery in self.batteries:
            battery.reset_capacity()

        # Reinitialize shared cost and battery-house connections
        self.district_cost_shared = 0
        self.battery_houses_connections = {battery: [] for battery in self.batteries}

        # Reset invalid solution flag
        self.invalid = 0
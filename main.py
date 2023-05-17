def main():

    #create parent class
    class vehicle:

        def set_make(self, make):
            self.make = make

        def set_model(self, model):
            self.model = model

        def display_option(self):
            print(f"\nThe make is: {self.make}")
            print(f"The model is: {self.model}")

    #create child class that inherits from vehicle class
    class car(vehicle):

        def set_doors(self, doors):
            self.doors = doors

        def display_option(self):
            super().display_option()
            print(f"The number of doors is: {self.doors}")

    #create child class that inherits from vehicle class
    class truck(vehicle):

        def set_bed_length(self, bed_length):
            self.bed_length = bed_length

        def display_option(self):
            super().display_option()
            print(f"The bed length is: {self.bed_length}")

    print("Welcome to the Bellevue University Virtual Garage \n")

    #prompt user for the type of vehicle they wish to enter
    vehicle_type = int(input("Enter 1 to make a car, 2 to make a truck, and 3 to quit:     \n"))

    print()

    #create a new car object if user enters 1
    if vehicle_type == 1:
        new_car = car()
        new_car.set_make(input("Please enter the make: "))
        new_car.set_model(input("Please enter the model: "))
        new_car.set_doors(input("Please enter the number of doors: "))
        new_car.display_option()
        print("Your car has been added to the garage \n")
        main()

    #create a new truck object if user enters 2
    elif vehicle_type == 2:
        new_truck = truck()
        new_truck.set_make(input("Please enter the make: "))
        new_truck.set_model(input("Please enter the model: "))
        new_truck.set_bed_length(input("Please enter the length of the bed: "))
        new_truck.display_option()
        print("Your truck has been added to the garage. \n")
        main()

    #stop program if user enters 3
    elif vehicle_type == 3:
        quit
        
main()
#Hunter Vevia
#M03_Lab.py
#The program creates a parent class that hold a vehicle type and an automobile class that asks a user do define the features of a car
#vehicleType - string, stores type of vehicle | year - int, stores year of car | make - string, make of car | model - string, model of car | doors - int,number of doors | roof - string, stores type of roof | x - automobile object, stores the created automobile object

class Vehicle:
    def __init__(self):
        self.vehicleType = input("What kind of vehicle is it? (car, truck, plane, boat, or a broomstick)")
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        if(self.vehicleType.lower() != "car"): ##only accepts cars to continue creating the automobile
            return
        self.year = int(input("What is the year of the " + str(self.vehicleType) +"? "))
        self.make = input("What the the make of the " + str(self.vehicleType) + "? ")
        self.model = input("What the the model of the " + str(self.vehicleType) + "? ")
        self.doors = int(input("How many doors does it have? "))
        self.roof = input("Does it have a solid roof or sun roof? ")
    
    def __str__(self):
        string = "\nVehicle type: " + str(self.vehicleType) +"\nYear: " + str(self.year) + "\nMake: " + str(self.make) + "\nModel: " + str(self.model) + "\nNumber of doors: " + str(self.doors) + "\nType of roof: " + str(self.roof) + "\n"
        return string
    
x = Automobile()
print(x)
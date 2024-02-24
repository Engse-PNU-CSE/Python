class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0
        self.gasTank = 0
    
    def getDescriptiveName(self):
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()
    
    def readOdometer(self):
        print(f"This car has {self.odometerReading} miles on it")

    def updateOdometer(self, milegae):
        if milegae >= self.odometerReading:
            self.odometerReading = milegae
        else:
            print("You can't roll back an odometer!")
    
    def incrementOdometer(self, miles):
        self.odometerReading += miles

    def fillGastank(self, addGas):
        self.gasTank += addGas

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fillGastank(self):
        print("This car doesn't have a gas tank!")

class Battery:
    def __init__(self, batterySize=40):
        self.batterySize = batterySize

    def decribeBattry(self):
        print(f"This car has a {self.batterySize}-kWh battery.")

    def getRange(self):
        if self.batterySize == 40:
            range = 150
        elif self.batterySize == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

myLeaf = ElectricCar('nissan', 'leaf', '2024')
print(myLeaf.getDescriptiveName())
myLeaf.battery.decribeBattry()
myLeaf.fillGastank()
myLeaf.battery.getRange()
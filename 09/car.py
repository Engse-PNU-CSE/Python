class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0
    
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


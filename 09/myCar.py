from car import Car

myNewCar = Car('kia', 'k9', '2021')
print(myNewCar.getDescriptiveName())
myNewCar.odometerReading = 23
myNewCar.readOdometer()
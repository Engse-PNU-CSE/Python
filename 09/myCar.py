from car import Car

myNewCar = Car('kia', 'k9', '2021')
print(myNewCar.get_descriptive_name())
myNewCar.odometer_reading= 23
myNewCar.read_odometer()

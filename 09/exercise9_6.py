from exercise9_1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
      super().__init__(restaurant_name, cuisine_type)
      self.flavors = flavors
    
    def discribe_flavors(self):
       print(f"This Icecream is {self.flavors} icecream")
       print("this is {}".format(self.flavors))
       print("this is {}, {}, {}".format(self.flavors, "1", "2"))

myic = IceCreamStand("Italy", "pizza", "Cookies and Cream")
myic.discribe_flavors()

# pandas, numpy, skelaton, pyporch
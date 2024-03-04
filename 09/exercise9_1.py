class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
      self.restaurant_name = restaurant_name
      self.cuisine_type = cuisine_type
    def discribe_restaurant(self):
       print(f"Restaurant_name : {self.restaurant_name}, Cuision_type : {self.cuisine_type}")

    def open_restaurant(self):
       print(f"{self.restaurant_name} is open")

class User:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname
        self.__price = 4_000
    def describe_user(self):
        fullname = f"{self.fname} {self.lname}"
        print(f"Name : {fullname}")
    def greet_user(self):
       print(f"welcome, {self.fname} {self.lname}")


my_restaurant = Restaurant("kim", "korean")
print(my_restaurant.restaurant_name, my_restaurant.cuisine_type, my_restaurant._Restaurant__price)
my_restaurant.discribe_restaurant() 
my_restaurant.open_restaurant()

engse = User("kim", "seyoung")
engse.describe_user()
engse.greet_user()
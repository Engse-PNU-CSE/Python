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
    def describe_user(self):
        fullname = f"{self.fname} {self.lname}"
        print(f"Name : {fullname}")
    def greet_user(self):
       print(f"welcome, {self.fname} {self.lname}")
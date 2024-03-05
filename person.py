class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.weight = 50 #public attribute
        self.__vision = 1.0 #private attribute
    
    def show_person_vision(self):
        print("{}'s vision is {}".format(self.name, self.__vision))

    def __str__(self): #tostring() method -> return type is String
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    

new_person = Person('kim', 30, 'busan')
print("this person {}".format(new_person.name))
print("{}'s weight is {}".format(new_person.name, new_person.weight))
new_person.show_person_vision()
print(str(new_person))
print(new_person.__str__())
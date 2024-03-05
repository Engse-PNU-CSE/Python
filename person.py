class Person:
    count = 0 # class attribute
    def __init__(self, name, age, address): #constructor
        self.name = name #field attribute
        self.age = age
        self.address = address
        self.weight = 50 #public attribute
        self.height = 170
        self.__vision = 1.0 #private attribute
        self.mylist = [1, 2, 3, 4]
        print("create {} object".format(self.name))
        Person.count += 1 ##increase class attribute
    
    def show_person_vision(self):
        print("{}'s vision is {}".format(self.name, self.__vision))

    def __str__(self): #tostring() method -> return type is String
        return "{}\t{}\t{}".format(self.name, self.age, self.address)
    
    def __len__(self):
        return len(self.mylist)+2
    
    def __eq__(self, other):
        return self.address == other.address
    
    def __call__(self):
        return int(self.height**2/100)/self.weight
    
    def __getitem__(self, index):
        return self.mylist[index]
    
    def __del__(self):
        print("delele {} object".format(self.name))

    @classmethod #decorator -> annotation
    def printing(cls): #cls : class
        print("object count : {}".format(cls.count))

Person("guest", 25, "Seoul")  
Person.printing()
Person("asdf", 12, "!@#")
new_person = Person('kim', 30, 'busan')

print(f"person object's age is : {new_person.age:5}")    

print("this person {}".format(new_person.name))
print("{}'s weight is {}".format(new_person.name, new_person.weight))
new_person.show_person_vision()
print(new_person())
print(type(new_person), isinstance(new_person, Person))
print(new_person[3])
print(new_person.count)

new_person.printing()
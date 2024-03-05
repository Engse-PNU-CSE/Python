class Shape:
    def __init__(self, base, height):
        self.__base = base

    @property
    def get_base(self):
            return self.__base
    
    @height.setter
    def height(self, value):
        self.__height = value

def get_data():
    return 1, 2, 3


_, a, b = get_data()
print(a, b)

a=[1, 2, 3]
b=[3, 4, 5]
mylist = [*a, *b]
print(mylist)
c=['a', 'b']
z=zip(a, c)
print(list(z))
###getter, setter를 정의하는데 decorator 사용

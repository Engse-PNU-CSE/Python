from exercise9_1 import User

class Privileages():
    def show_privileages(self):
        print(Privileages.privileages)

    def __init__(self, privileages):
        self.privileages = privileages

class Admin(User):

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.privileages = Privileages()

    

a = Admin("kim", "engse")
a.greet_user()
a.privileages("asdf")
a.privileages.show_privileages()

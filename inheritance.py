class BaseClass:
    def __init__(self):
        print("Base init")

    def set_name(self, name):
        self.name = name
        print("Base class set name: ")

class SubClass(BaseClass):

    def __init__(self):
        super().__init__( )
        print("Subclass  init")

    def set_name(self, name):
        self.name = name
        print("subclass set name")

    def welcome(self):
        print("Welco me")

    def display_name(self):
        print("Name  : " + self.name)


y = SubClass()

y.welcome()
y.set_name("sarath")
y.display_name()

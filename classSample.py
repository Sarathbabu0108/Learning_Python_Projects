
class TeamMember:
    year = 2020
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    def add_age(self):
        self.age = self.age+1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year : " + str(TeamMember.year))
        print("Name : " +self.name)
        print("Age : " + str(self.age))
        print("Place : " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year+1



x = TeamMember("Sarath", 27, "poonjar")
y = TeamMember("syam", 31, "kottayam")

x.display()
y.display()

print("-------------------------------")


TeamMember.year = TeamMember.year+1

x.add_age()
y.add_age()
x.display()
y.display()

print("------------------------------------")

TeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("Delhi")
y.relocate("Mumbai")
x.display()
y.display()
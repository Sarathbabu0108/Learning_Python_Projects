class sample:
    def set_name(self,name):
        self.name = name
    def __add__(self, other):
        name=self.name + other.name
        return name


first_name = sample()
second_name = sample()

first_name.set_name("Sarath")
second_name.set_name("Babu")

full_name = first_name + second_name

print("Name : " + full_name)


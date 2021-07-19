class First:
    def display(self):
        print("First")


class Second:
    def display(self):
        print("Second")


class Third(Second, First):
    def display(self):
        print("Third")


x = Third()
#x.display_Third()
x.display()

print(Third.mro())


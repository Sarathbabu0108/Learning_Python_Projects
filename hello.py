
b = 1.2
try:
    a = 10/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("cant divided by zero")
print("program completed")
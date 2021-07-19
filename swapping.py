number1 = float(input("Enter  number1: "))
number2 = float(input("Enter number2: "))
# This is my sample comment
print(type(number1))
print(type(number2))

temp = number1
number1 = number2
number2 = temp

print("Result after swapping is: ")
print("The value for number1 : " + str(number1))
print("The value for number2 : " + str(temp))

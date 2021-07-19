number1 = float(input("Enter two numbers : "))
number2 = float(input())
choice = int(input("1)Addition\n2)Multiplication\n3)Division\n4)Substraction\nEnter your choice : "))
if choice == 1:
    result = number1 + number2
    print("Result is : " + str(result))
elif choice == 2:
    result = number1 * number2
    print("Result is : " + str(result))
elif choice == 3:
    result = number1/number2
    print("Result is : " + str(result))
elif choice == 4:
    result = number1 - number2
    print("Result is : " + str(result))
else:
    print("Please enter the correct choice")
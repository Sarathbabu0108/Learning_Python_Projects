num1 = int(input("Enter three numbers\n"))
num2 = int(input())
num3 = int(input())
if num1 > num2:
    if num1 > num3:
        print("The greater number is num1 " + str(num1))
    else:
        print("The greater number is num3 " + str(num3))
elif num2 > num3:
    print("The greater number is num2 " + str(num2))
else:
    print("The greater number is num3  " + str(num3))

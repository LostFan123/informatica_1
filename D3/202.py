# 1. We have tools to avoid code duplication: 
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))
number5 = int(input("Enter the fifth number: "))
number6 = int(input("Enter the sixth number: "))
number7 = int(input("Enter the seventh number: "))
number8 = int(input("Enter the eighth number: "))
number9 = int(input("Enter the nineth number: "))
number10 = int(input("Enter the tenth number: "))
finalnumber=(number1+number2+number3+number4+number5+number6+number7+number8+number9+number10)
print(finalnumber)

# Possible solution:
counter = 0
total = 0
while counter != 10:
    total += float(input("Number: "))
    counter += 1
print(total)

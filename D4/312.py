# Good solution, but avoid repeating logic 
number = int(input("Enter a number: "))
counter = 0
while counter < 2 and number != 0:
    digit = number % 10
    if digit % 2 == 0:
        counter = counter + 1
        number = number // 10  # this is repeated twice
    else:
        number = number // 10
if counter == 2:
    print("There are at least 2 even digits")
else:
    print("There are no 2 even digits")

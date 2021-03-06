number = float(input("Number: "))
exponent = int(input("Exponent: "))
result = 1
counter = 0
while counter < exponent:
    result *= number
    counter += 1
print(f"{number} ** {exponent} == {result}")

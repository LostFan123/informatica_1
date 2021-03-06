number = float(input("Number: "))
exponent = int(input("Exponent: "))
if exponent < 0:
    raise ValueError("Exponent must be a positive integer")  # A better alternative to `exit()`
result = 1
counter = 0
while counter < exponent:
    result *= number
    counter += 1
print(f"{number} ** {exponent} == {result}")

# Possible solution. Using a flag variable to stop the loop.
number = int(input("Number: "))
divisor = 2
divisor_is_found = False
while divisor != number and not divisor_is_found:
    if number % divisor == 0:
        divisor_is_found = True
    divisor += 1
if divisor_is_found:
    print(f"{number} is not prime")
else:
    print(f"{number} is prime")

# 1. We don't need to continue looping if we already found out that the number is not a prime.
#    Failing example: 12
number = int(input("Number: "))
divisor = number - 1
while divisor > 1:
    if number % divisor == 0:
        print(f"{number} is not a prime")  # <- If we reach here, the loop should stop
    divisor -= 1
print(f"{number} is prime")  # <- This will be executed always. Not what we want!

# Possible solution. Using a **flag variable** to stop the loop.
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

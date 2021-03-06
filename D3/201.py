# 1. We don't need to continue looping if we already found out that the number is not a prime.
#    Failing example: 12
number = int(input("Number: "))
divisor = number - 1
while divisor > 1:
    if number % divisor == 0:
        print(f"{number} is not a prime")  # <- If we reach here, the loop should stop
    divisor -= 1
print(f"{number} is prime")  # <- This will be executed always. Not what we want!

# 2. Similar problem. We don't need to go over all possible divisors:
number = int(input("Number: "))
divisor = number - 1
is_prime = True
while divisor > 1:
    if number % divisor == 0:
        is_prime = False
        #  print("We found that it's not a prime")
    divisor -= 1
    #  print(divisor)
if is_prime:
    print("Prime!")
else:
    print("Not prime!")
    
# 3. Setting the flag variable `is_prime` to `True` will give incorrect results.
#    Failing example: 9
number = int(input("N: "))
divisor = number - 1
is_prime = True
while divisor > 1:
	if number % divisor == 0:
		is_prime = False
	else:
		is_prime = True
	divisor = divisor - 1
if is_prime:
	print(f"{number} is a prime number.")
else:
	print(f"{number} is not a prime number.")

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

# Task:
#   Write a program that reads from keyboard 1 number and informs if this number is a prime
#   number or not. To test if a number is prime or not you have to loop over all its possible divisors. If
#   no divisor is found (other than 1 or the self number) then it is prime
# Note: there are still more efficient ways to solve this task, but for simplicity we are not going to discuss them.

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = int(input("Number: "))
divisor = 2
divisor_is_found = False
while divisor != number // 2 and not divisor_is_found:
    if number % divisor == 0:
        divisor_is_found = True
    divisor += 1
if divisor_is_found:
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
    
# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using for-else loop construct.
number = int(input("Number: "))
for divisor in range(2, number // 2 + 1):
    if number % divisor == 0:
        print(f"{number} is not a prime number")
        break
else:
    print(f"{number} is a prime number")  # this line will be executed only if the loop was not stopped by `break`
    
# ------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. We don't need to continue looping if we already found out that the number is not a prime.
# 2. The choice of the initial divisor as `number - 1` is not optimal. 
#    If the number is 1000, it's better to start iterating from 2 and up than from 999 and down.
number = int(input("Number: "))
divisor = number - 1
while divisor > 1:
    if number % divisor == 0:
        print(f"{number} is not a prime")  # <- If we reach here, the loop should stop
    divisor -= 1
print(f"{number} is prime")  # <- This will be executed always. Not what we want!
    
# 2. Setting the flag variable `is_prime` to `True` will give incorrect results.
#    Failing example: 9
number = int(input("N: "))
divisor = number - 1
is_prime = True
while divisor > 1:
	if number % divisor == 0:
		is_prime = False
	else:
		is_prime = True  # this will be executed for number == 9 and divisor == 2, which is the divisor of the last iteration
	divisor = divisor - 1
if is_prime:
	print(f"{number} is a prime number.")
else:
	print(f"{number} is not a prime number.")

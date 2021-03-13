# Task:
#   Write a program that calculates the sum of all the divisors of a positive integer number X
#   introduced from keyboard. Remember that Y is a divisor of X if Y<X and the remainder of the
#   integer division is 0.

# ------------------------------------------------------------------------------------------------
# Possible solution:
number = int(input("Number: "))
divisor = 2
divisors_sum = 0
while divisor <= number // 2:
    if number % divisor == 0:
        print("Divisor:", divisor)
        divisors_sum += divisor
    divisor += 1
print("Sum of the divisors:", divisors_sum)

# Or if for-loop is allowed:
number = int(input("Number: "))
divisors_sum = 0
for divisor in range(2, number // 2 + 1):
    if number % divisor == 0:
        print("Divisor:", divisor)
        divisors_sum += divisor
print("Sum of the divisors:", divisors_sum)

# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using `sum` with a generator expression passed to it as an argument.
number = int(input("Number: "))
divisors_sum = sum(divisor for divisor in range(2, number // 2 + 1)
                   if number % divisor == 0)
print("Sum of the divisors:", divisors_sum)

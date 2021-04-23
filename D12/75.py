# Task:
#   Write a procedure to print on the screen the first n primes numbers. The procedure receives n as
#   an argument. Create a function to see if a number is prime or not and use that function to call the
#   procedure.

# -----------------------------------------------------------------------------------------------------
# Possible solution:
# (not the most optimal, though. For that check https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# or this monster: https://stackoverflow.com/a/10733621/7851470 which I didn't even try to understand.)
def primes(n):
    primes_found = 0
    candidate = 2
    while primes_found != n:
        if is_prime(candidate):
            print(candidate)
            primes_found += 1
        candidate += 1
    
    
def is_prime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True

# Usage example:
primes(10)


# -----------------------------------------------------------------------------------------------------
# Advanced solution.
#   Not trying to improve the efficiency.
#   Adding type hints.
#   Using `itertools.count` to generate numbers 2, 3, 4, .... See: https://docs.python.org/3/library/itertools.html#itertools.count
#   Using built-in function `filter` to get from those numbers only the primes. See: https://docs.python.org/3/library/functions.html#filter
#   and https://docs.python.org/3/howto/functional.html#built-in-functions
#   Using `itertools.islice` to get only the first N numbers from `filter(is_prime, count(2))`.
#   See: https://docs.python.org/3/library/itertools.html#itertools.islice
#   Using `all` built-in to check if a number is prime: https://docs.python.org/3/library/functions.html#all
from itertools import count, islice

def primes(n: int) -> None:
    for prime in islice(filter(is_prime, count(2)), n):
        print(prime)

        
def is_prime(number: int) -> bool:
    return all(number % divisor for divisor in range(2, number // 2 + 1))

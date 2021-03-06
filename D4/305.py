# 1. Shadowing built-in `sum` function. 
# 2. The task was calculate the sum of numbers from 1 to N, not a sum of digits of some number.
n = int(input("Enter a number: "))
sum = 0
while n != 0:
    n2 = n % 10
    if n2 % 2 == 0 or n2 % 5 == 0:
        sum = sum + n2
    n = n // 10
print("The sum of the even number and multiples of 5 is ", sum)

# Possible solution:
n = int(input("Enter a number: "))
result = 0
counter = 1
while counter <= n:
    if counter % 2 == 0 or counter % 5 == 0:
        print(counter)
        result += counter
    counter += 1
print("Result:", result)

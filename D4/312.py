# 1. No need to count odd digits.
# 2. Incorrect order of calculating quotient and remainder - n gets overwritten before we get the first digit.
#    Failing example: 21
n = int(input("Tell me a number: "))
even = 0
odd = 0
while (n>0):
    n = n//10
    if ((n%10)%2 == 0):
        even = even + 1
    else: 
        odd = odd + 1
if (even == 2):
    print("This number has 2 even digits")
elif (even > 2):
    print("This number has more than 2 even digits")
else:
    print("This number has no even digits")

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

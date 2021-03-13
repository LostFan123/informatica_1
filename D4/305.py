# Task:
#   Calculate the sum of all numbers from 1 to n that are even or multiple of 5. 

# ------------------------------------------------------------------------------------------------
# Possible solution:
n = int(input("Enter a number: "))
result = 0
counter = 1
while counter <= n:
    if counter % 2 == 0 or counter % 5 == 0:
        result += counter
    counter += 1
print("Result:", result)

# or if for-loop is allowed:
n = int(input("Enter a number: "))
result = 0
for counter in range(2, n + 1):
    if counter % 2 == 0 or counter % 5 == 0:
        result += counter
print("Result:", result)

# Alternatively, we don't even need to loop. 
# The following equations can be derived from the sum of arithmetic sequence:
n = int(input("Enter a number: "))
even_count = n // 2
even_sum = even_count * (even_count + 1))  # 2 + 4 + ...
rest_count = (n + 5) // 10  # divisible by five but not even
rest_sum = 5 * rest_count * rest_count  # 5 + 15 + 25 + ...
print("Result:", even_sum + rest_sum)

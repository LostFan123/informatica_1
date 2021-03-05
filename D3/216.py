# Possible solution:
first = 1
print(first)
second = 2
counter = 1
while counter < 20:
    print(second)
    temp = first + second
    first = second
    second = temp
    counter += 1

# Improvement: temporary variable can be avoided
first = 1
print(first)
second = 2
counter = 1
while counter < 20:
    print(second)
    second = first + second
    first = second - first
    counter += 1

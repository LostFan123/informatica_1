# possible solution without using temporary variables
first = 1
second = 2
counter = 2
print(first)
print(second)
while counter != 20:
    second = first + second
    first = second - first
    print(second)
    counter += 1

# Task:
#   Suppose we have a file 'people.txt' with data related to personal information. Each line in the
#   file contains the following information: person's name and, number of working hours separated with
#   a space character. Create a program to ask the user to enter the price of each working hour, then
#   read the file 'people.txt' and then write on a file 'payments.txt' the salary to give to each person
#   (person's name and salary, in each line separated by a space). Write in the console the number of
#   people to pay and the total quantity needed to pay them all.

# ------------------------------------------------------------------------------------------------------
# Possible solution.
# Using `file.close()`:
price = float(input("Price: "))
people_file = open("people.txt")
payments_file = open("payments.txt", 'w')
people_count = 0
total_payment = 0
for line in people_file:
    name, hours = line.split(' ')
    salary = price * int(hours)
    payments_file.write(f"{name} {salary}")
    people_count += 1
    total_payment += salary
people_file.close()
payments_file.close()
print(people_count, total_payment)

# Using `with` keyword:
price = float(input("Price: "))
with open("people.txt") as people_file, open("payments.txt", 'w') as payments_file:
    people_count = 0
    total_payment = 0
    for line in people_file:
        name, hours = line.split(' ')
        salary = price * int(hours)
        payments_file.write(f"{name} {salary}")
        people_count += 1
        total_payment += salary
print(people_count, total_payment)

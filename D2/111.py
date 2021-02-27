# 1. Check the logic with simple test cases: 1, 4, 100, 400.
# The following will fail for 100:
year = int(input("Year: "))
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")

    
# Possible solution:
year = int(input("Enter a year: "))
if (year % 4) == 0 and not (year % 100) == 0:
    print(str(year) + " is a leap year. ")
elif year % 400 == 0:
    print(str(year) + " is a leap year. ")
else:
    print(str(year) + " is not a leap year. ")
    
# or without `elif`:
year = int(input("Enter a year: "))
if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print(str(year) + " is a leap year. ")
else:
    print(str(year) + " is not a leap year. ")

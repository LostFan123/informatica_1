# Task:
#   Write a program that reads from keyboard one year number and indicates if that year is or not
#   a leap year (bisiesto). NOTE: Leap years are those that are multiple of 4 but not multiples of
#   100, with the exception of the multiples of 400 which are leap years.

# ------------------------------------------------------------------------------------------------
# Possible solution:
year = int(input("Enter a year: "))
if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
    print(str(year) + " is a leap year. ")
else:
    print(str(year) + " is not a leap year. ")
    

# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Python already has a built-in functionality for this task.
import calendar
year = int(input("Enter a year: "))
print(calendar.isleap(year))

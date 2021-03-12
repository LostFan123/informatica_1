# Task:
#   Write a program that reads from keyboard a large number of minutes and shows how many
#   days, hours and minutes it corresponds. For example, 4565 minutes correspond to 3d, 4h, 5'.

# ------------------------------------------------------------------------------------------------

# Possible solution:
total_minutes = int(input("Enter minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
days = hours // 24
hours = hours % 24
print(total_minutes, "minutes correspond to", str(days) + "d,", str(hours) + "h,", str(m) + "'")

# to simplify the final `print` we can use f-strings (format strings):
print(f"{total_minutes} minutes correspond to {days}d, {hours}h, {minutes}'")

# In fact, calculating both the quotient and the remainder of integer division at the same time
# is so frequent that Python provides a built-in function `divmod` that returns them both at the same time:
total_minutes = int(input("Enter minutes: "))
hours, minutes = divmod(total_minutes, 60)
days, hours = divmod(hours, 24)
print(f"{total_minutes} minutes correspond to {days}d, {hours}h, {minutes}'")

# ------------------------------------------------------------------------------------------------

# Common mistakes:
# 1. Operating on floats will cause issues with precision. 
#    Failing example: 27
import math
t = int(input("Enter a quantity of minutes: "))  # Let t == 27
t_d = (t / 60) / 24  # 0.01875
t_h = (t_d - math.floor(t_d)) * 24  # 0.44999999999999996 instead of 0.45
t_m = (t_h - math.floor(t_h)) * 60  # 26.999999999999996 instead of 27
print(f"This quantity of minutes is {math.floor(t_d)}d, {math.floor(t_h)}h, {math.floor(t_m)}'")


# 2. `round()` will round the number to the closest integer, but we always need to round down.
#    Failing example: 780 (13 hours)
t = int(input("Enter a quantity of minutes: "))  # Let t == 780
t_d = t / 1440  # 0.5416666666666666
days_count = round(t_d)  # 1 instead of 0
# etc.

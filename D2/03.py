# 1. Operating on floats will cause issues with precision. Failing example: 27. (0.01875 * 24 != 0.45)
import math
t = int(input("Enter a quantity of minutes: "))
t_d = (t / 60) / 24
t_h = (t_d - math.floor(t_d)) * 24
t_m = (t_h - math.floor(t_h)) * 60
print("This quantity of minutes is " + str(math.floor(t_d)) + " d, " + str(math.floor(t_h)) + " h, " + str(math.floor(t_m)) + " m.")


# 2. `round()` will round the number up. Failing example: 780 (13 hours)
t = int(input("Enter a quantity of minutes: "))
t_d = t / 1440
days_count = round(t_d)
# ...and so on...

# 3. Use meaningful names. Something like this is very difficult to understand:
r = int(input("Number of minutes: "))
l = 60 * 24
p = 60
di = int(r / l)
rd = r % l
h = int(rd / p)
rh = rd % p
m = rh
print(str(di) + " days " + str(h) + " hours and " + str(m) + " minutes.")


# Good solution
total_minutes = int(input("Enter minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
days = hours // 24
hours = hours % 24
print(total_minutes, "minutes correspond to", str(days) + "d,", str(hours) + "h,", str(m) + "'")

# it's a good practice to take out repetetive values as variables:
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
total_minutes = int(input("Enter minutes: "))
hours = total_minutes // MINUTES_PER_HOUR
minutes = total_minutes % MINUTES_PER_HOUR
days = hours // HOURS_PER_DAY
hours = hours % HOURS_PER_DAY

# to simplify the final `print` we can use f-strings (format strings):
print(f"{total_minutes} minutes correspond to {days}d, {hours}h, {minutes}'")

# in fact, calculating both the quotient and the remainder of integer division at the same time
# is so frequent that Python provides a built-in function `divmod` that returns them both at the same time:
total_minutes = int(input("Enter minutes: "))
hours, minutes = divmod(total_minutes, 60)
days, hours = divmod(hours, 24)
print(f"{total_minutes} minutes correspond to {days}d, {hours}h, {minutes}'")

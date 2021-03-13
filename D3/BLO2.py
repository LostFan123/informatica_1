# Task:
#   The IT system of the gym encodes the exercises done by one person using a digits-code
#   of a number. Write the code to calculate and show the Kcal burned in a training session using the
#   following information:
#   code exercise desc Kcal
#   1 running 5' 50
#   2 elliptical 5' 20
#   3 lift weight 5’ 15
#   4 abdominals 30r 35
#   5 spinning 1h 180
#   EXAMPLE: The code 2343111 corresponds to 235 Kcal => a session with 15' running (150 Kcal)
#   + 10' of lift weight (30 Kcal) + abdominals (35 Kcal) + 5' elliptical (20).

# ------------------------------------------------------------------------------------------------
# Possible solution:
code = int(input("Code: "))
kcal_total = 0
while code != 0:
    digit = code % 10
    code = code // 10
    # The above two lines can be rewritten as:
    # code, digit = divmod(code, 10)
    if digit == 1:
        kcal = 50
    elif digit == 2:
        kcal = 20
    elif digit == 3:
        kcal = 15
    elif digit == 4:
        kcal = 35
    elif digit == 5:
        kcal = 180
    kcal_total += kcal
print(f"Total Kcal: {kcal_total}")

# If for-loops are allowed:
code = input("Code: ")
kcal_total = 0
for digit in code:
    if digit == '1':
        kcal = 50
    elif digit == '2':
        kcal = 20
    elif digit == '3':
        kcal = 15
    elif digit == '4':
        kcal = 35
    elif digit == '5':
        kcal = 180
    kcal_total += kcal
print(f"Total Kcal: {kcal_total}")

# ------------------------------------------------------------------------------------------------
# Advanced solution:
#   Using a dictionary.
kcal_per_digit = {'1': 50, '2': 20, '3': 15, '4': 35, '5': 180}
code = input("Code: ")
kcal_total = 0
for digit in code:
    kcal = kcal_per_digit[digit]
    kcal_total += kcal
print(f"Total Kcal: {kcal_total}")

# or the same but using a `sum` function with a generator expression passed to it as an argument:
kcal_per_digit = {'1': 50, '2': 20, '3': 15, '4': 35, '5': 180}
kcal_total = sum(kcal_per_digit[digit] for digit in input("Code: "))
print(f"Total Kcal: {kcal_total}")

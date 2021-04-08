# Task:
#   Assume having the file “person_workout.txt” with the information of the burnt Kcal by
#   the users of a gym. Write a program that reads this files and shows in screen the information of the
#   users, but only of those that burnt more than 50Kcal in their last exercise. The format of the file is
#   as following:
#   Person Name 1 320 Kcal
#   Person Name 2 50 Kcal
#   … etc
# Note: the format is not very clear, let's assume that values are tab-separated.
#       Also assuming that each person is encountered in the file just once.

# --------------------------------------------------------------------------------------------------------
# Possible solution:
with open("person_workout.txt") as file:
    for line in file:
        name, kcals = line.split('\t')
        kcals = int(kcals.split(' ')[0])  # removing the Kcal unit from the string
        if kcals > 50:
            print(name, kcals)

# --------------------------------------------------------------------------------------------------------
# Advanced solution.
# If each user can be recorded several times in the file, 
# we need to keep info on each user's last Kcals burnt somehow.
# For that, it's better to use a dictionary:
last_exercise_kcals_per_person = {}
with open("person_workout.txt") as file:
    for line in file:
        name, kcals = line.split('\t')
        last_exercise_kcals_per_person[name] = int(kcals.split(' ')[0])
for name, kcals in last_exercise_kcals_per_person.items():
    if kcals > 50:
        print(name, kcals)

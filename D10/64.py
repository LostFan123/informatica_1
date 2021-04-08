# Task:
#   Write a program that asks the user for a file name with information of the top tennis palyers and
#   shows the current top-one tennis player and his/her nationality. Each line of the file contains the
#   data of a tennis player (name, nationality, trainer's name, points, and number of won tournaments),
#   separated by commas. The top-one player is the one with more points. In case of even score, the one
#   with more tournaments will be the top-one. Modify the name on the text file (from ATP.txt to ie.
#   Top-Ten-Tennis.csv) and test that your code is still working

# -----------------------------------------------------------------------------------------------------
# Possible solution:
file_name = input("Name of file: ")
top_player_points = -1
top_player_victories = -1
with open(file_name) as file:
    for line in file:
        name, nationality, coach, points, victories = line.split(',')
        points = int(points)
        victories = int(victories)
        if points > top_player_points or points == top_player_points and victories > top_player_victories:
            top_player = name
            top_player_points = points
            top_player_victories = victories
            top_player_nationality = nationality
print(top_player, top_player_nationality)

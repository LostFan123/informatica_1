# Task:
#   Write the code that creates a new file named ATP.txt . Inside the file the program will store the
#   information obtained from keyboard about the list of the world top-ten tennis players, which is:
#   name, nationality, trainer's name, points, and number of won tournaments. Write the information of
#   each tennis player in separate line of the new file, separated by commas

# ----------------------------------------------------------------------------------------------------
# Possible solution:
with open("ATP.txt", 'w') as file:
    for index in range(1, 11):
        print(f"Enter info about player Nº{index}.")
        name = input("Name: ")
        nationality = input("Nationality: ") 
        coach = input("Trainer's name: ")
        points = input("Points: ")
        wins_count = input("Number of won tournaments: ")
        line = ','.join([name, nationality, coach, points, wins_count])
        file.write(line + '\n')

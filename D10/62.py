# Task:
#   Given a text file equipo.txt, with the following format:
#    First line has the name of a team,
#    Second line has the trainer's name,
#    from third line on, each line holds the information of a player: the dorsal number, the
#   number of scored goals and his name .
#   Write a program that reads the content of equipo.txt and creates a new file liga.txt with the
#   following content:
#    The first line should be: "El equipo <nombre_del_equipo> tiene por entrenador a
#   <nombre_del_entrenador>"
#    The following lines should be: "El jugador <nom> con dorsal <dorsal> ha marcado <goles>
#   goles"
#    The last line will be: "El equipo ha marcado en total <goles> goles, y el jugador que más
#   goles ha marcado es el que tiene como dorsal: <dorsal>".
#   The program should also write the adequate error messages for each one of the following cases:
#    Unable to find or read the input file equipo.txt
#    The file equipo.txt does not follow the established format. 
#   Note: assuming that the list of goalscorers is not empty

# -----------------------------------------------------------------------------------------------
# Posssible solution.
with open("equipo.txt") as input_file, open("liga.txt", 'w') as output_file:
    team = input_file.readline().strip()
    coach = input_file.readline().strip()
    output_file.write(f"El equipo {team} tiene por entrenador a {coach}\n")
    total_goals = 0
    most_goals = -1
    for line in input_file:
        number, goals, name = line.split(',')
        goals = int(goals)
        total_goals += goals
        if goals > most_goals:
            topscorer_number = number
        output_file.write(f"El jugador {name} con dorsal {number} "
                          f"ha marcado {goals} goles\n")
    output_file.write(f"El equipo ha marcado en total {total_goals} goles, "
                      f"y el jugador que más goles ha marcado es el "
                      f"que tiene como dorsal: {topscorer_number}")

    
# ----------------------------------------------------------------------------------------------
# Common mistakes.
# 1. Ok.. Not really a mistake, but the following is not the most concise way to write a file:
#    Asssuming `r` is a file-object, and `s` is a list with details about the player.
r.write("The player")
r.write(s[2])
r.write("with number")
r.write(s[0])
r.write("has scored")
r.write(s[1])
r.write("goals")
r.write("\n")

# 2. Using index to check for the first two lines:
...
with open("equipo.txt") as equipo:
    i = 1
    goles = 0
    maxgoals = 0
    for line in equipo:
        if i == 1:  # this will be checked on each iteration. We can avoid that.
            nombre_del_equipo= line.rstrip()
        elif i == 2:
            coach = line.rstrip()
            liga.write("El equipo " + nombre_del_equipo + " tiene por entrenador a " + coach + "\n")
        else:
            jugadores = line.split(",")
            dorsal = jugadores[0]
            goals = int(jugadores[1])
            player = jugadores[2].rstrip()
            liga.write("El jugador " + player + " con dorsal " + str(dorsal) + " ha marcado " + str(goals) + " goles" + "\n" )
            goles = goles + int(jugadores[1])

            if goals > maxgoals:
                maxgoals = goals
                maxdorsal = dorsal
        i += 1
...

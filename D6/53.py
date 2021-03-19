# Task:
#   In an experiment 3 sensors are recorded in 5 successive times. For each sample the values are
#   stored in a vector of three elements.
#   T1= [1.25, 11.5, 25.1] T2= [2.3, 15.6, 22.2 ]
#   T3= [0.7, 12.4, 28.6] T4= [1.57, 10.3, 20.3]
#   T5= [1.8, 9.9, 18.7]
#   Show a plot with points representing the values of the three variables, having in the X axis the time.

# --------------------------------------------------------------------------------------------------------
# Possible solution
import matplotlib.pyplot as plt

T1 = [1.25, 11.5, 25.1]
T2 = [2.3, 15.6, 22.2]
T3 = [0.7, 12.4, 28.6]
T4 = [1.57, 10.3, 20.3]
T5 = [1.8, 9.9, 18.7]
measurements = [T1, T2, T3, T4, T5]
sensor1 = [0] * 5
sensor2 = [0] * 5
sensor3 = [0] * 5
for i in range(len(measurements)):
    measurement = measurements[i]
    sensor1[i] = measurement[0]
    sensor2[i] = measurement[1]
    sensor3[i] = measurement[2]
plt.plot(sensor1, '-o')
plt.plot(sensor2, '-o')
plt.plot(sensor3, '-o')
plt.show()

# --------------------------------------------------------------------------------------------------------
# Advanced solution.
# Iterating over multiple lists in parallel.
# See: https://docs.python.org/3/library/functions.html#zip 
#  and https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
import matplotlib.pyplot as plt

T1 = [1.25, 11.5, 25.1]
T2 = [2.3, 15.6, 22.2]
T3 = [0.7, 12.4, 28.6]
T4 = [1.57, 10.3, 20.3]
T5 = [1.8, 9.9, 18.7]
for sensor in zip(T1, T2, T3, T4, T5):
    plt.plot(sensor, '-o')

# Task:
#   Using the following vector A with the ages of the people that assist to an event
#   A=[15, 18, 32, 7, 55, 27, 81, 44, 34, 61, 29, 33, 72, 51, 48];
#   show a plot -using function bar()- with the frequency of the ages within the intervals i1,i2, i3, i4 and
#   i5, which are defined as i1= [0 – 12] i2= [13 - 18] i3= [19 - 35] i4= [36 - 65] i5= [66+]

# ----------------------------------------------------------------------------------------------------------
# Possible solution
import matplotlib.pyplot as plt

A = [15, 18, 32, 7, 55, 27, 81, 44, 34, 61, 29, 33, 72, 51, 48]
age_limits = [66, 36, 19, 13, 0]
age_counts = [0] * len(age_limits)
for age in A:
    found = False
    i = 0
    while not found:
        if age >= age_limits[i]:
            age_counts[-i - 1] += 1
            found = True
        i += 1
xs = ['0 – 12', '13 - 18', '19 - 35', '36 - 65', '66+']
plt.bar(xs, age_counts)
plt.show()

# ----------------------------------------------------------------------------------------------------------
# Common mistakes:
# 1. Using multiple if-elif (not really a mistake, but we can avoid unnecessary repetition)
# 2. Plotting bars one by one in a loop instead of plotting them all at once.
import matplotlib.pyplot as plt
A = [15, 18, 32, 7, 55, 27, 81, 44, 34, 61, 29, 33, 72, 51, 48]
freq = [0] * 5;
n = 0
while n < len(A):
    if A[n] <= 12:
        freq[0] += 1
    elif 12 < A[n] <= 18:
        freq[1] += 1
    elif 18 < A[n] <= 35:
        freq[2] += 1
    elif 35 < A[n] <= 65:
        freq[3] += 1
    elif A[n] > 65:
        freq[4] += 1
    n += 1
n = 0
while n < len(freq):
    plt.bar(n, freq[n])
    n += 1
plt.show()

# ----------------------------------------------------------------------------------------------------------
# Advanced solution.
# Using `numpy.histogram` to count values inside the given bins.
# See https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
A = [15, 18, 32, 7, 55, 27, 81, 44, 34, 61, 29, 33, 72, 51, 48]
age_limits = [0, 13, 19, 36, 66, np.inf]
age_counts = np.histogram(A, age_limits)[0]
xs = ['0 - 12', '13 - 18', '19 - 35', '36 - 65', '66+']
plt.bar(xs, age_counts)
plt.show()

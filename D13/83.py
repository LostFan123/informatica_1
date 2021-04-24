# Task:
#   Write the declaration for a vector containing 50 CStudent elements. Then, write the code to add
#   0.5 points on marks of all subjects that are coursed by girls.

# -------------------------------------------------------------------------------------------------
# Possible solution (following the guidelines from the ATENEA document):
# Note: we cannot write `students = [CStudent()] * 50` as this will create a list of the same object 
# repeated 50 times. Instead we can use a loop with append:
students = []
for _ in range(50):
    students.append(CStudent())
# or a list comprehension: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
students = [CStudent() for _ in range(50)]
# ignoring filling the students info since the task says nothing about it...
for student in students:
    if student.sex == 'F':
        student.marks = [mark + 0.5 for mark in student.marks]

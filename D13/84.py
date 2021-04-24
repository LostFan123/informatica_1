# Task:
#   Suppose that a school has a maximum of 100 students and each student has always 10 subjects.
#   Write the declaration for the corresponding class which will be called CSchool. This class will
#   contain the school information, so the structure will have:
#    An integer, the school identifier
#    An integer, the number of students
#    A vector of CStudent type with information regarding to each student
#   Declare an object of CSchool type and write the code to update the Pass field of all students
#   (remember that Pass field must be true if the student passed more than 6 subjects, otherwise must be
#   false.)


# -----------------------------------------------------------------------------------------------------
# Possible solution (following the guidelines from the ATENEA):
class CSchool:
    def __init__(self):
        self.identifier = 0
        self.students_count = 0
        self.students = []

        
school = CSchool()
# ignoring filling a list of students since the task says nothing about it
for student in school.students:
    passed_count = 0
    for mark in student.marks:
        if mark >= 5:
            passed_count += 1
    if passed_count > 6:
        student.pass = True
    
# -----------------------------------------------------------------------------------------------------
# Advanced solution (See advanced solutions for 8.2)
# Using a `dataclass` but not using `property` just for the sake of example:
from dataclasses import dataclass, field
from typing import List

@dataclass
class CSchool:
    identifier: int
    students_count: int = 0
    students: List[CStudent] = field(default_factory=list)

school = CSchool(1, students_count=1234, students=[CStudent(...), ...])  # I'm lazy to fill it =)
for student in school.students:
    if sum(mark >= 5 for mark in student.marks) > 6:
        student.passed = True
        

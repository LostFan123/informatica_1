# Task: 
#   Write the definition of a CStudent class, which must contain the following information:
#    Identifier - an integer used to identify the student
#    Sex - a character (‘M’ form male and ‘F’ for female)
#    Marks - a vector of 10 reals corresponding to marks of 10 subjects
#    Pass - a boolean (true -1- or false -0-) indicating if the student pass or does not pass the
#   course.
#   Write the declaration for an object student of type CStudent. Then write the code to put true in the
#   Pass field value if the student passes more than 6 subjects (to pass a subject you must have a mark
#   higher than or equal to 5), otherwise put false in the Pass field. .


# ------------------------------------------------------------------------------------------------------
# Possible solution (following the guidelines from the document on ATENEA):
class CStudent:
    def __init__(self):
        self.identifier = 0
        self.sex = ''
        self.marks = []
        self.pass = False
        
student = CStudent()
passed_subjects_count = 0
for mark in student.marks:
    if mark >= 5:
        passed_subjects_count += 1
        if passed_subjects_count == 6:
            self.pass = True
            break
# The following is not necessary since `False` is default, but as the task requires us to do it, here it is:
if passed_subjects_count < 6:
    self.pass = False  


# ------------------------------------------------------------------------------------------------------
# Advanced solution.
#   1. It's a questionable design to initialize objects of CStudent type with default values for identifier and sex.
#      What you would normally see is something like this:
from typing import Optional, List  # https://stackoverflow.com/questions/51710037/how-should-i-use-the-optional-type-hint

class CStudent:
    def __init__(self, 
                 identifier: int, 
                 *, # <- this will make all the following arguments keyword-only
                 sex: str,
                 passed: bool = False,
                 marks: Optional[List[int]] = None):  # cannot use empty list as default argument: https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
        self.identifier = identifier
        self.sex = sex
        self.passed = passed
        self.marks = [] if marks is None else marks
    
#     and then intiialize it as:
John = CStudent(4, sex='M')
Jack = CStudent(8, sex='M', passed=True)
Kate = CStudent(15, sex='F', passed=False, marks=[2, 3])

#   2. On Python 3.8 and later we can use `Literal` to type hint the `sex`:
#      https://docs.python.org/3.8/library/typing.html#typing.Literal
from enum import Enum
from typing import Optional, List, Literal


class CStudent:
    def __init__(self, 
                 identifier: int, 
                 *,
                 sex: Literal['M', 'F'],
                 passed: bool = False,
                 marks: Optional[List[int]] = None):  # cannot use empty list as default argument: https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
        self.identifier = identifier
        self.sex = sex
        self.passed = passed
        self.marks = [] if marks is None else marks
        
John = CStudent(4, sex='M')
Kate = CStudent(15, sex='F', passed=False, marks=[2, 3])


#   3. Since our class has only one method (`__init__`), then it probably shouldn't be a class:
#      https://www.youtube.com/watch?v=o9pEzgHorH0
#      We could use `dataclass` here instead: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field
from typing import List, Literal

@dataclass
class CStudent:
    identifier: int
    sex: Literal['M', 'F']
    passed: bool = False
    marks: List[int] = field(default_factory=list)  # https://docs.python.org/3/library/dataclasses.html#default-factory-functions
        
Jack = CStudent(4, 'M', passed=True)
Jack.marks.append(5)
print(Jack.marks)

#   4. Using `sum` to calculate how many times the passing mark is encountered in the list:
passed_subjects_count = sum(mark >= 5 for mark in student.marks)

#   5. This logic could've been put inside the class itself:
from dataclasses import dataclass, field
from typing import List, Literal

@dataclass
class CStudent:
    identifier: int
    sex: Literal['M', 'F']
    marks: List[int] = field(default_factory=list)
    
    @property  # to be able to call it as `student.passed` instead of `student.passed()`
    def passed(self) -> bool:
        return sum(mark >= 5 for mark in self.marks) >= 6
    
student = CStudent(1, 'M', marks=[6,6,6,6,6,6])
print(student.passed)

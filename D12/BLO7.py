# Task: 
#   Write the function to keep track of the training activity of a person. The gym will suggest
#   persons to check their health status after each 100 training sessions in which they spent more than
#   200Kcal.
#   The function receives as parameters a vector of numbers HC and one number kc: HC has the
#   history of the kilo calories burnt by the person, while kc has the kilo calories burnt in his/her last
#   training exercise.
#   Only those sessions that burnt more than 200 Kcal are considered as full sessions to account for
#   health check. Also it is count as one session when two consecutive sessions with less than 200
#   Kcal burnt together more than 300 Kcal.
#   The function will return a Boolean set to True in case a health check is suggested. Otherwise the
#   Boolean will be set at False.
#   HEADER: def health_check (HC, kc)


# -------------------------------------------------------------------------------------------------------
# Possible solution (if I understand the task correctly...):
def health_check(history, last):
    # the number of sessions when more than 200Kcal were burnt
    overburns_count = last > 200
    history.append(last)
    for index, kcal in enumerate(history[:-1]):
        if kcal > 200 or history[index + 1] < 200 and kcal + history[index + 1] > 300:
            overburns_count += 1
        if overburns_count == 100:
            return True
    return False


# -------------------------------------------------------------------------------------------------------
# Advanced solution.
#   Using `zip` to iterate over pairs of items: https://docs.python.org/3/library/functions.html#zip
#   + type hints.
from typing import List 

def health_check(history: List[int], last: int) -> bool:
    overburns_count = last > 200
    history.append(last)
    for kcal, next_kcal in zip(history, history[1:]):
        if kcal > 200 or next_kcal < 200 and kcal + next_kcal > 300:
            overburns_count += 1
        if overburns_count == 100:
            return True
    return False

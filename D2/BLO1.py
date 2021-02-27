# one should avoid duplicating logic:
...
if sex == 'M':
    recommented_weight = 20 + 2 * training_months
else:
    recommented_weight = 20 + 1 * training_months
# one of the solutions I received went through all possible combinations of age/sex
# and for each combination also checked if the weight is greater than the max.

# Possible solution:
MIN_WEIGHT = 20
AGE_LIMIT = 65
MAX_WEIGHT_FOR_OLD = 60
MAX_WEIGHT_FOR_YOUNG = 80
WEIGHT_DELTA_M = 2
WEIGHT_DELTA_F = 1
age = int(input("Age: "))
sex = input("Sex (M/F): ")
training_months = int(input("Months of training: "))
if age > AGE_LIMIT:
    max_weight = MAX_WEIGHT_FOR_OLD
else:
    max_weight = MAX_WEIGHT_FOR_YOUNG
if sex == 'M':
    weight_delta = WEIGHT_DELTA_M
else:
    weight_delta = WEIGHT_DELTA_F
recommended_weight = MIN_WEIGHT + weight_delta * training_months
if recommended_weight > max_weight:
    recommended_weight = max_weight
print(f"Recommended weight is {recommended_weight}")    

# this can be shortened by using a so-called conditional expression:
max_weight = MAX_WEIGHT_FOR_OLD if age > AGE_LIMIT else MAX_WEIGHT_FOR_YOUNG
weight_delta = WEIGHT_DELTA_M if sex == 'M' else WEIGHT_DELTA_F
# ... and using `min` built-in function:
age = int(input("Age: "))
sex = input("Sex (M/F): ")
training_months = int(input("Months of training: "))
max_weight = 60 if age > 65 else 80
weight_delta = 2 if sex == 'M' else 1
recommended_weight = min(max_weight, 20 + weight_delta * training_months)
print(f"Recommended weight is {recommended_weight}")    

# Task:
# Write the code that asks the user age, sex and months of training and calculates the personal recommended weight of a gym exercise, such that: the minimum weight is 20 Kg, the maximum is 60 kg for older than 65 years or 80 kg otherwise, and the formula adds to the minimum: 2
# kg for each month of training in case of men, and 1 kg per month for women.
# EXAMPLE: For a 50 years old man with 16 months of training => the recommended weight is 52 kg

# ------------------------------------------------------------------------------------------------
# Possible solution:
age = int(input("Age: "))
sex = input("Sex (M/F): ")
training_months = int(input("Months of training: "))
max_weight = 60 if age > 65 else 80
weight_delta = 2 if sex == 'M' else 1
recommended_weight = MIN_WEIGHT + weight_delta * training_months
if recommended_weight > max_weight:
    recommended_weight = max_weight
print(f"Recommended weight is {recommended_weight}")   

# or using a built-in `min` function:
age = int(input("Age: "))
sex = input("Sex (M/F): ")
training_months = int(input("Months of training: "))
max_weight = 60 if age > 65 else 80
weight_delta = 2 if sex == 'M' else 1
recommended_weight = min(max_weight, 20 + weight_delta * training_months)
print(f"Recommended weight is {recommended_weight}")    

# 300207 - INFORMÀTICA 1 (Grup: 2A11)
This repository contains the tasks from the deliverables discussed in the class, as well as their possible solutions.
Common mistakes are also discussed.

## Do’s and Don’ts
🟢 Use meaningful names of the variables. It's much easier to read a code like this:
```python
total_minutes = int(input("Number of minutes: "))
minutes_per_day = 60 * 24
minutes_per_hour = 60
days = int(total_minutes / minutes_per_day)
minutes_remainder = total_minutes % minutes_per_day
hours = int(minutes_remainder / minutes_per_hour)
minutes = minutes_remainder % minutes_per_hour
print(str(days) + " days " + str(hours) + " hours and " + str(minutes) + " minutes.")
```
then when the variables have cryptic names:
```python
r = int(input("Number of minutes: "))
l = 60 * 24
p = 60
di = int(r / l)
rd = r % l
h = int(rd / p)
rh = rd % p
m = rh
print(str(di) + " days " + str(h) + " hours and " + str(m) + " minutes.")
```
🔴 Don't use (at least until the first exam) functionality of the language that treats lists as arrays with the dynamically changed size.  
Yeah.. I know. That seems unfair. But the motivation of the creators of the course is to teach you first about fixed-size arrays.
What you cannot use: `list.append`, `list.extend`, `list.pop`, `list.remove`.  
Most probably you won't be allowed to concatenate strings inside a loop as well. So, the following won't be allowed:
```python
text = ''
for index in range(5):
    text += '*'
print(text)
# *****
```
🔴 Don't use `eval`. We already have functions like `int` and `float` that perfectly do the job of conevrting user input to either integers or floats.
While `eval` is also capable of that, it actually is not the right tool since its purpose is, in fact, to evaluate valid Python expressions.
```python
print(eval("N: "))  # N: 1 + 2
# 3
```
Using `eval` can be also dangerous. It's possible that someone will pass a system call in it that can delete all your files, for example. 

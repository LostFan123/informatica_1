# 300207 - INFORMÀTICA 1 (Grup: 2A11)
This repository contains the tasks from the deliverables discussed in the class. 
Possible solutions are shown as well as common mistakes and advanced approaches.
The advanced solutions are not necessary to understand but are included for those 
who are interested if there are "better ways" to solve the problems.  
These solutions also, most probably, won't be accepted on the exams.

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
🟢 Test your code using simple input data. 
For example, for the task where we need to find out if a year is a leap year or not, I received the following solution:
```python
year = int(input("Year: "))
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")
```
By checking it on examples like: 1, 4, 100, 400 we can easily see that the code doesn't produce the expected result.  
🟢 If you don't understand what some code does, you can either 1) add `print`s on every line and print what the variables contain. This can give a rough idea of what is going on in the code. 2) If you are using an IDE (like PyCharm, Spyder, etc.) you can use a [debugger](https://www.jetbrains.com/help/pycharm/part-1-debugging-python-code.html#start-debugger-session) instead. This is a cleaner way. 3) Paste the code into [Python Tutor](http://pythontutor.com/visualize.html).  
🔴 Don't use (at least until the first exam) functionality of the language that treats lists as arrays with the dynamically changed size.  
Yeah.. I know. That seems unfair. But the motivation of the creators of the course is to teach you first about fixed-size arrays.
So, for example, you cannot use: `list.append`, `list.extend`, `list.pop`, `list.remove`. And, most probably, you won't be allowed to concatenate strings inside a loop as well. So, the following won't be allowed:
```python
text = ''
for index in range(5):
    text += '*'
print(text)
# *****
```  
🔴 Don't use `eval`. We already have functions like `int` and `float` that perfectly do the job of conevrting user input to either integers or floats.
While `eval` is also capable of that, it's actually not the right tool since its purpose, in fact, is to evaluate valid Python expressions.
```python
print(eval("N: "))  # N: 1 + 2
# 3
```
Using `eval` can be also dangerous. It's possible that someone will pass a system call in it that can delete all your files!   
🔴 [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) (Don't repeat yourself). If you see that you have some repeating logic in the code, then, most proably, there is a better way to write it.

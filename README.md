# Task 19th May 2021
## Program to calculate year of birth!
### Timings
30-60 Minutes

### Summary
Cool, we've used strings to make a program that made a welcome message. Now let's use some numerical types.

Create program that calculates the year of birth.

### Tasks
- define the variables age and name
- make a calculation for the year in which the person was born
- print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values

### Second Part
- prompt the user for input and re-assign the variable age and name
- figure out a way to account for if the persons birthday has already happened this year or not
### Extra
- go look into the library time
- print out the amount of hour this person has lived

### Acceptance Criteria
- program defines the variable age and name
- program prints the string "OMG <person>, you are <age> years old so you were born in <year>"

## My Solution
```python
# Promts User to enter their name and welcomes user
Name = str(input("Please enter your name: "))
print("Hello " + Name)

# Promts User to enter their age
Age = int(input("Please enter your age: "))

# Promts user to enter their month of birth
Month_of_birth = int(input("Please enter the month you were born in numerical format e.g '1': "))

# Calculatiom forth their date of birth based on the month they were born
Birthday_passed_this_year = 2021 - Age
Birthday_not_passed_this_year = 2021 - Age + 1

# An if, else statement which allows the correct calculation to be made based on their month of birth
if (Month_of_birth <= 6):
    print("OMG " + Name + ", " + "you are " + str(Age) + " years old " + "so you were born in " + str(Birthday_passed_this_year))
else:
    print("OMG " + Name + ", " + "you are " + str(Age) + " years old " + "so you were born in " + str(Birthday_not_passed_this_year))
```
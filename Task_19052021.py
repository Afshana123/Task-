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
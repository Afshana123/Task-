Name = str(input("Please enter your name: "))
print("Hello " + Name)

Age = int(input("Please enter your age: "))

Month_of_birth = int(input("Please enter the month you were born in numerical format e.g '1': "))

Birthday_passed_this_year = 2021 - Age
Birthday_not_passed_this_year = 2021 - Age + 1

if (Month_of_birth <= 6):
    print("OMG " + Name + ", " + "you are " + str(Age) + " years old " + "so you were born in " + str(Birthday_passed_this_year))
else:
    print("OMG " + Name + ", " + "you are " + str(Age) + " years old " + "so you were born in " + str(Birthday_not_passed_this_year))
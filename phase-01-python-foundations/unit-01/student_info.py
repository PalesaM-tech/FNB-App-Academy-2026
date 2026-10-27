# collect personal information
first_name = input("Enter your First name: ")
surname = input("Enter your Surname: ")
age = int(input("Enter your Age: "))
age_in_months= age * 12
favourite_number = float(input("Enter your favourite number: "))

print(f"Welcome, {first_name.upper()} {surname.upper()}!")
print(f"Welcome, {first_name.title()} {surname.title()}")
print(f"Your age in months:, {age_in_months} ")
print(f"You favourite number is:, {round(favourite_number, 2)}")

#Data types
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourite_number))

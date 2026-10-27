#YouTube------ BroCode-Functions--------------------

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +" " +last

full_name = create_name("teboho", "mokoena")

print(full_name)

def add(x, y):
    z = x + y
    return z

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of R{amount} is due: {due_date}.")

def happy_birthday(name, age):
    print(f"Happy birthday to you! {name}")
    print(f"You are {age} old!")
    print(f"Happy birthday to you! {name}")

display_invoice("Simphiwe", 900, "01/09/2026")

happy_birthday("Palesa", 20)

#return = statement used to end a function and send a result back to the caller
# -----------YouTube. Conditionals and Booleans------------

#False values:
     # False
     # None
     # Zero of any numeric type
     # Any empty sequence. For example, "", (), [].
     # Any empty mapping. For example, {}

condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")


#---testing out the "is" keyword---

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  #this is considered True because the values are the same but,
print(id(a))
print(id(b))
print(a is b)  #here they are False because they are stored differently/ different memory or have different ID

# ---booleans operations---
# and
# or
# not
#--- using the "and" operations
user = "admin"
logged_in = True

if user == "admin" and logged_in:
    print("Admin Page")
else:
    print("Bad credentials")

#--- using the "or" operations
user = "admin"
logged_in = False

if user == "admin" or logged_in:
    print("Admin Page")
else:
    print("Bad credentials")

#--- using the "not" operations---
user = "admin"
logged_in = False

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

#---break---
language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No match")

#-----------FNB APP ACADEMY-----------------
#A guessing game

secret_word = "python"

while True:
    guess = input("Enter the programming language we are using: ").lower()

    if guess == secret_word:
        print("You guessed the correct language !!!")
        break  #used to escape a loop
    else:
        print("Incorrect guess, try again !!!")
        break



#Building a simple rep counter

for rep in range(1, 4):   #the "rep" is a temporary variable
    print(f"This is rep no. {rep}")

# countdown using WHILE loop
count = 4

while count >0 :
    print(count)
    count = count - 1

print("Blast off !!!")


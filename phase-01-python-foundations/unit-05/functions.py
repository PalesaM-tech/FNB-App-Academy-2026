#----Chatgpt explaination-------
def greeting():
    print("Hello")
    print("Enjoy your stay!")
    print("Have a nice day!")

greeting()

# ---Parameters---
def greetingz(name):
    print(f"Hello {name}")

greetingz("Palesa")

# ---Return---
def add(a, b):
    return a + b

answer = add(5, 3)

print(answer)

# YouTube explaination
def hello_func():
    print("Hello Function.")
# DRY  "Keeping your code dry" - dont repeat yourself when you can put it in a variable/ function.
hello_func()
hello_func()

def hello_func():
    return("Hello Function.")

print(hello_func().upper())


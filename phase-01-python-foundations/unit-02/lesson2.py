#Corey Schafer:strings video
greeting = "Hello"
name = "Palesa"

#print(help(str))
#print(dir(name))

#text = greeting + ", " + name + ". Welcome! " #concatenating
#the way of writting below is for python versions that is not version 3.6 and higher
text = "{}, {}. Welcome!".format(greeting, name) #{} is for place holder
#the writting below contains f-string and is for newer versions
text = f"{greeting}, {name}. Welcome!"
print(text)

message = "Hello World"
message = message.replace("World", "Universe")
print(message)

print(message.upper())
print(message.lower())
print(message.count("o"))
print(message.find("World"))


#FNB APP ACADEMY LESSON BELOW
#Create a professional email generating system

first_name = input("Enter your First Name: ").strip()
surname = input("Enter your Last Name: ").strip()

username = f"{first_name[0]}{surname}"
print(f"Your email is: {username.lower()}@university.co.za")

#Using string methods 
town = "  Bloemfontein  "

print(town.upper())
print(town.strip())

#Tracking individual letters
name = "Python"

print(name[0])
print(name[-1])
print(name[2])
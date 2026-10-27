#the range funtion - used to generate a sequence of numbers
numbers2 =range(5, 10) #an object that can store a sequence of numbers

for number in numbers2:
    print(numbers2)

#for loops
numbers1 = [1, 2, 3, 4, 5]
for item in numbers1:
    print(item)

i = 0
while i < len(numbers1):
    print(numbers1[i])
    i = i +1

#list methods
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
numbers.insert(0, -2)
numbers.remove(3)
print(numbers)
print(6 in numbers)
print(len(numbers))

#lists
names = ["Palesa", "Naledi", "Muchis", "Ipeleng", "Mahau"]
names[2] = "Mutshidzi"
names[4] = "Mohau"
print(names[0:3]) 
print(names)
print(len(names))

#while loops
i = 1
while i<=10:
    print(i * "the") #placing an asterisks, means multipying/repeating the "string" according to the i value
    i += 1


weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kg's: " + str(converted))


temperature = -2

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #if temp is greater than 20 and less than 30, its a nice day
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold today")
print("Done!")

price = 25
print(price > 10 and price < 30)

x = 3 > 2
print(x)

name = input("Enter your name: ")
print(f"Greetings, {name}")

names = input()
print(f"Hello, {name}")


name = input("Enter your name: ")
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)
print(age)

first_number = input("First Digit: ")
second_number = input("Second Digit: ")
sum = float(first_number) + float(second_number)
print("Sum: "+ str(sum))

course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.find("y"))
print(course.find("for"))
print(course.replace('for', "4"))
print('Anna' in course )

x = 10
x = x + 3
x += 3
x *=3
x -= 3
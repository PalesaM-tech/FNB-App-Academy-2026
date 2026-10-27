#-------YOUTUBE---Loops and Iterations----------------
x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x = x + 1

nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in "abc":
        print(num, letter)

#using the break
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

#using the continue function

for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)


#------FNB APP ACADEMY------------
#working with dictionaries

student = {"name": "Palesa",
           "age": 25,
           "course": "Intro to Python"
           }

print(student["name"])
print(student["age"])

# working list (shopping cart)

cart = ["Apples", "Eggs", "Milk"]
print(cart[0])

cart.append("Bread")
print(cart)

for item in cart:
    print(item)

for i in range(5):
    print("hello")

for i in range(1, 20, 2):
    print(i)


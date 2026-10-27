#YouTube vid- Working with data types
num = 3.54

print(type(num))

#Arithmetic operators
#Addition: 3 + 2
#Subtraction: 3 - 2
#Multiplication: 3 * 2
#Division: 3 / 2
#Floor divsion: 3 // 2
#Exponent: 3 ** 2
#Modulus: 3 % 2

#NOTE: PYTHON USE BEDMAS
print(7 % 2)
print(round(3.456, 2))

#Comparison Operators, will return booleans(True/False value)

num1 = 3
num2 = 2

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

numb1 = "100"
numb2 = "200"

numb1 = int(numb1)
numb2 = int(numb2)

print(numb1 + numb2)

#FNB APP ACADEMY WORK!!!
#calculating a tip at the resturant

bill = float(input("Enter the bill: R"))
tip = 0.15 #written in decimal

tip_value = bill * tip
total_amount = bill + tip_value

print(f"Here is the tip: {tip_value}")
print(f"Here is the tip: {round(tip_value, 2)} rounded")

print(f"Here is the total amount: {total_amount}")
print(f"Here is the total amount: {round(total_amount, 2)} rounded")

#ADDING two numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the first number: "))

print("Answer: ", (number1 + number2))

#Type Casting
#converting original functions to something else
#for example int(str)
#The fix is type casting,  wrapping input() with int() or float(). 
# Use int() for whole numbers and float() when decimals are possible.
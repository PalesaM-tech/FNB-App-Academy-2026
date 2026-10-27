#Collect 2 numbers from the user
value_1 = float(input("Enter your first value: "))
value_2 = float(input("Enter your second value: "))

#Calculate and display
answer_add = round(value_1 + value_2, 2)
print(f"This is the addition answer: {answer_add}") 

answer_minus = round(value_1 - value_2, 2)
print(f"This is the subtraction answer: {answer_minus}")
 
answer_multiplication = round(value_1 * value_2, 2)
print(f"This is the the multiplication answer: {answer_multiplication}")
#Below is for division, floor division, modulus
#moved everything into the else block
if value_2 == 0:
    print("Invalid input. You can't divide by zero.")
else:
    answer_division = round(value_1 / value_2, 2)
    print(f"This is the divison answer: {answer_division}")
    
    answer_floor_div = round(value_1 // value_2, 2)
    print(f"This is the floor division answer: {answer_floor_div}")
    
    answer_modulus = round(value_1 % value_2, 2)
    print(f"This is the remainder: {answer_modulus}") 
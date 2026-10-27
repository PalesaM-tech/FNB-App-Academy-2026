#fuel cost calculator
print(7 + 3 * 2)
print(2 ** 8)
#kilometers user wants to drive
kilometers = float(input("Enter kilometers you want to drive: "))

#current petrol price per litre
price_per_liter = float(input("Enter the petrol price per liter: "))
liters_needed = kilometers / 10

#calculate total costs
total_cost = round(liters_needed * price_per_liter, 2)

print(f"Kilometers: {kilometers}km")
print(f"Petrol price: R{price_per_liter}")
print(f"Fuel needed: {liters_needed}litres")
print(f"This is the total cost: R{total_cost}")
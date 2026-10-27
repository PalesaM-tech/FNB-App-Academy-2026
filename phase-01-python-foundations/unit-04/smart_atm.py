balance = float("5000")
#how much the user wants to with draw
withdraw = float(input("Enter amount you want to withdraw: "))

new_balance = balance - withdraw


if withdraw <= 0:
    print("Invalid amount. You must withdraw more than 'R0'")
elif withdraw <= balance:
    new_balance = balance - withdraw
    print(f"Withdrawal successful! Remaining balance: R{new_balance}")
else:
    print("Declined. Insufficient funds")
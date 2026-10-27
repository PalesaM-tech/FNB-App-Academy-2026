password = input("Enter your password: ")
final_password = password.strip()

print(f"Your password hint: It starts with {final_password[0].upper()} and ends with {final_password[-1].upper()}")
print(f"Your password hint: It starts with {final_password[0:3].upper()} and ends with {final_password[-3:].upper()}")

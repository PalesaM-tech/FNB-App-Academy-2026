#collect personal information and bio message
first_name = input("Enter you first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a bio message: ").strip()
bio_count = len(bio)
new_bio = bio.replace("I am", "I'm")

print(f"Your Name: {first_name}")
print(f"Your Last name: {last_name}")

#creating a username
username = f"{first_name[0]}{last_name}"
print(f"You username is: {username.lower()}")

#fullname in title case
full_name = first_name + " " + last_name
print(f"Welcome, {full_name}")
print(f"This is your Fullname: {full_name.title()}")

#The bio
print(f"This is the bio: {bio}")
#strip the bio
print(f"This is your Biography count: {bio_count}")

#replacement in the bio
print(f"This is the new bio: {new_bio}")
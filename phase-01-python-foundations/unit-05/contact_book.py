#dictionary to store contacts

contacts = []

print(contacts)
#implement an add_contact function that appends a new dictionary to the list
def add_contact():
    name = input("Enter contact's name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
        }
    contacts.append(contact)
    print("Contact successfully added!")

add_contact()
    
#implement a search_contact(name) function that searches by name and returns 

def search_contact(contact):
    for contact in contacts:
        if contacts["name"] == contact:
            return contact

        return None

contact_found = search_contact(input("Enter name you are searching for: "))
if contact_found:
    print(f"Contact has been provided: {contact_found}")
else:
    print("Contact not found")

search_contact(contact_found)

def delete_contact():
    pass

def view_all():
    pass

search_person = input("Enter contact name: ").find(contacts)
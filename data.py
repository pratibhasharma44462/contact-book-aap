contacts_get = {}

while True:
    print("\n Contact book aap")
    print("1) Create contact")
    print("2) View contact")
    print("3) Update contact")
    print("4) Search contact")
    print("5) Delete contact")
    print("6) Count contact")
    print("7) Exit contact")

    choose = int(input("enter your prefrence: "))
    if choose == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts_get[name] = phone
        print(f"Contact {name} added with phone number {phone}.")

    elif choose == 2:
        if contacts_get:
            for name, phone in contacts_get.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts available.")

    elif choose == 3:
        name = input("Enter the name of the contact to update: ")
        if name in contacts_get:
            new_phone = input("Enter new phone number: ")
            contacts_get[name] = new_phone
            print(f"Contact {name} updated with new phone number {new_phone}.")
        else:
            print(f"Contact {name} not found.")

    elif choose == 4:
        name = input("Enter the name of the contact to search: ")
        if name in contacts_get:
            print(f"Contact found: Name: {name}, Phone: {contacts_get[name]}")
        else:
            print(f"Contact {name} not found.")

    elif choose == 5:
        name = input("Enter the name of the contact to delete: ")
        if name in contacts_get:
            del contacts_get[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    elif choose == 6:
        print(f"Total contacts: {len(contacts_get)}")

    elif choose == 7:
        print("Exiting contact book app.")
        break

    else:
        print("Invalid choice, please try again.")
    input("Press Enter to continue...")
    print("\n")  # For better readability in the loop




# This code shows a simple contact book application that allows users to create, view, update, search, delete, and count contacts.
# It uses a dictionary to store contacts, where the key is the contact's name and the value is the phone number.
# The application runs in a loop until the user chooses to exit. Each operation is handled with appropriate messages.
# The code is designed to be user-friendly and provides feedback for each action taken.
# The contact book app is a simple command-line application that allows users to manage their contacts.
# It provides options to create, view, update, search, delete, and count contacts.
# The contacts are stored in a dictionary where the key is the contact's name and the value is the phone number.
# The app runs in a loop, allowing users to perform multiple operations until they choose to exit.
# Each operation is accompanied by appropriate messages to guide the user through the process.
# The app is designed to be user-friendly and provides feedback for each action taken.

         

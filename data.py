contacts_get = {}

while True:
    print("\n Contact book aap")
    print("1 Create contact")
    print("2 View contact")
    print("3 Update contact")
    print("4 Search contact")
    print("5 Delete contact")
    print("6 Count contact")
    print("7 Exit contact")

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





         

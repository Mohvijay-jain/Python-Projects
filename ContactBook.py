def contact_book():
    contacts = {}  

    while True:
        print("\nContact Book")
        print("1. Add Contact to phone log")
        print("2. View Contacts from phone log")
        print("3. Edit Contact")
        print("4. Delete Contact from phone log")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            country_code = input("Enter your country code: ")
            number = input(f"Enter your number: ")
            full_number = country_code +" " +number
            email_id = input("Enter your Email Id:")
            contacts[name] = full_number
            print(f"Contact '{name}' added.")

        elif choice == '2':
            if contacts:
                print("Contacts:")
                for name, phone in contacts.items():
                    print(f"{name} : {phone} : {email_id}")
                    
            else:
                print("No contacts found.")

        elif choice == '3':
            name = input("Enter contact name to edit: ")
            if name in contacts:
                new_country_code = input("Enter new country code: ")
                new_number = input("Enter new number: ")
                new_email_id = input("Enter new Email-Id:")
                contacts[name] = new_country_code + new_number
                print(f"Contact '{name}' updated.")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter contact name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' deleted.")
            else:
                print("Contact not found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

contact_book()
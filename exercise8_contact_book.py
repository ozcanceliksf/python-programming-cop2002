# Exercise 8 - Contact Book
# COP2002 - Python Programming
# Ozcan Celik

def add_contact(contacts, name, phone, email):
    """Add a new contact to the dictionary."""
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")

def search_contact(contacts, name):
    """Search for a contact by name."""
    if name in contacts:
        info = contacts[name]
        print(f"\nName  : {name}")
        print(f"Phone : {info['phone']}")
        print(f"Email : {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    """Delete a contact from the dictionary."""
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def list_contacts(contacts):
    """List all saved contacts."""
    if not contacts:
        print("No contacts saved.")
        return
    print("\n--- Contact List ---")
    for i, (name, info) in enumerate(contacts.items(), 1):
        print(f"{i}. {name} | {info['phone']} | {info['email']}")
    print("--------------------")

def main():
    contacts = {}

    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. List all contacts")
        print("5. Exit")

        choice = input("\nChoose (1-5): ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            name = input("Search name: ").strip()
            search_contact(contacts, name)
        elif choice == "3":
            name = input("Delete name: ").strip()
            delete_contact(contacts, name)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

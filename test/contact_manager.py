# contact_manager.py

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def save_contacts():
    with open("contacts.txt", "w") as f:
        for c in contacts:
            f.write(f"{c['name']},{c['phone']},{c['email']}\n")
    print("Contacts saved.\n")

def load_contacts():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append({"name": name, "phone": phone, "email": email})
        print("Contacts loaded.\n")
    except FileNotFoundError:
        print("No saved contacts found.\n")

def main():
    load_contacts()
    while True:
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            save_contacts()
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()

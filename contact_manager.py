import re
import os

# Initialize contact data storage
contacts = {}

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    print("\n--- Add a New Contact ---")
    id = input("Enter a unique identifier (e.g., phone number or email address): ")
    
    if id in contacts:
        print("A contact with this identifier already exists.")
        return
    
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address (optional): ")
    notes = input("Enter any additional notes (optional): ")

    contacts[id] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address,
        'Notes': notes
    }

    print("Contact added successfully.")

def edit_contact():
    print("\n--- Edit an Existing Contact ---")
    id = input("Enter the unique identifier of the contact to edit: ")
    
    if id not in contacts:
        print("Contact not found.")
        return
    
    print("Leave a field blank to keep its current value.")
    name = input(f"Enter the contact's name ({contacts[id]['Name']}): ") or contacts[id]['Name']
    phone = input(f"Enter the contact's phone number ({contacts[id]['Phone']}): ") or contacts[id]['Phone']
    email = input(f"Enter the contact's email address ({contacts[id]['Email']}): ") or contacts[id]['Email']
    address = input(f"Enter the contact's address ({contacts[id]['Address']}): ") or contacts[id]['Address']
    notes = input(f"Enter any additional notes ({contacts[id]['Notes']}): ") or contacts[id]['Notes']

    contacts[id] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address,
        'Notes': notes
    }

    print("Contact updated successfully.")

def delete_contact():
    print("\n--- Delete a Contact ---")
    id = input("Enter the unique identifier of the contact to delete: ")
    
    if id not in contacts:
        print("Contact not found.")
        return
    
    del contacts[id]
    print("Contact deleted successfully.")

def search_contact():
    print("\n--- Search for a Contact ---")
    id = input("Enter the unique identifier of the contact to search: ")
    
    if id not in contacts:
        print("Contact not found.")
        return
    
    contact = contacts[id]
    print(f"Name: {contact['Name']}")
    print(f"Phone: {contact['Phone']}")
    print(f"Email: {contact['Email']}")
    print(f"Address: {contact['Address']}")
    print(f"Notes: {contact['Notes']}")

def display_all_contacts():
    print("\n--- Display All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return
    
    for id, contact in contacts.items():
        print(f"\nIdentifier: {id}")
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Address: {contact['Address']}")
        print(f"Notes: {contact['Notes']}")

def export_contacts():
    print("\n--- Export Contacts to a Text File ---")
    filename = input("Enter the filename to save the contacts: ")
    
    try:
        with open(filename, 'w') as file:
            for id, contact in contacts.items():
                file.write(f"Identifier: {id}\n")
                file.write(f"Name: {contact['Name']}\n")
                file.write(f"Phone: {contact['Phone']}\n")
                file.write(f"Email: {contact['Email']}\n")
                file.write(f"Address: {contact['Address']}\n")
                file.write(f"Notes: {contact['Notes']}\n")
                file.write("\n---\n\n")
        print("Contacts exported successfully.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def import_contacts():
    print("\n--- Import Contacts from a Text File ---")
    filename = input("Enter the filename to load contacts from: ")
    
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    
    try:
        with open(filename, 'r') as file:
            content = file.read().split('\n---\n\n')
            for entry in content:
                lines = entry.split('\n')
                if len(lines) < 6:
                    continue
                id = lines[0].split(': ')[1]
                contacts[id] = {
                    'Name': lines[1].split(': ')[1],
                    'Phone': lines[2].split(': ')[1],
                    'Email': lines[3].split(': ')[1],
                    'Address': lines[4].split(': ')[1],
                    'Notes': lines[5].split(': ')[1]
                }
        print("Contacts imported successfully.")
    except Exception as e:
        print(f"An error occurred while importing contacts: {e}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-8): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()

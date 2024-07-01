welcome = input("Welcome user!!! To your Contact Management Sytem: menu/Shutdown?")

menu = input('Menu\nAdd new Contact\nEdit existing Contact\nDelete Contact\nSearch for a Contact\nDisplay all Contacts\nExport contacts to a text file\nImport contact from a text file\nExit')


contacts = {}

response = input()

#     if 
    
def add_new_contact(contacts):
    contacts_name = input('enter name:')
    contacts_address = input('enter address:')
    contacts_email = input('enter email:')
    contacts_phonenum = input('enter phone num:')
    contacts[contacts_email] = {'name':contacts_name,
                                'address': contacts_address,
                                'email': contacts_email,
                                'phone': contacts_phonenum
                                    }
    print('you have added',(contacts))
add_new_contact(contacts)


def edit_existing_contact(contacts):
    email = input('pls enter email of contact you want to update:')
    if email in contacts:
        contacts_name = input('enter name:')
        contacts_address = input('enter address:')
        contacts_email = input('enter email:')
        contacts_phonenum = input('enter phone num:')
        contacts.update({contacts_email:{'name':contacts_name,
                                    'address': contacts_address,
                                    'email': contacts_email,
                                    'phone': contacts_phonenum
                                        }}) 
    print((contacts),'has been edited')
    

def delete_contact(contacts):
    phone_num = input('please enter number of contact you wish to delete:')
    if phone_num in contacts:
        contacts_name = input('enter name:')
        contacts_address = input('enter address:')
        contacts_email = input('enter email')
        contacts_phone_num = input('enter phone number:')
        contacts.remove({contacts_phone_num:{'name': contacts_name,
                                             'address': contacts_address,
                                             'email': contacts_email,
                                             'phone': contacts_phone_num
                                             }})
    print('you have deleted',(contacts))

def seach_for_a_contact(contacts):
    contact = input('who are you looking for?')
    if contact in contacts:
        contacts_name = input('enter name')
        contacts_address = input('whats their address')
        contacts_num = input ('whats their number')
        contacts_email = input('what is theie email')
        contacts.display({contacts:{'name': contacts_name,
                                    'address': contacts_address,
                                    'email': contacts_email,
                                    'phone' : contacts_num
                                    }})
        print('here is'(contacts))

def display_all_contacts(contacts):
    for email, contact_info in contacts.items:
        print(email, contact_info)


def export_contacts(contacts):
    pass

def import_contacts(contacts):
    from contact_management_system import contacts
    pass
        
        
def exit(contacts):
    if response == exit:
        print('Goodbye User!!!')

while True:
    menu = input('Menu\nadd new contact\nedit existing contact\ndelete contact\nsearch for a contact\ndisplay all contacts\nexport contacts to a text file\nimport contact from a text file\nexit')
    if input == 'menu':
        print(menu)
    if input == 'add_new_contact':
        print(add_new_contact)
    if input == 'edit existing contact':
        print(edit_existing_contact)
    if input == 'delete contact':
        print(delete_contact)
    if input == 'search for a contact':
        print(seach_for_a_contact)
    if input == 'display all contacts':
        print(display_all_contacts)
    if input == 'export contact':
        print(export_contacts)
    if input == 'import contact':
        print(import_contacts)
    elif input == 'shutdown':
        break
    else:
        print(f'Invalid entry please try again|\n{menu}')
welcome(contacts)
contacts()


address_book = {}

def add_contact():
    name = input('Enter the name: ')
    phone = input('Enter the phone number: ')
    address = input('Enter the address: ')
    address_book[name] = {'phone': phone, 'address': address}
    print(f'Contact {name} has been added!')

def view_contacts():
    if not address_book:
        print('Address book is empty.')
    else:
        for name, details in address_book.items():
            print(f'Name: {name}')
            print(f'Phone: {details["phone"]}')
            print(f'Address: {details["address"]}')

def search_contact():
    name = input('Enter the name search for:')
    if name in address_book:
        details = address_book[name]
        print(f'Name {name}')
        print(f'Phone {details["phone"]}')
        print(f'Address: {details["address"]}')
    else:
        print(f'Contact {name} not found in address book.')

while True:
    print('\nAddress Book Menu:')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Search Contact')
    print('4. Exit')

    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print('Goodbye')
        break
    else:
        print(f'Invalid choice. Please select (1/2/3/4): ')

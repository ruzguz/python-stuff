from cbook import ContactBook, Contact
import csv

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue 
            contact_book.add(row[0], row[1], row[2])


    while True:        

        print('')
        print('1 - Add contact')
        print('2 - Update contact')
        print('3 - Find contact')
        print('4 - Remove contact')
        print('5 - List contacts')
        print('6 - Exit')
        print('')

        command = input('Select an option: ')

        if command == '1':
            name = input('Introduce the name of the contact: ')
            phone = int(input('Introduce the phone number: '))
            email = input('Introduce the email: ')
            
            contact_book.add(name, phone, email)

        elif command == '2':
            name = input('Introduce the name of the contact to update: ')
            new_name = input('Introduce the new name (leave in blank to use the current name): ')
            new_phone = input('Introduce the new phone number (leave in blank to use the current phone number): ')
            new_email = input('Introduce the new email (leave in blank to use the current email): ')

            contact_book.update(name, new_name, new_phone, new_email)
             
        elif command == '3':
            name = input('Introduce the name contact to find: ')
            contact_book.find_contact(name)
        elif command == '4':
            name = input('Introduce the name of the contact: ')
            contact_book.remove(name)
        elif command == '5':
            contact_book.list_contacts()
        else:
            break


if __name__ == '__main__':
    print('WELCOME TO THE APP')
    print('')
    run()

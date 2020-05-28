class Contact:
    
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

    def print_contact(self):
        print('------------------------------------')
        print('Name: {}'.format(self._name))
        print('Phone: {}'.format(self._phone))
        print('Email: {}'.format(self._email))
        print('------------------------------------')

    # Setters and Getters
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def set_phone(self, phone):
        self._phone = phone

    def set_email(self, email):
        self._email = email

class ContactBook:
    
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self._contacts.append(new_contact)

    def list_contacts(self):
        for contact in self._contacts:
            contact.print_contact()

    def find_contact(self, name):
        contacts = [c for c in self._contacts if c.get_name() == name]
        
        if len(contacts) == 0:
            print('Contact not found.')
            return

        for contact in contacts:
            contact.print_contact()

    def remove(self, name):
        self._contacts = [c for c in self._contacts if c.get_name() != name]

    def update(self, name, new_name, new_phone, new_email):
        for contact in self._contacts:
            if contact.get_name() == name:
                if new_name != '':
                    contact.set_name(new_name)
                if new_phone != '':
                    contact.set_phone(new_phone)
                if new_email != '':
                    contact.set_email(new_email)
        

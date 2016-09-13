class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):
    all_orders = {}

    def order(self, string):
        Supplier.all_orders[self.email] = string


class ContactList:

    @staticmethod
    def extendlist(list):
        Contact.all_contacts.extend(list)

    @staticmethod
    def search(string):
        return [item[0] for item in Contact.all_contacts if item[0] == string]

    @staticmethod
    def longest_name():
        return max(Contact.all_contacts[0], key=len)

a = Contact("pisti", "alma")
b = Contact("zsoltiiiii", "narancs")
c = Contact("pisti", "kelep")
d = Contact("lali", "pokakip")

# print(ContactList.search("pisti"))
# print(ContactList.longest_name())
print(Contact.all_contacts)


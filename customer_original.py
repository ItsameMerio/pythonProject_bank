from account import Account


class Customer:

    bank_id = 0
    def __init__(self, name):
        self.name = name

    def get_id(self):
        self.id = Customer.bank_id
        Customer.bank_id += 1
        return self.id

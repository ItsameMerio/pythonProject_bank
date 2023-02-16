from account import Account
class Customer:

    bank_id = 0
    def __init__(self, name):
        self.name = name
        Customer.bank_id += 1
        self._id = Customer.bank_id


    def get_id(self):
        return self._id

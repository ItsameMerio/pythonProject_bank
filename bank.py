import account
from customer import Customer
from account import Account
from personal_account import PersonalAccount
from savings_account import SavingsAccount

class Bank:

    def __init__(self, name_bank):
        self._name = name_bank
        self._customers = []
        self._accounts = []

    def get_name(self):
        return self._name

    def get_customers(self):
        return self._customers

    def get_customers_by_name(self, name):
        matches = []
        for customer in self.get_customers():
            if name == customer.name:
                matches.append(customer)
        return matches

    def get_customer_by_id(self, id):
        for customer in self.get_customers():
            if id == customer.get_id():
                return customer
        return None

    def add_customer(self, customer):
        if not self.get_customer_by_id(customer.get_id()):
            self._customers.append(customer)

    def add_savings_account(self, customer):
        if self.get_customer_by_id(customer.get_id()):
            enew = SavingsAccount(customer)
            self._accounts.append(enew)
            return enew
        return None

    def add_personal_account(self, customer):
        if self.get_customer_by_id(customer.get_id()):
            enew = PersonalAccount(customer)
            self._accounts.append(enew)
            return enew
        return None


    def remove_customer(self, customer):
        if self.get_customer_by_id(customer.get_id()):
            self._customers.remove(customer)


    def get_accounts(self, customer):
        matches = []
        if not self.get_customer_by_id(customer.get_id()):
            return matches
        for account in self._accounts:
            ids = account.get_customer().get_id()
            if ids == customer.get_id():
                matches.append(account)
        return matches

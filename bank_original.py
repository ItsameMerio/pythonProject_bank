from customer_original import Customer
from account import Account


class Bank:

    def __init__(self, name_bank):
        self.name = name_bank
        self.customers = []
        self.accounts = []

    def get_name(self, name):
        return self.name

    def get_customers(self):
        return self.customers

    def get_customers_by_name(self, customer):
        matches = []
        customers_name = self.get_customers()
        for i in range(len(customers_name)):
            if customer == customers_name[i][1]:
                matches.append(customers_name[i][1])
            return matches

    def get_customer_by_id(self, customer):
        matches = []
        customers_id = self.get_customers()
        for i in range(len(customers_id)):
            if customer == customers_id[i][2]:
                matches.append(customers_id[i][2])
                return matches
            else:
                return None

    def add_customer(self, customer):
        customers = self.get_customers()
        for i in range(len(customers)):
            if customer == customers[i]:
                continue
            else:
                customers.append(Customer(customer))

    def add_account(self, customer):
        customers = self.get_customers()
        for i in customers:
            if customer == customers[i]:
                accounts.append(Account(customer))

    def remove_customer(self, customer):
        try:
            self.customers.remove(customer)
        except ValueError:
            pass

    def get_accounts(self, customer):
        matches = []
        acc = accounts.copy()
        for i in range(len(acc)):
            if customer == acc[i][0]:
                matches.append(acc[i][0])
            return matches

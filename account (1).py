class Account:

    def __init__(self, customer):
        self._owner = customer
        self._balance = 0

    def get_customer(self):
        return self._owner

    def get_balance(self):
        return self._balance

    def deposit(self, summa):
        self._balance += summa

    def withdraw(self, summa):

        if summa > self.get_balance():
            return False
        self._balance -= summa
        return True

    def transfer_to(self, account, summa):
        if self._balance == 0:
            return False
        if self.withdraw(summa):
            account.deposit(summa)
            return True
        return False

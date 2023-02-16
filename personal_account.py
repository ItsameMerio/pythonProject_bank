from account import Account


class PersonalAccount(Account):

    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, summa):
        if self._balance == 0:
            return False
        if self.withdraw(summa):
            account.deposit(summa)
            return True
        return False

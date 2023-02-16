from account import Account


class SavingsAccount(Account):
    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, summa):
        if self._balance == 0:
            return False
        customer1 = self.get_customer()
        customer2 = account.get_customer()
        if customer1 == customer2:
            if self.withdraw(summa):
                account.deposit(summa)
                return True
        return False

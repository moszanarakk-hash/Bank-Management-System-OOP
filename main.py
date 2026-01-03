class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount
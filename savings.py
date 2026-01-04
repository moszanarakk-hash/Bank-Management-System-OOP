class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self._update_balance(interest)

        logging.info(
            f"{self.account_holder} รับดอกเบี้ย {interest} | อัตรา {self.interest_rate}")

        return interest
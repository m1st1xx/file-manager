class BankAccount:
    def __init__(self,balance,owner):
        self._balance=balance
        self._account_id="12345"
        self.owner=owner
    def get_balance(self):
        return f"your balance: {self._balance}"
    def deposit(self,sum):
        self._balance+=sum
        return f"balance deposited for {sum} "
class CreditAccount(BankAccount):
    def __init__(self,balance,owner,credit):
        super().__init__(balance,owner)
        self.__credit=credit
    def info_credit(self):
        return f"your credit: {self.__credit}"
    def pay_for_credit(self,pay):
            self._balance-=pay
            self.__credit -= pay
            return f"congratulations credit deposited for {pay}"


account=BankAccount(10000,"vanya")
creaccount=CreditAccount(10000,"oleg",30000)
print(account.get_balance())
print(account.deposit(1000))
print(account.get_balance())
print(creaccount.get_balance())
print(creaccount.deposit(10000))
print(creaccount.info_credit())
print(creaccount.pay_for_credit(7000))
print(creaccount.get_balance())
print(creaccount.info_credit())
print(account._balance)
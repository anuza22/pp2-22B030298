class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add):
        self.balance+=add

    def withdraw(self, k2):
        if k2<=self.balance:
            self.balance-=k2

    def mybalance(self):
        print(self.balance)


bank = Account("Anuza", 0)
bank.deposit(5000)
bank.mybalance()
bank.withdraw(500)
bank.mybalance()



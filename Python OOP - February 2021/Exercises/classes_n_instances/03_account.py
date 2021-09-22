class Account:

    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance if balance > 0 else balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())


account2 = Account(1234, "George", 1000)
print(account2.credit(500))
print(account2.debit(1500))
print(account2.info())

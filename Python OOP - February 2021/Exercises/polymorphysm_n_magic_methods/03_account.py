class Account:

    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    @staticmethod
    def int_serializer(value_type):
        if isinstance(value_type, int):
            return True
        return False

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.amount - amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.amount -= amount_to_add
        account._transactions.append(amount_to_add)
        return f"New balance: {account.balance}"

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        acc._transactions = self._transactions + other._transactions
        return acc

    def __reversed__(self):
        return reversed(self._transactions)

    def add_transaction(self, amount):
        serializer_value = self.int_serializer(amount)
        if not serializer_value:
            raise ValueError("please use int for amount")
        self._transactions.append(amount)


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

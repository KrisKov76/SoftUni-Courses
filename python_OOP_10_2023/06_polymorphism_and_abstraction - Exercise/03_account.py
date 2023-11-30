class Account:
    def __init__(self, owner, starting_amount=0):
        self.owner = owner
        self._transactions = []
        self.amount = starting_amount

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __iter__(self):
        return iter(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_account = Account(new_owner, self.amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    @property
    def balance(self):
        return self.amount

    def handle_transaction(self, transaction_amount):
        new_balance = self.amount + transaction_amount
        if new_balance < 0:
            raise ValueError("sorry, cannot go in debt!")
        else:
            self._transactions.append(transaction_amount)
            self.amount = new_balance
            return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        new_balance = self.amount + amount
        if new_balance < 0:
            raise ValueError("sorry, cannot go in debt!")
        else:
            self._transactions.append(amount)
            self.amount = new_balance
            return f"New balance: {self.amount}"


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

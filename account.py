class Account:

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('Creating new Account')

    def __init__(self, number, name, balance):
        Account.increment_instance_count()
        self._number = number
        self._name = name
        self._balance = balance

    def __str__(self):
        return 'Account [' + str(self._number) + '] - ' + self._name

    @property
    def balance(self):
        """ The docstring for the balance property """
        return self._balance

class CurrentAccount(Account):
    def __init__(self, number, name, balance, overdraftLimit):
        super().__init__(number, name, balance)
        self.overdraftLimit = overdraftLimit

    def __str__(self):
        return super().__str__() + ', current account = ' + str(self._balance) + ', overdraft limit: ' + str(self.overdraftLimit)

    def withdraw(self, amount):
        if amount < self.overdraftLimit:
            self._balance -= amount
        else: print('Withdrawal would exceed your overdraft limit')

    def deposit(self, amount):
        self._balance += amount

class DepositAccount(Account):

    def __init__(self, number, name, balance, interestRate):
        super().__init__(number, name, balance)
        self.interestRate = interestRate

    def __str__(self):
        return super().__str__() + ', savings account = ' + str(self._balance) + ', interest rate: ' + str(self.interestRate)

class InvestmentAccount(Account):

    def __init__(self, number, name, balance, investmentType):
        super().__init__(number, name, balance)
        self.investmentType = investmentType

    def __str__(self):
        return super().__str__() + ', investment account = ' + str(self._balance)

acc1 = CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')

print(acc1)
print(acc2)
print(acc3)

acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.balance)

print('Number of Account instances created:', Account.instance_count)
print('balance:', acc1.balance)
acc1.withdraw(300.00)
print('balance:', acc1.balance)
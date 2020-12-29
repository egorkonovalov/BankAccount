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

    def deposit(self, amount):
        if amount < 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, 'Cannot withdraw negative amounts')
        else:
            self._balance += amount

    @property
    def balance(self):
        """ The docstring for the balance property """
        return self._balance

    def __str__(self):
        return f'Account [{str(self._number)}] - {self._name}'


class CurrentAccount(Account):
    def __init__(self, number, name, balance, overdraftLimit):
        super().__init__(number, name, balance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, 'Cannot withdraw negative amounts')
        elif self._balance - amount < self.overdraftLimit:
            print('Withdrawal would exceed your overdraft limit')
            raise BalanceError(self)
        else:
            self._balance -= amount

    def __str__(self):
        return f'{super().__str__()}, current account = {str(self._balance)}, overdraft limit: {str(self.overdraftLimit)}'


class AmountError(Exception):
    """ Valid amount must be positive """

    def __init__(self, account, message):
        self.account = account
        self.message = message

    def __str__(self):
        return f'AmountError ({self.message} on {str(self.account)})'

class BalanceError(Exception):
    """ Balance can not be negative """

    def __init__(self, amount, message='BalanceError (The balance can not be below an overdraft limit)'):
        self.amount = amount
        self.message = message

    def __str__(self):
        return self.message

class DepositAccount(Account):

    def __init__(self, number, name, balance, interestRate):
        super().__init__(number, name, balance)
        self.interestRate = interestRate

    def __str__(self):
        return f'{super().__str__()} savings account = {str(self._balance)} interest rate: {str(self.interestRate)}'

class InvestmentAccount(Account):

    def __init__(self, number, name, balance, investmentType):
        super().__init__(number, name, balance)
        self.investmentType = investmentType

    def __str__(self):
        return f'{super().__str__()} investment account = {str(self._balance)}'

acc1 = CurrentAccount('123', 'John', 10.05, -100.0)
acc2 = DepositAccount('345', 'John', 23.55, 0.5)
acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')

print(acc1)
#print(acc2)
#print(acc3)

#acc1.deposit(23.45)
#acc1.withdraw(12.33)
#print('balance:', acc1.balance)

#print('Number of Account instances created:', Account.instance_count)
#print('balance:', acc1.balance)
#acc1.withdraw(300.00)
#print('balance:', acc1.balance)

try:
    acc1.deposit(-500)
except AmountError as e:
    print(e)

try:
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)
except BalanceError as e:
    print('Handling Exception')
    print(e)
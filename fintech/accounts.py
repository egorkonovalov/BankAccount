from abc import ABCMeta
from timeit import default_timer

# This is a module containing types of accounts


#This decorator is used for logging how long a method takes to execute:
def timer(func):
    def inner(self, value):
        print('calling ', func.__name__, 'on', self, 'with', value)
        start = default_timer()
        func(self, value)
        end = default_timer()
        print('returned from ', func.__name__, 'it took', end - start, 'seconds')
    return inner


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


class Account(metaclass=ABCMeta):
    """ A class that represents a type of account """

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

    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        print(f'__getattr__: unknown attribute accessed - {attribute}')
        return -1

    def __enter__(self):
        print('__enter__')
        return self

    # Args exception type, exception value and traceback
    def __exit__(self, *args):
        print('__exit__:', args)
        return True

    @timer
    def deposit(self, amount):
        if amount < 0:
            raise AmountError(account=self, message='Cannot deposit negative amounts')
        else:
            self._balance += amount

    @timer
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

    @timer
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

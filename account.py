from fintech.accounts import *

# acc1 = CurrentAccount('123', 'John', 10.05, -100.0)
# acc2 = DepositAccount('345', 'John', 23.55, 0.5)
# acc3 = InvestmentAccount('567', 'Phoebe', 12.45, 'high risk')

# print(acc1)
# print(acc2)
# print(acc3)

# acc1.deposit(23.45)
# acc1.withdraw(12.33)
# print('balance:', acc1.balance)

# print('Number of Account instances created:', Account.instance_count)

# try:
#    acc1.deposit(-500)
# except AmountError as e:
#    print(e)

# try:
#    print('balance:', acc1.balance)
#    acc1.withdraw(300.00)
#    print('balance:', acc1.balance)
# except BalanceError as e:
#    print('Handling Exception')
#    print(e)

with CurrentAccount ('891', 'Adam', 5.0, -50.0) as acc:
    acc.deposit(23.0)
    acc.withdraw(12.33)
    print(acc.balance)
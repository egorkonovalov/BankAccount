# Set up sets
print('Accounts:')
print('-' * 25)
salary = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
savings = {'Kirsty', 'Emily', 'Ian', 'Stuart'}
# Output the basic sets
print('salary:', salary)
print('savings:', savings)
print('-' * 25)
print('Opened both the salary and a savings account: ', salary.intersection(savings))
print('Opened only the salary: ', salary.difference(savings))
print('Only opened the savings: ', savings.difference(salary))
print('Opened either (or both) of the salary and the savings account: ', salary.union(savings))
print('Opened either (but not both) of the salary and the savings account: ', salary.symmetric_difference(savings))
print('-' * 25)
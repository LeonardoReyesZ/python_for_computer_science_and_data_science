# ex_10.16.py
"""Account Inheritance Hierarchy."""

from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

mySavingAccount = SavingsAccount('Samantha', 20000, .1)
myCheckingAccount = CheckingAccount('Andrea', 50000, .1)

print(f'{mySavingAccount}\nInterest generated: ${mySavingAccount.calculate_interest()}')
mySavingAccount.deposit(mySavingAccount.calculate_interest())
print(f'Current balance: ${mySavingAccount.balance}', end='\n\n')

print(f'{myCheckingAccount}')
myCheckingAccount.deposit(10000)
print(f'After deposit: $10000')
print(f'Current balance: ${myCheckingAccount.balance}')
myCheckingAccount.withdraw(50000)
print(f'After withdraw: $50000')
print(f'Current balance: ${myCheckingAccount.balance}')
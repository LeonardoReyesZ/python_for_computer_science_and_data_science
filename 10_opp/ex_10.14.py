# ex_10.14
"""Creating an account data class dynamically"""

from dataclasses import make_dataclass

# list of attribute names
fields = ['account', 'name', 'balance']

# dynamically create the Account data class
Account = make_dataclass('Account', fields)


# example usage
account1 = Account(account='001', name='John Doe', balance=10000)
account2 = account1
account3 = Account(account='003', name='Stacy Smith', balance=20000)

print(account1)
print(account2)
print(account3, end='\n\n')

print(f"account1 == account2: {account1 == account2}")
print(f"account1 == account3: {account1 == account3}")
print(f"account2 == account3: {account2 == account3}")
print(f"account1 != account2: {account1 != account2}")
print(f"account1 != account3: {account1 != account3}")
print(f"account2 != account3: {account2 != account3}")
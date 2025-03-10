# ex_10.6
"""Duck typing"""
from decimal import Decimal
from commissionemployee import CommissionEmployee
from salariedcommissionemployee import SalariedCommissionEmployee
from salariedemployee import SalariedEmployee


class WellPaidDuck:
    def __repr__(self):
        return 'I am a well paid duck'

    def earnings(self):
        return Decimal('1_000_000.00')


c = CommissionEmployee("sue", "Jones", '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
s = SalariedCommissionEmployee("Bob", "Lewis", '444-44-4444', Decimal('5000.00'),
                               Decimal('0.04'), Decimal('300.00'))

f = SalariedEmployee("Leonardo", "Reyes", '666-66-6666', Decimal('5_000_000_000'))

d = WellPaidDuck()

employees = [c,s,f,d]

for employee in employees:
    print(employee)
    print(f'{employee.earnings():,.2f}\n')

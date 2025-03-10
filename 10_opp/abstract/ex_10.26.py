# ex_10.26.py
from Employee import Employee
from SalariedEmployee import SalariedEmployee
from HourlyEmployee import HourlyEmployee

#employee = Employee('Sam', 'Smith', '33-333-3333') # error

salariedEmployee = SalariedEmployee('Sam', 'Smith', '33-333-3333', 600)
hourlyEmployee = HourlyEmployee('Bryan', 'Adams', '22-222-2222', 50, 10)

print(salariedEmployee)
print(f"earnings: ${salariedEmployee.earnings()}\n")

print(hourlyEmployee)
print(f"earnings: ${hourlyEmployee.earnings()}\n\n")


employees = [salariedEmployee, hourlyEmployee]

for employee in employees:
    print(employee)
    print(f"earnings: ${employee.earnings()}\n")
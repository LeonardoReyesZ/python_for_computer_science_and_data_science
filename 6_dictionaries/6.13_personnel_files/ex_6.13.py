staff_members = {
    1001: {'Name': 'Alice Smith', 'Date of Birth': '1980-01-15', 'Office Branch': 'New York'},
    1002: {'Name': 'Bob Johnson', 'Date of Birth': '1975-03-22', 'Office Branch': 'Chicago'},
    1003: {'Name': 'Charlie Lee', 'Date of Birth': '1990-07-19', 'Office Branch': 'San Francisco'},
    1004: {'Name': 'Diana Ross', 'Date of Birth': '1985-05-30', 'Office Branch': 'Los Angeles'}
}

# Display the staff information
for personnel_number, info in staff_members.items():
    print(f'Personnel Number: {personnel_number}')
    for key, value in info.items():
        print(f'\t{key}: {value}')
    print()

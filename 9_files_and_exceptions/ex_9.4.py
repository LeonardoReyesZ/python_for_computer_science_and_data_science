# ex_9.4: Reading students records from a csv file
import csv

try: # try to open grades.csv file
    with open('grades.csv', 'r', newline='') as file:
        print( f'{"First Name":<15}{"Last Name":<15}{"Exam 1":^8}{"Exam 2":^8}{"Exam 3":^8}' )
        print( '-'*54)
        reader = csv.reader(file)
        for record in reader:
            firstName, lastName, exam1, exam2, exam3 = record # get the data
            print( f'{firstName.upper():<15}{lastName.upper():<15}{exam1:^8}{exam2:^8}{exam3:^8}' )

except FileNotFoundError:
    print( "The file 'grades.csv' was not found.")
except Exception as e:
    print( f"An error occurred: {e}")
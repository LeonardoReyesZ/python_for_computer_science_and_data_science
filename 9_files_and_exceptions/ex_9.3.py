# ex_9.3: Writing student records to a csv file
import csv

with open('grades.csv', 'w', newline='') as file: # open or create grades.csv file
    writer = csv.writer(file)

    while True:
        # Collect student information
        firstName = input( "\nEnter student's first name (or type 'done' to finish): " )
        if firstName.lower() == 'done':
            print( "\nData entry finished. Records saved to grades.csv.")
            break

        lastName = input( "Enter student's last name: ")

        # collect and validate exam grades
        try:
            exam1Grade = int(input("Enter exam 1 grade: "))
            exam2Grade = int(input("Enter exam 2 grade: "))
            exam3Grade = int(input("Enter exam 3 grade: "))

        except ValueError:
            print( "Invalid input for grades. Please enter integer values." )
            continue

        # write the student record to the csv file
        writer.writerow( [firstName, lastName, exam1Grade, exam2Grade, exam3Grade] )
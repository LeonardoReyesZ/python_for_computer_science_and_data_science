# ex_9.6: Writing a gradebook dictionary to a JSON file
import json

gradebook_dict = { 'students': [] } # dictionary to collect students data

while True: # collect data
    firstName = input("\nEnter student's first name (or type 'done' to finish): ")

    if firstName.lower() == 'done': # finish collection
        print( "\nData entry finished. Records saved to grades.json\n")
        break

    lastName = input("Enter student's last name: ")

    try:
        exam1Grade = int(input("Enter exam 1 grade: "))
        exam2Grade = int(input("Enter exam 2 grade: "))
        exam3Grade = int(input("Enter exam 3 grade: "))
    except ValueError:
        print( "Invalid input for grades. Please enter integers values" )
        continue

    # append the students data as a dictionary to the list of students in gradebook_dict
    gradebook_dict['students'].append({'first_name': firstName, 'last_name': lastName,
                                       'exam1': exam1Grade, 'exam2': exam2Grade, 'exam3': exam3Grade})

# write the gradebook_dict to a JSON file
with open('grades.json', 'w') as file:
    json.dump(gradebook_dict, file, indent=4)
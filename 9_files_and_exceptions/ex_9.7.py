# ex_9.7: Reading gradebook dictionary from a JSON file
import json

try: # try to open grades.json file in a read mode
    with open('grades.json', 'r') as file:
        file_json = json.load(file)

    students = file_json.get('students', [])

    if not students:
        print( "No student data found." )

    else:
        print( f'{"First Name":<15}{"Last Name":<15}{"Exam 1":<8}{"Exam 2":<8}{"Exam 3":<8}{"Average"}' )
        print('-'*61)

        totalExam1 = []
        totalExam2 = []
        totalExam3 = []
        classAverages = []

        # get each student data
        for student in students:
            firstName = student['first_name']
            lastName = student['last_name']
            exam1 = student['exam1']
            exam2 = student['exam2']
            exam3 = student['exam3']

            studentAverage = (exam1+exam2+exam3) / 3

            print( f'{firstName:<15}{lastName:<15}{exam1:<8.2f}{exam2:<8.2f}{exam3:<8.2f}{studentAverage:.2f}')

            totalExam1.append(exam1)
            totalExam2.append(exam2)
            totalExam3.append(exam3)
            classAverages.append(studentAverage)

        print('-' * 61)
        print( f'{"Class averages: ":<30}{sum(totalExam1)/len(totalExam1):<8.2f}{sum(totalExam2)/len(totalExam2):<8.2f}'
           f'{sum(totalExam3)/len(totalExam3):<8.2f}{sum(classAverages)/len(classAverages):.2f}')

except FileNotFoundError:
    print( "The file grades.json was not found" )
except Exception as e:
    print( f"An error occurred: {e}")
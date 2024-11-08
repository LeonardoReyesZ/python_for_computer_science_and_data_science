# ex_9.5: Creating a grade report from a csv file
import csv

try: # try to open grades.csv file
    with open('grades.csv', 'r', newline='') as file:
        print( f'{"First Name":<15}{"Second Name":<15}{"Exam 1":<8}{"Exam 2":<8}{"Exam 3":<8}{"Average"}' )
        print( '-'*61)
        reader = csv.reader(file)

        totalExam1 = []
        totalExam2 = []
        totalExam3 = []
        classAverages = []

        for record in reader: # get data
            firstName, secondName, exam1, exam2, exam3 = record
            studentAverage = (float(exam1)+float(exam2)+float(exam3)) / 3
            print(f'{firstName.upper():<15}{secondName.upper():<15}{exam1:<8}{exam2:<8}{exam3:<8}{studentAverage:.2f}')
            totalExam1.append( float(exam1) )
            totalExam2.append( float(exam2) )
            totalExam3.append( float(exam3) )
            classAverages.append( studentAverage )

        print('-' * 61)
        print( f'{"Class Averages":<30}{sum(totalExam1)/len(totalExam1):<8.2f}{sum(totalExam2)/len(totalExam2):<8.2f}'
               f'{sum(totalExam3)/len(totalExam3):<8.2f}{sum(classAverages)/len(classAverages):.2f}' )

except FileNotFoundError:
    print( "The file 'grades.csv' was not found." )
except Exception as e:
    print( f"An error occurred: {e}" )
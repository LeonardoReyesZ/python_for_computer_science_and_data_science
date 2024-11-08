# ex_9.8: pickle object serialization and deserialization
import pickle

def input_student_data():
    """Read student data and save it to a .p file"""
    gradebook_dict = { 'students': [] } # dictionary to collect students data
    while True: # collect data
        firstName = input("\nEnter student's first name (or type 'done' to finish): ")

        if firstName.lower() == 'done': # finish collection
            print( "\nData entry finished. Records saved to grades.p\n")
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

    # write the gradebook_dict to a pickle file
    pickle.dump( gradebook_dict, open("grades.p", "wb") )
# end input_student_data()


def display_data():
    """Read and display student data from a .p file"""
    try:  # try to open grades.json file in a read mode
        file_p = pickle.load( open("grades.p", "rb") )

        students = file_p.get('students', [])

        if not students:
            print("No student data found.")

        else:
            print(f'{"First Name":<15}{"Last Name":<15}{"Exam 1":<8}{"Exam 2":<8}{"Exam 3":<8}{"Average"}')
            print('-' * 61)

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

                studentAverage = (exam1 + exam2 + exam3) / 3

                print(f'{firstName:<15}{lastName:<15}{exam1:<8.2f}{exam2:<8.2f}{exam3:<8.2f}{studentAverage:.2f}')

                totalExam1.append(exam1)
                totalExam2.append(exam2)
                totalExam3.append(exam3)
                classAverages.append(studentAverage)

            print('-' * 61)
            print(
                f'{"Class averages: ":<30}{sum(totalExam1) / len(totalExam1):<8.2f}{sum(totalExam2) / len(totalExam2):<8.2f}'
                f'{sum(totalExam3) / len(totalExam3):<8.2f}{sum(classAverages) / len(classAverages):.2f}')

    except FileNotFoundError:
        print("The file grades.p was not found")
    except Exception as e:
        print(f"An error occurred: {e}")
# end display_data()


# test pickle file processing
input_student_data()
display_data()
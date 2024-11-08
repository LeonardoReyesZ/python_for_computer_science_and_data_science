# ex_9.1: writing grades to a plain text file

print("Enter the grades, (type 'done' to finish):")

# open or create grades.txt
with open('grades.txt', 'w') as file:
    while True:
        grade = input("-> ")

        # check if users wants to stop inputting grades
        if grade.lower() == 'done':
            print( "Grades saved to grades.txt")
            break

        try:
            # try to convert the input to a float to validate it's a number
            grade_value = float(grade)
            file.write(f"{grade_value}\n") # write grade to file
        except ValueError:
            print("Invalid grade. Please enter a number or 'done' to finish.")
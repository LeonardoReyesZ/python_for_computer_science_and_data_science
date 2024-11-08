# ex_9.2: Reading grades from a plain text file

# open grades.txt file in reading mode
with open('grades.txt', 'r') as file:
    # read all the lines, strip newlines, and convert them to floats
    grades = [float(line.strip()) for line in file.readlines()]

    print(f'Grades in the file:')
    print(grades)

    print( f'\nCount of grades: {len(grades)}')
    print( f'Total of the grades: {sum(grades)}')
    print( f'Average of the grades: {sum(grades) / len(grades):.2f}')
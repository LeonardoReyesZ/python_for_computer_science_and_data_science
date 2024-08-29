# ex_8.11: Evaluate Word Problems

# mapping word numbers to digits
word_to_digit = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

# mapping operations to lambda functions
operations = {
    "plus": lambda x,y: x+y,
    "minus": lambda x,y: x-y,
    "times": lambda x,y: x*y,
    "divided by": lambda x,y: x/y
}

# mapping word operation to operand
operators = {
    "plus": '+',
    "minus": '-',
    "times": '*',
    "divided by": '/'
}


def word_operation( problem ):
    """Solve a mathematical word problem"""
    # tokenize the problem
    words = problem.split()
    number1 = word_to_digit[words[0]]
    number2 = word_to_digit[words[-1]]

    # extract operation (can be one or two words)
    if "divided" in words:
        operation = "divided by"
    else:
        operation = words[1]

    # perform operation
    result = operations[operation](number1, number2)

    print( f"{number1} {operators[operation]} {number2} = {result}" )
# end word_operation()


# test the program
operation = input("Enter a mathematical word problem(number1 + operation + number2): ").lower()

try:
    word_operation(operation)
except KeyError:
    print("Invalid input! Please ensure you're using words for numbers 0-9 and valid operations.")


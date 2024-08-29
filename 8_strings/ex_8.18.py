# ex_8.18: Password Validation
import re

def validate_password( password ):
    """Validate if a password contains at least one lowercase, one uppercase, one digit and no blanks"""
    # pattern to validate a password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\s]{8,}$'

    # check if the password meets the requirements
    return re.match(pattern, password)
# end validate_password()


def feedback( password ):
    """Provide validation feedback."""
    if not re.search(r'[a-z]', password):
        print( "Password must contain at least one lowercase letter." )

    if not re.search(r'[A-Z]', password):
        print( "Password must contain at least one uppercase letter." )

    if not re.search(r'\d', password):
        print( "Password must contain at least one digit" )

    if re.search(r'\s', password):
        print( "Password must not contain spaces" )

    if len(password) < 8:
        print( "Password must be at least 8 characters long.")
# end feedback


# test the program
print( "A valid password contains at least one lowercase, one uppercase, one digit and no blanks")
user_password = input("Enter your password: ")

# validate user password
if validate_password( user_password ):
    print( "\nYour password is valid!" )

else:
    print( f"\nInvalid password")
    feedback(user_password)
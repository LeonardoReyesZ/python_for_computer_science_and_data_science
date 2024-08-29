# ex_8.19: Regular Expression Tester
import re

def regex( pattern, test_string ):
    """Test a regular expression pattern"""
    # compile the regular expression pattern into a reegex object
    regex = re.compile( pattern )

    # find all matches in the string
    matches = regex.finditer( test_string )

    # print matches and their positions
    if matches:
        print( f"Matches for pattern '{pattern}':" )
        for match in matches:
            print( f"Match '{match.group()}' found at positions {match.start()} to {match.end()-1}" )

    else:
        print( f"Not matches found for pattern '{pattern}'")
# end test_regex()


# run regular expression tester
pattern = input("Enter the regular expression pattern: ")
test_string = input("Enter the test string: ")

print()

regex( pattern, test_string )
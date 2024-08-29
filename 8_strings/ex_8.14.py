# ex_8.14: capturing substrings
import re

def b_words():
    text = input("Enter the text line: ").lower()

    # tokenize the line of text using regular expressions to find all words
    words = re.findall(r'\b\w+\b', text)

    # filter and print matches
    for word in words:
        if re.match(r'^b', word):
            print( word )
# end of b_words()

def ed_words():
    text = input("Enter the text line: ").lower()

    # tokenize the line of text using regular expressions
    words = re.findall(r'\b\w+\b', text)

    # filter and print the matches
    for word in words:
        if re.search(r'ed\b', word):
            print( word )
# end ed_words()

# test the program
b_words()
print()
ed_words()

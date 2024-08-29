# ex_8.5: tokenizing and comparing strings

# read a line of text amd save it in lower case
text = input("Enter a line of text: ").lower()

# tokenize the line of text
words = text.split()

# filter the words that start with 'b'
b_words = [word for word in words if word.startswith('b')]

if b_words:
    print( f"Words that start with 'b': {' '.join(b_words)}" )

else:
    print("No words starting with 'b' found.")
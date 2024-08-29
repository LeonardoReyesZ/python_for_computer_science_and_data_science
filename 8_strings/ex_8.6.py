# ex_8.6: tokenizing and comparing strings

# Read a line of text (lower case)
sentence = input("Enter a sentence: ").lower()

# Tokenize the sentence into words (using space as the delimiter)
words = sentence.split()

# Filter words that end with 'ed'
ed_words = [word for word in words if word.endswith('ed')]

# Output the filtered words
if ed_words:
    print("Words ending with 'ed':", " ".join(ed_words))
else:
    print("No words ending with 'ed' found.")

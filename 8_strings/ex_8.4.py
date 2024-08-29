# ex_8.4: Sorting word in a sentence

# read a line of a text and save it in lower case
text = input("Enter the text line: ").lower()

# toketinze the sentence into sorted words
sorted_words = sorted( text.split() )

print( f"Sorted Words: {' '.join(sorted_words)}" )

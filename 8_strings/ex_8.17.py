# ex_8.17: Regular Expression for autocorrection
import re

def autocorrect( text ):
    """Function to correct words with two capital letters."""
    # pattern to find words that start with two capital letters.
    pattern  = r'\b([A-Z])([A-Z])'

    # function to replace the second capital letter to lower case
    def correct( match ):
        return match.group(1) + match.group(2).lower()

    # correct the words
    correction = re.sub( pattern, correct, text )

    return correction
# end autocorrect()


# text sample
text_sample = "I met with JOhn yesterday. We discussed the TAble and CHairs."
corrected_text = autocorrect( text_sample )

print( f"Original text:\n{text_sample}\n")
print( f"Corrected text:\n{corrected_text}")

# ex_8.12: scrambled text
import random

def scramble_word(word):
    """Scramble the letters of a word, except for the first and last letters."""
    if len(word) <= 3:  # Words with 3 or fewer characters are returned unchanged
        return word

    # Keep the first and last letters in place
    first_letter = word[0]
    last_letter = word[-1]

    # Middle letters to be scrambled
    middle_letters = list(word[1:-1])

    # Scramble the middle letters
    random.shuffle(middle_letters)

    # Reconstruct the word with scrambled middle letters
    scrambled_word = first_letter + ''.join(middle_letters) + last_letter

    return scrambled_word
# end scramble_word


def scramble_text(text):
    """Scramble each word in the text."""
    words = text.split()  # Split the text into individual words
    scrambled_words = [scramble_word(word) for word in words]  # Scramble each word

    # Rejoin the scrambled words into a full sentence
    scrambled_sentence = ' '.join(scrambled_words)

    return scrambled_sentence
# end scramble_text()


# Example usage
text_sample = "This is an example sentence for the scrambling project"
scrambled_output = scramble_text(text_sample)
print(f"Scrambled text: {scrambled_output}")

import difflib

def load_dictionary(file_path):
    """Load dictionary from a file into a set for faster lookup."""
    with open(file_path, 'r') as f:
        words = {line.strip().lower() for line in f}
    return words
# end load_dictionary

def check_spelling(text, dictionary):
    """Check the spelling of words in the provided text."""
    # Split the text into words and remove punctuation
    words = [word.strip(".,!?;:") for word in text.split()]

    misspelled_words = {}
    for word in words:
        if word.lower() not in dictionary:
            # Find the closest matches from the dictionary
            suggestions = difflib.get_close_matches(word.lower(), dictionary, n=3, cutoff=0.85)
            if suggestions:
                misspelled_words[word] = suggestions
            else:
                misspelled_words[word] = None  # No suggestions

    return misspelled_words
# end check_spelling

def main():
    # Load the dictionary of correct words
    dictionary = load_dictionary("dictionary.txt")

    # Read the text file with the content to check
    with open("text.txt", 'r') as f:
        text = f.read().lower()

    # Check for spelling mistakes
    misspelled_words = check_spelling(text, dictionary)

    # Print out misspelled words and suggestions
    if misspelled_words:
        print("Misspelled words and suggestions:")
        for word, suggestions in misspelled_words.items():
            if suggestions:
                print(f"{word}: Suggested corrections: {', '.join(suggestions)}")
            else:
                print(f"{word}: No suggestions found")
    else:
        print("No spelling mistakes found!")
# end main

if __name__ == "__main__":
    main()

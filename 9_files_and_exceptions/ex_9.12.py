# ex_9.12: state-of-the-union speeches
import re
from collections import Counter
# read file
with open('speech.txt', 'r') as file:
    text = file.read()

    cleaned_text = re.sub(r'[^\w\s-]', '', text)  # Remove all punctuation except hyphens
    cleaned_text = re.sub(r'-+', ' ', cleaned_text)  # Replace one or more hyphens with a space

    # split text into words
    words = cleaned_text.split()

    # split text into sentences
    sentence_pattern = r'(?<!\d)(?<!\b[A-Z])\s*[.!?:;]+(?!\s*")|--'
    sentences = re.split(sentence_pattern, text)
    sentences = [sentence.strip() for sentence in sentences]

    # statistics
    total_word_count = len(words)  # total word count
    total_character_count = len(cleaned_text.replace(" ", ""))

    # average word length
    average_word_length = total_character_count / total_word_count

    # average sentence length (in words)
    sentence_word_count = [len(sentence.split()) for sentence in sentences]
    average_sentence_length = sum(sentence_word_count) / len(sentence_word_count)

    word_distribution = Counter(words) # word distribution

    # word distribution of words ending in 'ly'
    ly_words = [word for word in words if word.endswith('ly')]
    ly_word_distribution = Counter(ly_words)

    # 10 longest words
    longest_words = sorted(words, key=len, reverse=True)[:10]

    # Displaying the results
    print(f"Total word Count: {total_word_count}")
    print(f"Total character Count: {total_character_count}")
    print(f"Average word length: {average_word_length:.2f}")
    print(f"Average sentence length: {average_sentence_length:.2f}")

    print(f"\nWord distribution:")
    for word, count in word_distribution.items():
        print(f"{word+':'} {count}")

    print(f"\nWord distribution of words ending in 'ly':")
    for word, count in ly_word_distribution.items():
        print(f"{word+':'} {count}")

    print("\n10 longest words:")
    for word in longest_words:
        print(word)
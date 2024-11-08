# ex_9.14: Basic similarity detection via average sentence length and average word length
import re
from collections import Counter

def statistics(text, title):
    """Function to display the statistics of a text."""
    # clean texts
    text_cleaned = re.sub(r'[_]|[^\w\s-]', '', text)
    text_cleaned = re.sub(r'-+', ' ', text_cleaned)

    # split text into words
    words = text_cleaned.split()

    # split text into sentences
    sentence_pattern = r'(?<!\d)(?<!\b[A-Z])(?<![IVXLCDM])\s*[.!?;]+(?!\s*")(?!\s*_)|--'
    sentences = re.split(sentence_pattern, text)
    sentences = [sentence.replace('\n', ' ').replace('\t', '').strip()
                                  for sentence in sentences]

    word_count = len(words)
    character_count = len(text_cleaned.replace(" ", ""))

    # average word length
    average_word_length = character_count / word_count

    # average sentence length (in words)
    sentence_word_count = [len(sentence.split()) for sentence in sentences]
    average_sentence_length = sum(sentence_word_count) / len(sentence_word_count)

    # word distribution
    romeo_and_juliet_word_distribution = Counter(words)

    # 10 longest words
    longest_words = sorted(words, key=len, reverse=True)[:10]

    # display statistics
    print(title)
    print(f"Total word Count: {word_count}")
    print(f"Total character Count: {character_count}")
    print(f"Average word length: {average_word_length:.2f}")
    print(f"Average sentence length: {average_sentence_length:.2f}")

    print(f"\nWord distribution:")
    for word, count in romeo_and_juliet_word_distribution.items():
        print(f"{word + ':'} {count}")

    print("\n10 longest words:")
    for word in longest_words:
        print(word)
# end statistics()


# read files
with (open('romeo_and_juliet.txt', 'r') as romeo_and_juliet_file,
      open('new_atlantis.txt', 'r') as new_atlantis_file):

    romeo_and_juliet = romeo_and_juliet_file.read()
    new_atlantis = new_atlantis_file.read()

    statistics(romeo_and_juliet, "Romeo and Juliet")
    print("\n\n")
    statistics(new_atlantis, "New Atlantis")
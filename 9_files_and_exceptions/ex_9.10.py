# ex_9.10: Analyzing a book from project gutenberg
import re
from collections import Counter

with open('pride_and_prejudice.txt', 'r') as file:
    file = file.read()

    cleaned_text = re.sub(r'[^\w\s-]|_+', '', file) # remove all punctuation except hyphens
    cleaned_text = re.sub(r'-+', ' ', cleaned_text) # replace one or more hyphens with a space

    # split the text into words
    words = cleaned_text.split()

    # split the text into sentences
    sentence_pattern = r'(?<!\d)(?<![A-Z])(?<!Mr)(?<!Mrs)(?<!etc)\s*[.!?:;]+'
    cleaned_text = file.replace("\n", " ")
    cleaned_text = re.sub(r'[\“\”()_\[\]\’\‘-]', "", cleaned_text) # clean the text
    cleaned_text = cleaned_text.split() # split into words
    cleaned_text = " ".join(line.strip() for line in cleaned_text) # rebuild sentences without extra spaces
    sentences = re.split(sentence_pattern, cleaned_text ) # split the text into sentences

    # statistics
    total_word_count = len(words) # total word count
    total_character_count = len(cleaned_text.replace(" ", ""))

    # average word length
    average_word_length = total_character_count / total_word_count

    # average sentence length (in words)
    sentence_word_count = [len(sentence.split()) for sentence in sentences]
    average_sentence_length = sum(sentence_word_count) / len(sentence_word_count)

    word_distribution = Counter(words) # word distribution

    # 10 longest words
    longest_words = sorted(words, key=len, reverse=True)[:10]

    # Display results
    print( f"Total word count: {total_word_count}\n"
           f"Total character count: {total_character_count}\n"
           f"Average word length: {average_word_length:.2f}\n"
           f"Average sentence length: {average_sentence_length:.2f}\n" )

    print( "\nWord distribution:")
    for word, count in word_distribution.items():
        print( f"{word+':'} {count}" )

    print( "\n10 longest words:" )
    for word in longest_words:
        print(word)
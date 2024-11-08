# ex_9.11: visualizing word frequencies with a word cloud
import re
from collections import Counter
from wordcloud import WordCloud

wordcloud = WordCloud(colormap='prism', background_color='white')

with open('pride_and_prejudice.txt', 'r') as file:
    file = file.read()

    cleaned_text = re.sub(r'[^\w\s-]|_+', '', file)  # remove all punctuation except hyphens
    cleaned_text = re.sub(r'-+', ' ', cleaned_text) # replace one or more hyphens with a space

    words = cleaned_text.split() # split text into words

    word_distribution = Counter(words)

    # get the top 200 most common words
    top_200_words = word_distribution.most_common(200)

    # get the frequencies into a dictionary
    frequencies = {word: count for word, count in top_200_words}

    # generate a rectangular word cloud and save its image to a file on disk
    wordcloud = wordcloud.fit_words(frequencies)
    wordcloud = wordcloud.to_file('PrideAndPrejudice.png')
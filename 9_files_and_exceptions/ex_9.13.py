# ex_9.13: building a basic sentiment analyzer
import re

def simple_sentiment_analysis(text, positive_words, negative_words):
    """Function to determine if a text is positive or negative."""
    words = text.split()

    # initialize the counters for positive and negative words
    positive_count = 0
    negative_count = 0

    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    # determine the overall sentiment
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"
# end simple_sentiment_analysis


with (open("positive_words.txt", 'r') as positive_words,
      open("negative_words.txt", 'r') as negative_words,
      open("tweet.txt", 'r') as tweet):

    positive_words = list(positive_words.read().lower().split())
    negative_words = list(negative_words.read().lower().split())
    tweet = tweet.read().lower()

    cleaned_tweet = re.sub(r'[^\w\s]', '', tweet) # cleaned the text

    print(f"The tweet is: {simple_sentiment_analysis(cleaned_tweet, positive_words, negative_words)}")
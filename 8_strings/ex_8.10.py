# ex_8.10: simple sentiment analysis
# sample of positive and negative words

# Expanded positive and negative word lists (50 words each)
positive_words = [
    "good", "great", "excellent", "happy", "fortunate", "correct", "superior", "love", "wonderful",
    "fantastic", "amazing", "nice", "positive", "joy", "delight", "pleased", "awesome", "beautiful",
    "brilliant", "cheerful", "content", "ecstatic", "elated", "enjoy", "enthusiastic", "fabulous",
    "glad", "grateful", "healthy", "incredible", "lucky", "marvelous", "optimistic", "outstanding",
    "perfect", "radiant", "satisfied", "skillful", "splendid", "successful", "superb", "terrific",
    "thrilled", "triumphant", "vibrant", "victorious", "worthy", "zestful", "admirable", "charming"
]

negative_words = [
    "bad", "terrible", "awful", "unfortunate", "wrong", "inferior", "hate", "horrible", "disgusting",
    "poor", "negative", "sad", "angry", "upset", "annoyed", "depressed", "unhappy", "painful",
    "dreadful", "miserable", "pathetic", "tragic", "horrid", "atrocious", "despicable", "nasty",
    "offensive", "repulsive", "appalling", "brutal", "cruel", "devastating", "disturbing", "frightening",
    "gloomy", "gruesome", "harmful", "hopeless", "horrendous", "irritating", "loathsome", "mean",
    "nauseating", "painful", "pessimistic", "regretful", "shameful", "unpleasant", "vile", "wretched"
]

# text samples:
text_sample1 = "The new phone is absolutely fantastic and works perfectly. I am so thrilled with this purchase!"
text_sample2 = "The customer service was appalling and the food was dreadful. I would not recommend this restaurant to anyone."
text_sample3 = "The experience was average. Nothing special, but also nothing terrible. Just a regular day."


def simple_sentiment_analysis( text ):
    """Function to determine if a text is positive or negative."""
    text = text.lower() # convert text to lower case
    words = text.split() # split the text into words

    # initialize counters for positive and negative words
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


# test  the program
print( f"The text1 is: {simple_sentiment_analysis(text_sample1)}")
print( f"The text2 is: {simple_sentiment_analysis(text_sample2)}")
print( f"The text3 is: {simple_sentiment_analysis(text_sample3)}")
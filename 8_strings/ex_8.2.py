# ex_8.2: Random Sentences
import random

# Define arrays of words
articles = ["the", "a", "one", "some", "any", "every", "another", "this", "that", "these"]
nouns = ["boy", "girl", "dog", "town", "car", "cat", "house", "tree", "park", "computer"]
verbs = ["drove", "jumped", "ran", "walked", "skipped", "flew", "swam", "read", "wrote", "sang"]
prepositions = ["to", "from", "over", "under", "on", "with", "by", "beside", "near", "around"]

def generate_sentence():
    """Function to generate a random sentence"""
    sentence = (
        f"{random.choice(articles)} "
        f"{random.choice(nouns)} "
        f"{random.choice(verbs)} "
        f"{random.choice(prepositions)} "
        f"{random.choice(articles)} "
        f"{random.choice(nouns)}"
    )

    # capitalize the first letter and add a period at the end
    sentence = sentence.capitalize() + "."
    return sentence
# end generate_sentence


# generate and print 20 sentences
for _ in range(20):
    print( generate_sentence() )
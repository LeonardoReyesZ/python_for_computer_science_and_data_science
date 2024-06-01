""" Script that uses a dictionary to summarize the frequency of each letter in a given text """

# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# function to count the frequencies in a text and display them
def character_frequency( text ):
    # initialize an empty dictionary to count the frequencies of each letter
    frequency = {}

    # convert the text to lowercase and remove spaces
    cleaned_text = text.lower().replace(" ", "")

    # iterate through the text and calculate frequencies
    for char in cleaned_text:
        if char.isalpha(): # ensure that char is a letter
            # if the letter is already in the dictionary, increment their frequency
            if char in frequency:
                frequency[char] += 1
            # if the letter is not in the dictionary, add them with a count of 1
            else:
                frequency[char] = 1

    # display the two-column table of letters and their frequencies
    print(f"{'Letter':<10}{'Frequency':<10}")
    print('-' * 20)
    for letter, freq in sorted(frequency.items()):
        print(f"{letter:<10}{freq:<10}")

# end function character_frequency


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# test the function with a text
sample_text = "In cryptoanalysis, the technique of character frequency analysis is often used to decipher a message when the key is unknown."
character_frequency( sample_text )

""" script that uses a dictionary to determine the number of votes received by a candidate.
    The votes are concatenated in a string. And make a visual graph """

import matplotlib.pyplot as plt # matplotlib graphing capabilities
import seaborn as sns # seaborn graphing capabilities

# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# function to count the votes and return them in a dictionary
def count_votes( vote_string ):
    # split the vote string by commas to get a list of votes
    votes = vote_string.split(',')

    # initialize an empty dictionary to count votes for each candidate
    vote_count = {}

    # iterate through the list of votes
    for vote in votes:
        # strip any whitespace around the vote
        candidate = vote.strip()

        # if the candidate is already in the dictionary, increment their count
        if candidate in vote_count:
            vote_count[candidate] += 1
        # if the candidate is not in the dictionary, add them with a count of 1
        else:
            vote_count[candidate] = 1

    return vote_count
# end function count_votes


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
vote_string = ("Alice, Bob, Alice, Charlie, Bob, Alice, Bob, Charlie, Charlie, Bob, Alice,"
               "Alice, Bob, Alice, Charlie, Bob, Alice, Bob, Charlie, Charlie, Bob, Alice")
results = count_votes(vote_string) # get the results in a dictionary

# show results in a graph #
# creating the initial bar plot with increased figure size and adjusted dodge
plt.figure(figsize=(14,6)) # increase figure size

# bar plot's title, set style and graph the votes
title = 'Total number of votes' # comma specifier
sns.set_style('whitegrid') # style
axes = sns.barplot( x=list(list(results.keys())), y=list(results.values()), palette='bright') # graph
axes.set_title(title) # set title to the object axes
axes.set(xlabel='Candiate', ylabel='Votes') # set labels
axes.set_ylim(top=max(results.values())*1.12) # make room for the text above each bar -> 12% taller

# display text above each bar
for bar, votes in zip(axes.patches, results.values()):
    text_x = bar.get_x() + bar.get_width()/2 # set x position
    text_y = bar.get_height() # set y position
    text = f'{votes:,}\n{votes / sum(results.values()):.3%}' # votes and percentage
    axes.text( text_x, text_y, text, fontsize=12, ha='center', va='bottom') # display text

# display the graph
plt.show()

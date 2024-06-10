""" Script to track the number of games won for a particular number of rolls
    and make a dynamic visualization of the data"""
import random
import matplotlib.pyplot as plt # matplotlib graphing capabilities
import seaborn as sns # seaborn graphing capabilities
import numpy as np

# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
def roll_dice():
    """Roll two dice and return their face value as a tuple."""
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1, die2) # pack die face values into a tuple
# end roll_dice

def play_craps():
    """Play the game of craps."""
    die_values = roll_dice() # first roll
    rolls_count = 1
    #display_dice( die_values )

    # determine game status and point, based on first roll
    sum_of_dice = sum( die_values )

    if sum_of_dice in (7, 11): # win
        game_status = 'WON'
    elif sum_of_dice in (2,3,12): # lose
        game_status = 'LOST'
    else: # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        #print('Point is ', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        rolls_count += 1
        #display_dice( die_values )
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point: # win by making point
            game_status = 'WON'
        elif sum_of_dice == 7: # lose by rolling 7
            game_status = 'LOST'

    return game_status, rolls_count # return the result of the game and the number of rolls played
# end play_craps

def simulate_number_of_games(n_games):
    wins_track = {}
    losses_track = {}

    # play n_games and track victories and defeats for each number of rolls
    for roll in range(n_games):
        result, rolls_count = play_craps() # play game and get the results

        # game won or lost after the 24th roll -> unlikely but possible
        # restrict data till the 15th roll to have a better visualization
        if rolls_count > 14:
            rolls_count = 15

        # track victories and defeats
        if result == 'WON':
            # if the number of rolls played is already in the wins_track dictionary
            if rolls_count in wins_track:
                wins_track[rolls_count] += 1 # increment the counter
            # if the number of rolls played is not in the wins_track dictionary
            else:
                wins_track[rolls_count] = 1 # added it with counter 1
        else:
            # if the number of rolls played is already in the losses_track dictionary
            if rolls_count in losses_track:
                losses_track[rolls_count] += 1 # increment the counter
            # if the number of rolls played is not in the losses_track dictionary
            else:
                losses_track[rolls_count] = 1 # added it with counter 1

    # sort the dictionaries
    wins_track = dict(sorted(wins_track.items()))
    losses_track = dict(sorted(losses_track.items()))

    return wins_track, losses_track
# end simulate_number_of_games


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# play 'n_games' games and get the victories and defeats in lists
n_games = 1000000 # games to play
wins, losses = simulate_number_of_games(n_games)
setValues = set(wins.keys()).union(set(losses.keys())) # get all the rolls

values = np.arange(1, len(setValues)+1) # for flexibility
wins = list(wins.values()) # for simplicity
losses = list(losses.values()) # for simplicity

# creating the initial bar plot with increased figure size and adjusted dodge
plt.figure(figsize=(25, 15)) # increase figure size
title = 'Dice Game of Craps'
sns.set_style('whitegrid')
# set the title and labels
plt.title(title)
plt.xlabel('Roll')
plt.ylabel('Number of Games')
plt.xticks(values) # Set x-ticks to be the rolls

# define the width of each bar and the offset for the second set of bars
bar_width = 0.4
offset = bar_width / 2

# plot the games won
plt.bar(values-offset, wins, width=bar_width, label='Games Won', color='blue')
# plot the games lost with an offset
plt.bar(values+offset, losses, width=bar_width, label='Games Lost', color='red')
# add a legend to differentiate the two sets of bars
plt.legend()

# display text above each bar for games won
for i, frequency in enumerate(wins):
    plt.text( values[i]-offset, frequency, f'{frequency}\n{frequency/n_games:.2%}', ha='center', va='bottom' )

# display text above each bar for games lost
for i, frequency in enumerate(losses):
    plt.text( values[i]+offset, frequency, f'{frequency}\n{frequency/n_games:.2%}', ha='center', va='bottom' )

plt.show()

""" Script to track the number of games won for a particular number of rolls.
    And make a dynamic visualization of the data """
from matplotlib import animation
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

# function update -> simulating 'n_games' the game of craps and updating victories and defeats
def update(frame_number, n_games, rolls, bar_width, offset):
    """ Configures bar plot contents for each animation frame. """
    # play n_games and update victories and defeats for each number of rolls
    for roll in range(n_games):
        result, rolls_count = play_craps() # play game and get the results

        # game won or lost after the 24th roll -> unlikely but possible
        # restrict data till the 15th roll to have a better visualization
        if rolls_count > 14:
            rolls_count = 15

        # track victories and defeats
        if result == 'WON':
            # if the number of rolls played is already in the wins_track dictionary
            if rolls_count in rolls['wins']:
                rolls['wins'][rolls_count] += 1 # increment the counter
            # if the number of rolls played is not in the wins_track dictionary
            else:
                rolls['wins'][rolls_count] = 1 # added it with counter 1
        else:
            # if the number of rolls played is already in the losses_track dictionary
            if rolls_count in rolls['losses']:
                rolls['losses'][rolls_count] += 1 # increment the counter
            # if the number of rolls played is not in the losses_track dictionary
            else:
                rolls['losses'][rolls_count] = 1 # added it with counter 1

        # get the total games played till now
        gamesPlayed = sum(rolls['wins'].values()) + sum(rolls['losses'].values())

        # convert data for flexibility
        values = np.arange(1, len(rolls['wins'].keys()) + 1)  # for flexibility
        wins = list(rolls['wins'].values())  # for simplicity
        losses = list(rolls['losses'].values())  # for simplicity

        # reconfigure plot for updated die frequencies
        plt.cla() # clear old contents contents of current figure
        plt.xlabel('Roll')
        plt.ylabel('Number of Games')
        plt.xticks(values)  # Set x-ticks to be the rolls

        # plot the games won
        plt.bar(values - offset, wins, width=bar_width, label='Games Won', color='blue')
        # plot the games lost with an offset
        plt.bar(values + offset, losses, width=bar_width, label='Games Lost', color='red')
        # add a legend to differentiate the two sets of bars
        plt.legend()

        # display text above each bar for games won and their corresponding percentage
        for i, frequency in enumerate(wins):
            plt.text(values[i] - offset, frequency, f'{frequency}\n{frequency / gamesPlayed:.1%}',
                     ha='center', va='bottom', fontsize=3.5)

        # display text above each bar for games lost
        for i, frequency in enumerate(losses):
            plt.text(values[i] + offset, frequency, f'{frequency}\n{frequency / gamesPlayed:.1%}',
                     ha='center', va='bottom', fontsize=3.5)
# end function update


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# configure the graph and maintain the state
# creating the initial bar plot with increased figure size and adjusted dodge
figure = plt.figure('Dice Game of Craps', figsize=(13, 6), dpi=200) # increase figure size
sns.set_style('whitegrid')

# define the width of each bar and the offset for the second set of bars
bar_width = 0.4
offset = bar_width / 2

# play 'n_games' games and get the victories and defeats in dictionaries
n_games = number_of_frames = 1000000 # games to play
rolls_per_frame = 1 # just for this exercise

rolls = {
    'wins': {i: 0 for i in range(1, 16)},
    'losses': {i: 0 for i in range(1, 16)}
}

# configure and start the animation that calls function update
game_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, rolls, bar_width, offset) )

plt.show() # display window

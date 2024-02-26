"""  Simulating the dice game Craps and graph  """
import matplotlib.pyplot as plt # Matplodlib graphing capabilities
import numpy as np
import random
import seaborn as sns # seaborn graphing capabilities


# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# Roll two dice and return their face values as a tuple. #
def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple
# end roll_dice

# Display one roll of the two dice. #
def display_dice(dice):
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
# end display_dice

#  play the game and count the frequencies of wins and loses  #
def play(rolls):
    victories = [0] * 12 # counter for the victories
    defeats = [0]*12 # counter for the defeats

    for roll in range(rolls):
        counter = -1 # to start saving the frequencies from index '0'
        die_values = roll_dice()  # first roll
        counter += 1  # increment counter
        #display_dice(die_values)

        # determine fame status and point, based on first roll
        sum_of_dice = sum(die_values)

        if sum_of_dice in (7, 11):  # win
            game_status = 'WON'
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = 'LOST'
        else:  # remember point
            game_status = 'CONTINUE'
            my_point = sum_of_dice
            #print('Point is', my_point)

        # continue rolling until player victories or loses
        while game_status == 'CONTINUE':
            die_values = roll_dice()
            counter += 1  # increment counter
            #display_dice(die_values)
            sum_of_dice = sum(die_values)

            if sum_of_dice == my_point:  # win by making point
                game_status = 'WON'
            elif sum_of_dice == 7:  # lise by rolling 7
                game_status = 'LOST'

        # frequency of 12 or more ....
        if counter > 11:
            counter = 11

        # display "victories" or "defeats" message
        if game_status == 'WON':
            #print(f'Player victories on roll: {counter+1}')
            victories[counter] = victories[counter] + 1 # increment the frequency in the corresponding roll
        else:
            defeats[counter] = defeats[counter]+1 # increment the frequency in the corresponding roll
            #print(f'Player loses on roll: {counter+1}')

    return (victories, defeats)
# end play

def graph(rolls, frequencies, what):
    # determine the unique games values and their frequencies
    values = [1,2,3,4,5,6,7,8,9,10,11,12]

    # reverse the order of values for y-axis flipping -> highest value at the top
    values = np.flip(values)
    frequencies = np.flip(frequencies)

    # creating the initial bar plot; horizontal
    # bar plot's title, set style and graph the frequencies
    title = f'Dice Game Craps {what} {rolls:,} Games'  # comma specifier
    sns.set_style('whitegrid')  # style
    # set horizontal orientation; set order
    axes = sns.barplot(x=frequencies, y=values, order=values, orient='h', palette='bright')  # graph
    axes.set_title(title)  # set title to object axes
    axes.set(xlabel='Frequency', ylabel='Roll')  # set labels
    # Make room for the text to the right of each bar (15% wider)
    axes.set_xlim(right=max(frequencies) * 1.15)

    # display text on the right of each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_width()  # set x position
        text_y = bar.get_y() + bar.get_height()/2.0  # set y position
        text = f' {frequency:,}\n {frequency / rolls:.3%}'  # frequency and percentange
        axes.text(text_x, text_y, text, fontsize=8, ha='left', va='center')  # display text

    plt.show()
# end graph


# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
# games to play
games = 360
games1 = 36000
games2 = 36000000

# play games and get the victories and defeats
victories, defeats = play(games)
victories1, defeats1 = play(games1)
victories2, defeats2 = play(games2)

# graph victories and defeats
graph(games, victories, "victories")
graph(games, defeats, "defeats")

graph(games1, victories1, "victories")
graph(games1, defeats1, "defeats")

graph(games2, victories2, "victories")
graph(games2, defeats2, "defeats")


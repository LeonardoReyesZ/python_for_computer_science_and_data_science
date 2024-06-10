""" Script to track the number of games won for a particular number of rolls """
import random

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
        if rolls_count > 24:
            rolls_count = 25

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
n_games = 1000000 # games to play
# play 'n_games' games and get the victories and defeats
wins, losses = simulate_number_of_games(n_games)

# print percentages of n_games
wins_percentage = sum(wins.values()) / n_games * 100
losses_percentage = sum(losses.values()) / n_games * 100
print(f"Percentage of wins: {wins_percentage:.2f}%")
print(f"Percentage of losses: {losses_percentage:.2f}%")

print(f"Percentage of wins/losses base on total number of rolls\n\n")
print(f"{'':<7}{'%Resolved':<15}{'Cumulative %':<20}")
print(f"{'Rolls':<7}{'on this roll':<15}{'Cumulative':<20}")

cumulative = 0
# get all the rolls with a victories and defeats
all_rolls = set(wins.keys()).union(set(losses.keys()))

# calculate the percentages of the total games played that were won or lost per roll
for roll in all_rolls:
    resolved_on_this_roll = wins.get(roll, 0) + losses.get(roll, 0)
    percentage_per_roll = resolved_on_this_roll / n_games * 100
    cumulative += percentage_per_roll
    print(f"{roll:<7}{percentage_per_roll:<15.2f}{cumulative:<20.2f}")

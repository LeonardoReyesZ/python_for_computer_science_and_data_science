"""   Rolling two dies, calculate frequencies and show it in a dynamic graph   """
from matplotlib import animation
import matplotlib.pyplot as plt # Matplodlib graphing capabilities
import numpy as np
import random
import seaborn as sns # seaborn graphing capabilities

# ~~~~~~~  Definition of Functions   ~~~~~ ~~~~~~ ~~~~~~~ ~~~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~ ~ #
# function update: rolling the dies and updating frequencies
def update( frame_number, rolls, values, frequencies ):
    """ Configures bar plot contents for each animation frame."""
    # roll the dices and update frequencies
    for i in range( rolls ):
        frequencies[random.randrange(1,7)+random.randrange(1,7)-2] += 1

        # reconfigure plot for updated dies frequencies
        plt.cla() # clear old contents contents of current figure
        # creating the initial bar plot; horizontal
        # bar plot's title, set style and graph the frequencies
        # set horizontal orientation; set order
        axes = sns.barplot(x=frequencies, y=values, order=values, orient='h', palette='bright')  # graph
        title = f'Rolling two Six-Sided Dies {sum(frequencies):,} Rolls'  # comma specifier
        axes.set_title(title)  # set title to object axes
        axes.set(xlabel='Frequency', ylabel='Sum of Dies Values')  # set labels
        # Make room for the text to the right of each bar (15% wider)
        axes.set_xlim(right=max(frequencies) * 1.15)

        # display text on the right of each bar
        for bar, frequency in zip(axes.patches, frequencies):
            text_x = bar.get_width()  # set x position
            text_y = bar.get_y() + bar.get_height() / 2.0  # set y position
            text = f' {frequency:,}\n {frequency / sum(frequencies):.3%}'  # frequency and percentage
            axes.text(text_x, text_y, text, fontsize=8, ha='left', va='center')  # display text
# end function update

# ~~~~~~~~  Program Execution   ~~~~~~~ ~~~~ ~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~~ ~ #
# read arguments for number of frames and rolls per frame
number_of_frames = int(input("Enter the number of frames: "))
rolls_per_frame = int(input("Enter the number of rolls per frame: "))

# configure the graph and maintain state
sns.set_style('whitegrid')  # style
figure = plt.figure('Rolling two Six-Sided Die') # figure for animation

frequencies = [0]*11 # eleven-element list of sum frequencies
values = list(range(2,13)) # sum of die faces for display on y-axis
# reverse the order of values for y-axis flipping -> the highest value at the top
values = np.flip(values)
frequencies = np.flip(frequencies)

# configure and start the animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, values, frequencies))

plt.show() # display window

"""   Simulating the flipping of a coin and count the frequencies  """

import matplotlib.pyplot as plt # Matplodlib graphing capabilities
import numpy as np
import random
import seaborn as sns # seaborn graphing capabilities


# ~~~~~~~~~~   Definition of Functions   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def print_graph(flips):
    # determine the unique flips values and their frequencies
    values, frequencies = np.unique(flips, return_counts=True)

    #  creating the initial bar plot
    # bar plot's title, set style and graph the frequencies
    title = f'Flipping a Coin {len(flips):,} Times'  # comma specifier
    sns.set_style('whitegrid')  # style
    axes = sns.barplot(x=values, y=frequencies, palette='bright')  # graph
    axes.set_title(title)  # set title to object axes
    axes.set(xlabel='Coin Value', ylabel='Frequency')  # set labels
    axes.set_ylim(top=max(frequencies) * 1.10)  # make room for the text above each bar -> 10% taller

    # display text above each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  # set x position
        text_y = bar.get_height()  # set y position
        text = f'{frequency:,}\n{frequency / len(flips):.3%}'  # frequency and percentange
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')  # display text

    # print the graph
    plt.show()
# end function print_graph


# ~~~~~~~~~~  Program Execution   ~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# list of 200 random coin values
flips1 = [random.randrange(1, 3) for i in range(200)]

# list of 20000 random coin values
flips2 = [random.randrange(1,3) for i in range(20000)]

# list of 200000 random coin values
flips3 = [random.randrange(1,3) for i in range(200000)]

# print graphs
print_graph(flips1)
print_graph(flips2)
print_graph(flips3)
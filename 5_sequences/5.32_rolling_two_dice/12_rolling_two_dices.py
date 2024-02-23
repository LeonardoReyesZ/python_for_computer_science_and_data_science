"""   Rolling two dies, calculate frequencies and show it as a bar plots   """
import matplotlib.pyplot as plt # Matplodlib graphing capabilities
import numpy as np
import random
import seaborn as sns # seaborn graphing capabilities


# ~~~~~~~  Definition of Functions   ~~~~~ ~~~~~~ ~~~~~~~ ~~~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~ ~ #
def graph(rolls):
    # determine the unique rolls values and their frequencies
    values, frequencies = np.unique(rolls, return_counts=True)

    # reverse the order of values for y-axis flipping -> highest value at the top
    values = np.flip(values)
    frequencies = np.flip(frequencies)

    # creating the initial bar plot; horizontal
    # bar plot's title, set style and graph the frequencies
    title = f'Rolling a Six-Sided Die {len(rolls):,} Rolls'  # comma specifier
    sns.set_style('whitegrid')  # style
    # set horizontal orientation; set order
    axes = sns.barplot(x=frequencies, y=values, order=values, orient='h', palette='bright')  # graph
    axes.set_title(title)  # set title to object axes
    axes.set(xlabel='Frequency', ylabel='Die Value')  # set labels
    # Make room for the text to the right of each bar (15% wider)
    axes.set_xlim(right=max(frequencies) * 1.15)

    # display text on the right of each bar
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_width()  # set x position
        text_y = bar.get_y() + bar.get_height()/2.0  # set y position
        text = f' {frequency:,}\n {frequency / len(rolls):.3%}'  # frequency and percentange
        axes.text(text_x, text_y, text, fontsize=8, ha='left', va='center')  # display text

    plt.show()
# end graph


# ~~~~~~~~  Program Execution   ~~~~~~~ ~~~~ ~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~~~~~~~ ~~~~~~~~ ~ #
# list of 360 sums of two random dice
rolls1 = [(random.randrange(1,7)+random.randrange(1,7)) for i in range(360)]

# list of 36000 sums of two random dice
rolls2 = [(random.randrange(1,7)+random.randrange(1,7)) for i in range(36000)]

# list of 36000000 sums of two random dice
rolls3 = [(random.randrange(1,7)+random.randrange(1,7)) for i in range(36000000)]

# print graphs
graph(rolls1)
graph(rolls2)
graph(rolls3)
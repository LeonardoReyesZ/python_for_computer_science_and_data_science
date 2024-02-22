import matplotlib.pyplot as plt # Matplotlib graphing capabilities
import seaborn as sns # seaborn graphing capabilities

# list of infections
infections = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301,
              1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# creating the initial bar plot with increased figure size and adjusted dodge
plt.figure(figsize=(14, 6)) # increase figure size

# bar plot's title, set style and graph the frequencies
title = "Number of infections per day" # comma specifier
sns.set_style('whitegrid') # style
axes = sns.barplot(x=list(range(1,len(infections) + 1)), y=infections, palette='bright') # graph
axes.set_title(title) # set title to the object axes
axes.set(xlabel='Day', ylabel='Infections')  # set labels
axes.set_ylim(top=max(infections)*1.10) # make room for the text above each bar -> 10% taller

# display text above each bar
for bar, infection in zip(axes.patches, infections):
    text_x = bar.get_x() + bar.get_width()/2 # set x position
    text_y = bar.get_height() # set y position
    text = f'{infection:,}\n{infection / sum(infections):.3%}' # infection and percentange
    axes.text(text_x, text_y, text, fontsize=6, ha='center', va='bottom') # display text

# display the graph
plt.show()
# ex_9.18: Anscombe's quarter csv
import pandas as pd
import matplotlib.pyplot as plt

# load data set into a pandas DataFrame
df = pd.read_csv('anscombe.csv')

# plotting each of the four datasets in Anscombe's Quartet
plt.figure(figsize=(12,8))

# define the dataset pairs
datasets = [('x1', 'y1'), ('x2', 'y2'), ('x3', 'y3'), ('x4', 'y4')]

for i, (x_col, y_col) in enumerate(datasets, start=1):
    plt.subplot(2, 2, i)
    plt.scatter(df[x_col], df[y_col])
    plt.title(f'Dataset {i}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xlim(2, 20) # adjust limits as needed
    plt.ylim(2, 14) # adjust limits as needed

plt.tight_layout()
plt.show()
# ex_9.17: working the Iris.csv dataset in pandas
import pandas as pd
import matplotlib.pyplot as plt

# load the dataset into pandas DataFrame
df = pd.read_csv('iris.csv', index_col=0)

print(df.head(), end="\n\n")
print(df.tail(), end="\n\n\n")

print(df.describe())

# create histograms for each numerical column
df.hist(figsize=(10,8), bins=30) # adjust bins as needed

# show the plots
plt.tight_layout() # adjust layout to prevent overlap
plt.show()
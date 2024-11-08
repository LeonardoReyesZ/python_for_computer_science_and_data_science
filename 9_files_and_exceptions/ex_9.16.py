# ex_9.16: working with the diamonds.csv Dataset in Pandas
import pandas as pd
import matplotlib.pyplot as plt

# load data set into a pandas DataFrame
df = pd.read_csv('diamonds.csv', index_col=0)

# display the first seven rows of the DataFrame
print(df.head(7), end="\n\n\n")

# display the last seven rows of the DataFrame
print(df.tail(7), end="\n\n\n")

# DataFrame method -> show statistics
print(df.describe(), end="\n\n\n")

# Series Method -> show statistics
print(df.describe(include='object'), end="\n\n\n")

# unique category values
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in '{column}':\n{unique_values}", end="\n\n")

# create histograms for each numerical column
df.hist(figsize=(10,8), bins=10) # adjust the number of bins as needed

# show the plots
plt.tight_layout() # adjust layout to prevent overlap
plt.show()
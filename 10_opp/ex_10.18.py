# ex_10.18
"""Time series."""

import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

la = pd.read_csv('ave_hi_la_jan_1895-2018.csv')

la.columns = ['Date', 'Temperature', 'Anomaly']
la.Date = la.Date.floordiv(100) # integer division on every element
pd.set_option('display.precision', 2)

print(la, end='\n\n')
print(la.describe())

linear_regression = stats.linregress(x=la.Date, y=la.Temperature)
print( linear_regression.slope )
print( linear_regression.intercept, end='\n\n' )
print( linear_regression.slope * 2019 + linear_regression.intercept )
print( linear_regression.slope * 1890 + linear_regression.intercept )


sns.set_style('darkgrid')
axes = sns.regplot(x=la.Date, y=la.Temperature)
axes.set_ylim(10, 70)

plt.show()
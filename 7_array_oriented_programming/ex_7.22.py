# ex_7.22: pandas series
import pandas as pd
import numpy as np
import random

serieA = pd.Series( [7, 11, 13, 17] )
print( f"serieA:\n{serieA}\n\n" )

serieB = pd.Series( 100, range(5) )
print( f"serieB:\n{serieB}\n\n" )

serieC = pd.Series( np.random.randint(0, 101, 20) )
print( f"serieC:\n{serieC}\n" )
print( f"serieC.describe():\n{serieC.describe()}\n\n" )

temperatures = pd.Series( [98.6, 98.9, 100.2, 97.9], index=['Julie','Charlie', 'Sam', 'Andrea'] )
print( f"Temperatures (SerieD):\n{temperatures}\n\n")

dict = {'Julie': 98.6, 'Charlie': 98.9, 'Sam': 100.2, 'Andrea': 97.9}
serieE = pd.Series( dict )
print( f"SerieE:\n{serieE}")
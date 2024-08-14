# ex_7.23: pandas dataFrames
import pandas as pd

temperatures_dic = {'Maxine': [30,35,38], 'James': [43,45,50], 'Amanda': [39,43,49]}

temperatures = pd.DataFrame( temperatures_dic )
print( f"temperatures:\n{temperatures}\n\n" )

temperatures_Index = pd.DataFrame( temperatures_dic, index=['Morning', 'Afternoon', 'Evening'] )
print( f"temperatures with custom indices\n{temperatures_Index}\n\n" )

print( f"Maxine's temperature:\n{temperatures_Index['Maxine']}\n\n" )

print( f"Morning temperature:\n{temperatures_Index.loc['Morning']}")

print( f"Morning and Evening temperatures:\n{temperatures_Index.loc[['Morning','Evening']]}\n\n")

print( f"temperatures of Amanda and Maxine\n{temperatures_Index[['Amanda','Maxine']]}\n\n")

print( f"temperatures of Amanda and Maxine in the morning and in the afternoon\n"
       f"{temperatures_Index.loc[['Morning','Afternoon'],['Amanda','Maxine']]}\n\n")

print( f"temperatures descriptive statistics\n{temperatures_Index.describe()}\n\n")

print( f"temperatures transpose\n{temperatures_Index.T}\n\n")

print( f"temperatures sorted\n{temperatures_Index.sort_index(axis=1)}")
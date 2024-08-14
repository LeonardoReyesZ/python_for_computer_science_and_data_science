# ex_7.21: shallow vs deep copy
import copy

dictionary = {'Sophia': [97,88]}

shallow_copy = dictionary.copy()
shallow_copy2 = copy.copy( dictionary )

dictionary['Sophia'] = [24,65,17]

print( "Shallow copy")
print( dictionary )
print( shallow_copy )
print( shallow_copy2, end="\n\n" )

dictionary = {'Sophia': [97,88]}
deep_copy = copy.deepcopy( dictionary )

dictionary['Sophia'] = [3454,45567,123,56]

print( "Deep copies" )
print( dictionary )
print( deep_copy )


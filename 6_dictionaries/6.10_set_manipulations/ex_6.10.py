""" script to create and compare sets"""
# ~~~~~~~~~  Definition of Functions  ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
def larger_set(set1, set2):
    if len(set1) > len(set2):
        print("Set1 has more elements than set2")
    elif len(set1) < len(set2):
        print("set2 has more elements than set1")
    else:
        print("set1 and set2 have the same number of elements")
# end larger_set

def set_equality(set1, set2):
    if set1 == set2:
        print("set1 is equal to set2")
    else:
        print("set1 is not equal to set2")
# end set_equality

def set_operations(set1, set2):
    print("Union: ", set1 | set2)
    print("Intersection: ", set1 & set2)
    print("Difference: ", set1 - set2)
    print("Symetric difference: ", set1 ^ set2)
# end set_operations

# ~~~~~~~~~  Program Execution     ~~ ~~~~ ~~~~~~ ~~~~~~~~~~~~ ~~~~~~~~~~ ~~~~ ~~~~~ ~~~~~~~~~~ ~ #
set1 = {'yellow', 'purple', 'red', 'black'}
set2 = {'black', 'white', 'blue'}

# test functions
larger_set(set1, set2)
set_equality(set1, set2)
set_operations(set1, set2)

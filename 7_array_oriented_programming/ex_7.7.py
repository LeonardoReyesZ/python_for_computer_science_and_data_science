# ex_7.7: Reimplement NumPy array output
def format_array( array ):
    # Find the maximum width of any element in the array
    max_width = max(len(str(element)) for row in array for element in row )

    # format each row and print it
    for row in array:
        formatted_row = "".join( f"{element:>{max_width+1}}" for element in row )
        print( formatted_row )
# end format_array


array = [ [1,20,30], [43,533,63], [700,84,9235] ]

format_array( array )
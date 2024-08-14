# ex_7.7: Reimplementing Numpy array Output
def format_dataframe(dataframe):
    # Find the maximum width for each column
    column_widths = []
    for col in range( len(dataframe[0]) ):
        max_width = max(len(str(dataframe[row][col])) for row in range(len(dataframe)))
        column_widths.append( max(max_width, len(str(col))) )  # Ensure column label fits

    # Print the column labels
    column_labels = "   " + " ".join(f"{col:>{column_widths[col]}}" for col in range(len(dataframe[0])))
    print(column_labels)

    # Print each row with row labels
    for row in range(len(dataframe)):
        formatted_row = f"{row:>2} " + " ".join(f"{dataframe[row][col]:>{column_widths[col]}}" for col in range(len(dataframe[0])))
        print(formatted_row)
# format_dataframe

# Example usage:
dataframe = [
    [1, 12, 123],
    [1234, 5, 67],
    [89, 10, 11]
]

format_dataframe(dataframe)

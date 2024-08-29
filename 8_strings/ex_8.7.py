# ex_8.7: converting integers into characters

# Print table header
print(f"{'Code':>5} {'Character':>10}")
print('-' * 18)

# Loop through the range 0 to 255
for i in range(256):
    try:
        # Display the code and corresponding character
        print(f"{i:>5} {i:>10c}")
    except ValueError:
        # Handle any characters that may not be displayable
        print(f"{i:>5} {'(undefined)':>10}")

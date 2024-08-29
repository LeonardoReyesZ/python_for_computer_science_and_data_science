# ex_8.8: converting integers into emojis

# start with the Unicode value for the smiley face emoji
start_emoji = 0x1F600

# Print table header
print(f"{'Code':>10} {'Emoji':>10}")
print('-' * 20)


# Loop through the next 10 Unicode code points
for i in range(10):
    code_point = start_emoji + i
    emoji = chr(code_point)
    print(f"{hex(code_point):>10}{emoji:>10}")
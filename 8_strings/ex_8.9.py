# ex_8.9: counting vowels in a sentence

# Read a phrase from the user
phrase = input("Enter a phrase: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize a counter
vowel_count = 0

# Count the vowels in the phrase
for char in phrase:
    if char in vowels:
        vowel_count += 1

# Output the number of vowels
print(f"Number of vowels: {vowel_count}")

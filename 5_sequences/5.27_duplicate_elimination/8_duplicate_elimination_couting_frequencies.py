import random
import numpy as np

# Function to generate a random user ID
def generate_user_id():
    letter = random.choice('abcdef')
    number = random.randint(1, 4)
    number2 = random.randint(1, 4)
    return f"{letter}{number}{number2}"

# Generate a list of 8000 random user IDs
user_ids = [generate_user_id() for _ in range(8000)]

# convert the list of user IDs to a numpy array
user_ids_array = np.array(user_ids)

# get the unique values and their frequencies
unique_user_ids, counts = np.unique(user_ids_array, return_counts=True)

# print unique values and their frequencies
for user_id, count in zip(unique_user_ids, counts):
    print(f"User ID: {user_id}, Frequency: {count}")

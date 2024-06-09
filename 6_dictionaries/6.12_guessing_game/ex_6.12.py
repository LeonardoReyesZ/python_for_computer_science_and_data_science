import random

# Define the characters and the actors in a dictionary
actors = {"Sean Bean": "Ned Stark", "Mark Addy":"Robert Baratheon", "Nikolaj Coster-Waldau": "Jaime Lannister",
          "Michelle Fairley":"Catelyn Stark", "Lena Headey": "Cersei Lannister"}

# shuffle the list of actors_characters to randomize the order of questions
items = list(actors.items()) # get a list to shuffle the items
random.shuffle(items) # shuffle the items
actors_shuffle = dict(items) # get back a dictionary

# initialize the variables
correct_guesses = 0

# ~~~~~   game loop   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
for actor, character in actors_shuffle.items():
    # ask the user for the actor's character
    user_input = input(f"\nwho played the character '{character}'? ")

    # check if the answer is correct
    if user_input.lower() == actor.lower():
        print("Correct!!!")
        correct_guesses += 1
    else:
        print(f"Wrong! the correct answer is {actor}")

    # check if the game is finish
    if correct_guesses == 5:
        print("Congratulations! You've linked all the actors to characters correctly.")
        break

# display the number of correct guesses
print(f"\nYou made {correct_guesses} correct guesses")

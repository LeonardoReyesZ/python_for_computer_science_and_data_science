# ex_8.23: Guess the correct synonym
import random

synonyms = {
    'happy': 'joyful',
    'sad': 'melancholy',
    'fast': 'quick',
    'smart': 'intelligent',
    'bright': 'luminous'
}

# ~~~~~~~~~~~~  Functions   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def select_random_pair( synonyms_dic ):
    """Select a random key-value pair from a synonyms dictionary."""
    hint, synonym = random.choice( list(synonyms_dic.items()) )
    return hint, synonym
# end select_random_pair

def display_guessed_word( synonym, guessed_letters ):
    """Displays the synonym with guessed letters revealed and unguessed letters as underscores"""
    display = ''.join( [letter if letter in guessed_letters else '_' for letter in synonym] )
    print( f"Current guess: {display}" )
# end display_guessed_word

def guess_synonym_game( hint, synonym ):
    """Game where user guesses letters and tries to find the synonym."""
    guessed_letters = set()
    attempts = len(synonym) + 3 # allow a few extra attempts beyond the word length

    print( f"Hint: {hint}" )

    while attempts > 0:
        print()
        display_guessed_word( synonym, guessed_letters )
        guess = input( "Guess a letter: ".lower() )

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print( "You already guessed that letter." )
        elif guess in synonym:
            guessed_letters.add( guess )
            print( "Good guess" )
        else:
            attempts -= 1
            print( f"Wrong guess! you have {attempts} attempts left." )

        # check if all letters have been guessed
        if all( letter in guessed_letters for letter in synonym ):
            print( f"All letters guessed!" )
            final_guess = input("Now, guess the synonym: ").lower()

            if final_guess == synonym:
                print("Congratulations! You guessed the correct synonym.")
            else:
                print(f"Sorry, that's incorrect. The correct synonym was '{synonym}'.")
            return

    print(f"You're out of attempts! The correct synonym was '{synonym}'.")
# end guess_synonym_game()

# ~~~~~~~~~~~~  Program Execution   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
hint, synonym = select_random_pair( synonyms )
guess_synonym_game( hint, synonym )
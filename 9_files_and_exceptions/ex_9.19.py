# ex_9.19: A crossword-puzzle generator
import random

# Example word list - you can replace this with a larger word source or dictionary
word_list = ["apple", "banana", "orange", "grape", "cherry", "pear", "plum",
    "kiwi", "peach", "melon", "berry", "lemon", "apricot", "lime", "fig"]

# Clue dictionary for the example word list
clue_dict = {
    "apple": "A popular red or green fruit often used in pies.",
    "banana": "A long, yellow fruit that monkeys love.",
    "orange": "A citrus fruit that is orange in color.",
    "grape": "A small, round fruit that grows in clusters, often used to make wine.",
    "cherry": "A small, red fruit often used in pies and desserts.",
    "pear": "A sweet, green or yellow fruit that is shaped like a bell.",
    "plum": "A small, round fruit with smooth skin and a pit.",
    "kiwi": "A small, fuzzy fruit with green flesh and black seeds.",
    "peach": "A juicy, orange fruit with a fuzzy skin.",
    "melon": "A large, juicy fruit that can be cantaloupe, watermelon, etc.",
    "berry": "A small, juicy fruit like a strawberry or blueberry.",
    "lemon": "A sour, yellow citrus fruit commonly used in drinks or cooking.",
    "apricot": "A small, orange fruit with a stone in the center.",
    "lime": "A small, green citrus fruit used to add tart flavor.",
    "fig": "A small, pear-shaped fruit that is often dried and eaten as a snack."
}

# constants for crossword generation
grid_size = 15 # Grid size (15x15)
black_square = "#" # symbol for black square
white_square = "." # symbol for white square
directions = ['across', 'down']# directions for placing words


def initialize_grid(size):
    """Initialize empty grid"""
    return [[white_square] * size for _ in range(size)]

def place_word_on_grid(grid, word, direction, row, col):
    """Randomly place words on the grid"""
    word_len = len(word)
    if direction == 'across':
        for i in range(word_len):
            grid[row][col+i] = word[i]
    elif direction == 'down':
        for i in range(word_len):
            grid[row+i][col] = word[i]
# end place_word_on_grid

def can_place_word(grid, word, direction, row, col):
    """Check if the word fits in the grid at the given position"""
    word_len = len(word)
    if direction == 'across':
        if col+word_len > grid_size: # word would overflow the grid
            return False
        for i in range(word_len):
            if grid[row][col+i] != white_square: # collision with another word
                return False
    elif direction == 'down':
        if row+word_len > grid_size: # word overflow the grid
            return False
        for i in range(word_len):
            if grid[row+i][col] != white_square: # collision with another word
                return False

    return True
# end can_place_word

def generate_crossword(grid, words):
    """Place words randomly in the grid"""
    for word in words:
        placed = False
        while not placed:
            direction = random.choice(directions)
            row = random.randint(0, grid_size-1)
            col = random.randint(0, grid_size-1)
            if can_place_word(grid, word, direction, row, col):
                place_word_on_grid(grid, word, direction, row, col)
                placed = True
# end generate_crossword


# generate a crossword puzzle
grid = initialize_grid(grid_size)
generate_crossword(grid, word_list)

# render the grid
for row in grid:
    print(" ". join(row))

# print clues
print("\n")
for i,clue in enumerate(clue_dict.values()):
    print(f"{f'{i}:':<4}{clue}")
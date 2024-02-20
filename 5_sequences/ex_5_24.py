"""   Program to simulate a card game  """

import random

# ==========  Definition of Functions   ============================================================================================
# function to print cards
def printDeck(deck, num_columns):
	for i, card in enumerate(deck):
		print('{0:<20}'.format(f"{card[0]} of {card[1]}"), end='')

		if (i+1) % num_columns == 0:
			print()  # Move to the next line for the next row
# end function printDeck()

# function to deal 5 cards
def dealCards(currentCard): # get the next card to deal
	if currentCard < 52: # if the deck is not empty
		return deck[currentCard:currentCard+5], currentCard+5 # deal 5 cards and increment the current card in the deck
	else:
		print('The deck is empty')
# end function dealCards

# function to determine if there is a pair in a hand of cards
def is_pair(hand):
	for i in range(len(hand)-1): # first card
		for j in range(i+1, len(hand)): # rest of the cards
			if hand[i][0] == hand[j][0]: # compare faces to find a pair
				return True # pair found
			
	return False # no pair found
# end function pair

# function to determine if there are two pairs in a hand of cards
def is_pairs(hand):
	counter = [0]*14 # create an array to counter the occurrences
	found = False # false by default

	for card in hand:
		current = face.index(card[0]) # get the current face of card
		counter[current] += 1 # increment the face counter

		if counter[current] == 2:
			if found:
				return True # second pair found -> finish
			else:
				found = True # first pair found -> continue

	return False # no pairs found
# end function is_pairs

# function to determine if there is three of a kind in the hand
def is_three(hand):
	counter = [0]*14 # create an array to counter the occurrences

	for card in hand:
		current = face.index(card[0]) # get the current face of card
		counter[current] += 1 # increment the face counter

		if counter[current] == 3:
			return True # three of a kind found

	return False # no three of a kind found
# end function is_three

# function to determine if there is a straight in the hand
def is_straight(hand):
	f = [False]*14 # create a bool array to tick the faces found in hand

	for card in hand:
		current = face.index(card[0]) # get the current face of card
		f[current] = True # tick the match faces

	for i in range(1, len(f)-len(hand)+1):
		if f[i] and f[i+1] and f[i+2] and f[i+3] and f[i+4]: # look for a straight
			return True # straight found

	return False # no straight found
# end function is_straight

# function to determine if there is a flush in the hand
def is_flush(hand):
	for i in range(len(hand)-1): # check the suits of each card
		if hand[i][1] != hand[i+1][1]:
			return False # different suit -> no flush found

	return True # flush found
# end function is_flush()

# function to determine if there is a full house in the hand
def is_fullHouse(hand):
	counter = [0]*14 # create an array to counter the occurrences
	pair = False  # false by default
	three = False  # false by default

	for card in hand:
		current = face.index(card[0]) # get the current face of card
		counter[current] += 1 # increment the face counter

	for count in counter:
		if count == 3:
			three = True # three of a kind found
		if count == 2:
			pair = True # a pair found

	if pair and three:
		return True # full house found

	else:
		return False # no full house found
# end function is_fullHouse

# function to determine if there is four of a kind in the hand
def is_four(hand):
	counter = [0]*14 # create an array to counter the occurrences

	for card in hand:
		current = face.index(card[0]) # get the current face of card
		counter[current] += 1 # increment the face counter

		if counter[current] == 4:
			return True # fout of a kind found

	return False # no four of a kind found
# end function is_four

# function to determine if there is a straight flush in the hand
def is_straightFlush(hand):
	if is_flush(hand) and is_straight(hand):
		return True # straight flush found

	return False # no straight flush found
# end function is_straightFlush()

# function to return the highest card in the hand
def highest(hand):
	hight = hand[0] # assuming that the first card is the highest card
	for card in hand:
		if face.index(card[0]) > face.index(hight[0]):
			hight = card

	return hight # return highest card
# end function highest

# function to determine who is the winner
def play(player1, player2):
	if is_straightFlush(player1):
		if not is_straightFlush(player2):
			return "Player 1 wins! straightFlush"
	elif is_straightFlush(player2):
		return "Player 2 wins! straightFlush"

	if is_four(player1):
		if not is_four(player2):
		 	return "Player 1 wins! four of a kind"
	elif is_four(player2):
		return "Player 2 wins!"

	if is_fullHouse(player1):
		if not is_fullHouse(player2):
			return "Player 1 wins! fullHouse"
	elif is_fullHouse(player2):
		return "Player 2 wins! fullHouse"

	if is_flush(player1):
		if not is_flush(player2):
			return "Player 1 wins! flush"
	elif is_flush(player2):
		return "Player 2 wins! flush"

	if is_straight(player1):
		if not is_straight(player2):
			return "Player 1 wins! straight"
	elif is_straight(player2):
		return "Player 2 wins! straight"

	if is_three(player1):
		if not is_three(player2):
			return "Player 1 wins! three of a kind"
	elif is_three(player2):
		return "Player 2 wins! three of a kind"

	if is_pairs(player1):
		if not is_pairs(player2):
			return "Player 1 wins! two pairs"
	elif is_pairs(player2):
		return "Player 2 wins! two pairs"

	if is_pair(player1):
		if not is_pair(player2):
			return "Player 1 wins! a pair"
	elif is_pair(player2):
		return "Player 2 wins! a pair"

	if face.index(highest(player1)[0]) > face.index(highest(player2)[0]):
		return "Player 1 wins! highest card"
	elif face.index(highest(player1)[0]) < face.index(highest(player2)[0]):
		return "Player 2 wins! highest card"

	return "Draw"
# end function play



# ==========  Program Execution   ===================================================================================================
currentCard = 0 # next card to deal 
num_columns = 4 # num of columns to print the deck

# Enumerating faces
face = [None, 'Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

deck = [
    ('Ace','Hearts'), ('Deuce','Hearts'), ('Three','Hearts'), ('Four','Hearts'), ('Five','Hearts'), ('Six','Hearts'), ('Seven','Hearts'),
    ('Eight','Hearts'), ('Nine','Hearts'), ('Ten','Hearts'), ('Jack','Hearts'), ('Queen','Hearts'), ('King','Hearts'),
    ('Ace','Diamonds'), ('Deuce','Diamonds'), ('Three','Diamonds'), ('Four','Diamonds'), ('Five','Diamonds'), ('Six','Diamonds'), ('Seven','Diamonds'),
    ('Eight','Diamonds'), ('Nine','Diamonds'), ('Ten','Diamonds'), ('Jack','Diamonds'), ('Queen','Diamonds'), ('King','Diamonds'),
    ('Ace','Clubs'), ('Deuce','Clubs'), ('Three','Clubs'), ('Four','Clubs'), ('Five','Clubs'), ('Six','Clubs'), ('Seven','Clubs'),
    ('Eight','Clubs'), ('Nine','Clubs'), ('Ten','Clubs'), ('Jack','Clubs'), ('Queen','Clubs'), ('King','Clubs'),
    ('Ace','Spades'), ('Deuce','Spades'), ('Three','Spades'), ('Four','Spades'), ('Five','Spades'), ('Six','Spades'), ('Seven','Spades'),
    ('Eight','Spades'), ('Nine','Spades'), ('Ten','Spades'), ('Jack','Spades'), ('Queen','Spades'), ('King','Spades')   
]

# convert the tuple to a list
deckList = list(deck)
# shuffle the list using random.shuffle
random.shuffle(deckList)
# convert the list back to a tuple if needed
deck = tuple(deckList)

#printDeck(deck, num_columns)


# deal cards to the players
player1, currentCard = dealCards(currentCard)
player2, currentCard = dealCards(currentCard)

print("\nPlayer's 1 hand:")
printDeck(player1, 5)

print("\nPlayer's 2 hand:")
printDeck(player2, 5)

# play the game and announce the winner
print(f"\n{play(player1, player2)}")

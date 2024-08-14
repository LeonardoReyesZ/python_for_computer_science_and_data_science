# ex_7.25: knight's tour -> brute force approaches
import random

# define chessboard size
SIZE = 8

# define all posible moves a knight can make
knight_moves = [ (2, 1), (1, 2), (-1, 2), (-2, 1),
    			 (-2, -1), (-1, -2), (1, -2), (2, -1) ]

def isValid(row, col, board):
	""" Cehck if the move is valid. """
	return (row>=0 and row<8 and col>=0 and col<8 and board[row][col] == -1)

def printBoard( board ):
	""" Print the chess board. """
	for row in board:
		for element in row:
			print( f"{element:>4}" , end='')
		print()

def knight_tour( rowStart, colStart ):
	""" Perform the knight's Tour using brute force. """
	# initialize the board with -1 to indicate unvisited square
	board = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]

	current_row = rowStart
	current_col = colStart
	counter = 2
	board[current_row][current_col] = 1  # starting point
	intents = 0

	while counter < 65:
		# make random moves
		newRow, newCol = knight_moves[ random.randrange(8) ]
		newRow += current_row
		newCol += current_col
		if isValid(newRow, newCol, board):
			# make move
			current_row = newRow
			current_col = newCol
			board[current_row][current_col] = counter
			counter += 1
		else:
			intents += 1

		if intents > 100:
			return counter-1, board
	# end of while

	return counter-1, board
# end knight_tour


def a(rowStart, colStart):
	"""try to solve the knight tour by brute force and print the final chess board"""
	counter, board = knight_tour(rowStart, colStart)
	if  counter == 64:
		print( "solution found!!!\n" )
		printBoard( board )
	else:
		print( f"No solution found, last move: {counter}\n")
		printBoard( board )
# end a

def b(rowStart, colStart):
	"""attempt 1,000,000 tours. Keep track of the results and show them"""
	results = []
	for i in range(1_000_000):
		results.append( knight_tour(rowStart, colStart)[0] )

	format = 0
	for result in results:
		print( f"{result:>4}", end='' )
		format += 1
		if format%10 == 0:
			print()
# end b

def c(rowStart, colStart):
	"""solve knight tour. Keep track of the results and show the results"""
	results = []
	temp = 0

	while temp != 64:
		temp = knight_tour(rowStart, colStart)[0]
		results.append( temp )
		print( f"{temp:<4}", end='')

	print( f"\n\nSolution found after {len(results)}\n" )
	format = 0
	for result in results:
		print( f"{result:>4}", end='' )
		format += 1
		if format%10 == 0:
			print()
# end c


# execute exercises
rowStart = 0
colStart = 0

# execute exercise a
#a(rowStart, colStart)

# execute exercise b
#b(rowStart, colStart)

# execute exercise c
c(rowStart, colStart)
# ex_7.24: introducing heuristic programming with the knight's tour
# define chessboard size
SIZE = 8

# define all posible moves a knight can make
knight_moves = [ (2, 1), (1, 2), (-1, 2), (-2, 1),
    			 (-2, -1), (-1, -2), (1, -2), (2, -1) ]

# accessibility board for heuristic approach
accessibility = [[2, 3, 4, 4, 4, 4, 3, 2],
				 [3, 4, 6, 6, 6, 6, 4, 3],
				 [4, 6, 8, 8, 8, 8, 6, 4],
				 [4, 6, 8, 8, 8, 8, 6, 4],
				 [4, 6, 8, 8, 8, 8, 6, 4],
				 [4, 6, 8, 8, 8, 8, 6, 4],
				 [3, 4, 6, 6, 6, 6, 4, 3],
				 [2, 3, 4, 4, 4, 4, 3, 2]]

def isValid(row, col, board):
	""" Cehck if the move is valid. """
	return (row>=0 and row<8 and col>=0 and col<8 and board[row][col] == -1)

def updateAccess(row, col, board):
	""" Update accessibility board values. """
	for move in knight_moves:
		newRow = row + move[0]
		newCol = col + move[1]
		if isValid( newRow, newCol, board ):
			accessibility[newRow][newCol] -= 1 # reduce accessibility value
# end updateAccess

def printBoard( board ):
	""" Print the chess board. """
	for row in board:
		for element in row:
			print( f"{element:>4}" , end='')
		print()

# end printBoard

def knight_tour( rowStart, colStart ):
	""" Perform the knight's Tour using the heuristic approach. """
	# initialize the board with -1 to indicate unvisited square
	board = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]

	current_row = rowStart
	current_col = colStart
	counter = 2
	board[current_row][current_col] = 1  # starting point
	updateAccess(current_row, current_col, board) # update accessibility board values

	while counter < 65:
		bestMove = (-1, -1)
		bestSquare = 10

		# look for the best move
		for move in knight_moves:
			newRow = current_row + move[0]
			newCol = current_col + move[1]
			if isValid(newRow, newCol, board):
				if accessibility[newRow][newCol] < bestSquare:
					bestSquare = accessibility[newRow][newCol]
					bestMove = move

		if bestMove == (-1, -1):
			print( "No solution found" )
			break  # nowhere to go

		# make move
		current_row += bestMove[0]
		current_col += bestMove[1]
		board[current_row][current_col] = counter
		counter += 1
		updateAccess(current_row, current_col, board)
	# end of while

	print(f"last move: {counter-1}", end="\n\n")
	printBoard( board )
# end knight_tour


# solve the knight's tour
rowStart = 3
colStart = 4
knight_tour(rowStart, colStart)
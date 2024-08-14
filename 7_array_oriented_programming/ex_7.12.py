# ex_7.12: Tic-Tac-Toe 3D | player against the computer
import numpy as np
import random

def check_winner( board, player ):
    # check rows and columns within each layer
    for layer in range(4):
        for index in range(4):
            if np.all( [board[layer, index, : ] == player] ) or np.all( [board[layer, : , index] == player] ):
                return True

        # check columns across layers
        for col in range(4):
            if np.all( board[ : , layer, col] == player ):
                return True

    # check rows and columns across layers
    for index in range(4):
        if np.all( [board[i, index, i] == player for i in range(4)] ):
            return True
        elif np.all( [board[3-i, index, i] == player for i in range(4)] ):
            return True
        elif np.all([board[i, i, index] == player for i in range(4)]):
            return True
        elif np.all([board[3-i, i, index] == player for i in range(4)]):
            return True

    # check diagonals within each layer
    for layer in range(4):
        if np.all( np.diag(board[layer]) == player ) or np.all( np.diag(np.fliplr(board[layer])) == player ):
            return True

    # check diagonals across layers (cube diagonals) | 4 diagonals in total
    if np.all( [board[i,i,i] == player for i in range(4)] ):
        return True
    elif np.all( [board[i,i,3-i] == player for i in range(4)] ):
        return True
    elif np.all( [board[i,3-i,i] == player for i in range(4)] ):
        return True
    elif np.all( [board[i,3-i,3-i] == player for i in range(4)] ):
        return True

    return False # no winner so far
# end check_winner

def check_draw( board ):
    return not np.any(board == ' ')
# end check_draw

def play_tic_tac_toe():
    board = np.full((4,4,4), ' ')
    current_player = 'O' if input("Do you want to start? ").strip().lower() != "yes" else 'X'

    while True:
        print( board )
        print( f"\nplayer {current_player}'s turn" )

        # get a valid move from the user
        if current_player == 'X':
            while True:
                try:
                    layer, row, col = map( int, input("Enter layer, row and a column (0-3): ").split() )
                    if board[layer,row,col] == ' ':
                        board[layer,row,col] = current_player
                        break
                    else:
                        print( "This square is alredy taken, try again" )
                except (ValueError, IndexError ):
                    print( "Invalid input, please enter two numbers between 0 and 3.")

        elif current_player == 'O':
            while True:
                layer = random.randint(0,3)
                row = random.randint(0,3)
                col = random.randint(0, 3)
                if board[layer,row,col] == ' ':
                    board[layer,row,col] = current_player
                    break

        # check for a winner
        if check_winner( board, current_player ):
            print( board )
            print( f"\nplayer {current_player} wins!!! ")
            break

        # check for a draw
        if check_draw( board ):
            print( board )
            print( "The game is a draw!")
            break

        # switch players
        current_player = 'O' if current_player=='X' else 'X'
# end play_tic_tac_toe


play_tic_tac_toe()
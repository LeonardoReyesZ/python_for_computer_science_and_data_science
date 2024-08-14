# ex_7.11: two-dimensional tic-tac-toe | player agains the computer
import numpy as np
import random

def check_winner( board, player ):
    # check the rows
    if any( np.all(board[row, : ] == player) for row in range(3) ):
        return True
    # check columns
    if any( np.all(board[ : , col] == player) for col in range(3) ):
        return True
    # check diagonals
    if np.all( np.diag(board) == player ):
        return True
    if np.all( np.diag(np.fliplr(board)) == player ):
        return True

    return False
# end check_winner

def check_draw( board ):
    return not np.any(board == ' ')
# end check_draw

def play_tic_tac_toe():
    board = np.full((3, 3), ' ')
    current_player = 'X'

    if (input("Do you want to start? ").strip().lower() != "yes"):
        current_player = 'O'


    while True:
        print( board )
        print( f"\nplayer {current_player}'s turn" )

        # get a valid move from the user
        if current_player == 'X':
            while True:
                try:
                    row, col = map( int, input("Enter row and a column (0,1,2): ").split() )
                    if board[row,col] == ' ':
                        board[row,col] = current_player
                        break
                    else:
                        print( "This square is alredy taken, try again" )
                except (ValueError, IndexError ):
                    print( "Invalid input, please enter two numbers between 0 and 2.")

        # computer's move
        else:
            while True:
                row = random.randint(0,2)
                col = random.randint(0, 2)
                if board[row,col] == ' ':
                    board[row,col] = current_player
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
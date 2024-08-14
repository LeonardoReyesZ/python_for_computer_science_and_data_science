# ex_7.10: two-dimensional tic-tac-toe
import numpy as np

def check_winner( board, player ):
    # check rows
    if any( np.all(board[row,:] == player) for row in range(3) ):
        return True;
    # check columns
    if any( np.all(board[:,col] == player) for col in range(3) ):
        return True;
    # check diagonals
    if np.all( np.diag(board) == player ):
        return True;
    if np.all( np.diag(np.fliplr(board)) == player ):
        return True

    return False
# end check_winner

def check_draw( board ):
    return not np.any( board==' ')
# end check_draw

def play_tic_tac_toe():
    board = np.full((3,3), ' ')
    current_player = 'X'

    while True:
        print( board )
        print( f"\nPlayer {current_player}'s turn")

        # get a valid move from the player
        while True:
            try:
                row, col = map(int, input( "Enter row and column (0,1,2): ").split() )
                if board[row, col] == ' ':
                    board[row, col] = current_player
                    break
                else:
                    print( 'This square is already taken. Try again.')
            except (ValueError, IndexError):
                print( 'Invalid input. Please enter two numbers between 0 and 2.')

        # check for a winner
        if check_winner( board, current_player ):
            print( board )
            print( f'\nPlayer {current_player} wins!')
            break

        # check for a draw
        if check_draw( board ):
            print( board )
            print( '\nThe game is a draw!')
            break

        # switch players
        current_player = 'O' if current_player == 'X' else 'X'
# end play_tic_tac_toe


play_tic_tac_toe()

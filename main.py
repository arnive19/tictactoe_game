# MODULES
# GLOBAL VARIABLES
game_still_on = True
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
winner = None
current_player = "X"

# display board
def display_board():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
# haha


# handle turn
def handle_turn(current_player):

    print("\n" + current_player + "'s turn\n")
    position = input("Enter number from 1-9:\n>>")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("\nInvalid index.Enter a number from 1-9:\n>>")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print("position already taken my opponent!")


    board[position] = current_player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    # print(winner + "is won the game")

def print_winner():
    if winner == "X" or winner == "O":
        print(winner + " won the game.")
    elif winner == None:
        print("It's a Tie. play again")

# check row
def check_row():
    global game_still_on
    row1_win = board[0] == board[1] == board[2] != "-"
    row2_win = board[3] == board[4] == board[5] != "-"
    row3_win = board[6] == board[7] == board[8] != "-"

    if row1_win or row2_win or row3_win:
        game_still_on = False

    if row1_win:
        return board[0]
    elif row2_win:
        return board[3]
    elif row3_win:
        return board[6]
    return

def check_column():
    global game_still_on
    col1_win = board[0] == board[3] == board[6] != "-"
    col2_win = board[1] == board[4] == board[7] != "-"
    col3_win = board[2] == board[5] == board[8] != "-"

    if col1_win or col2_win or col3_win:
        game_still_on = False

    if col1_win:
        return board[0]
    elif col2_win:
        return board[1]
    elif col3_win:
        return board[2]
    return


def check_diagonal():
    global game_still_on
    dia1_win = board[0] == board[4] == board[8] != "-"
    dia2_win = board[6] == board[4] == board[2] != "-"

    if dia1_win or dia2_win :
        game_still_on = False

    if dia1_win:
        return board[0]
    elif dia2_win:
        return board[6]

    return


# check column
# check diagonal


def check_if_tie():
    global game_still_on
    if '-' not in board:
        game_still_on = False
    return



def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# play game
def play_game():
    # display initial board
    display_board()
    while game_still_on:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    print_winner()

#-------------------------------------#
play_game()
#-------------------------------------#


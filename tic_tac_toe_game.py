"""TIK TAC TOE game program"""
# GAME BOARD
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

# if game is still going
game_still_going = True

#who won or tie
winner = None
# whose turn

current_player = "x"

# display board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# play game of tic tac toe
def play_game():

    # display initial board
    display_board()
    # while the game is still going
    while game_still_going:
        # handel a single turn of the arbetary player
        handle_turn(current_player)
        #  check if game is ended
        check_if_game_over()
        # flip to other player
        flip_player()

        # the game has ended
        if winner == "x" or winner == "o":
            print(winner + " won.")
        elif winner == None:
            print("tie.")

# handle the single turn of arbetary player
def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose your play position from 1-9: ")

    valid = False
    while not valid:
        
        while position not in ["1", "2", "3", "4", "5","6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:    
            print("You cannot go there. Go again.")

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    # setup global variable
    global winner

    # check rows
    row_winner = check_row()
    # check column
    column_winner = check_column()
    # check diagonal
    diagonal_winner = check_diagonal()

    # get the winner
    if row_winner:
        winner = row_winner
    elif diagonal_winner:
        winner = diagonal_winner
    elif column_winner:
        winner = column_winner
    else:
        # there was no winner
        winner = None    

    return

def check_row():
    # set up global variable
    global game_still_going
    # check if any of the row have all same value land is not empty
    row_1 = board[0] == board[1] ==board[2] != "-"
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"

    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner[x or o]       
    if row_1:
        return board[0] 
    elif row_2:
        return board[1]
    elif row_3:
        return board[2]    
    return

def check_column():
        # set up global variable
    global game_still_going
    # check if any of the column have all same value land is not empty
    column_1 = board[0] == board[3] ==board[6] != "-"
    column_2 = board[1] == board[4] ==board[7] != "-"
    column_3 = board[2] == board[5] ==board[8] != "-"
    # if any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner[x or o]
    if column_1:
        return board[0] 
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

    

def check_diagonal():
        # set up global variable
    global game_still_going
    # checl if any of the diagonal have all same value land is not empty
    diagonal_1 = board[0] == board[4] ==board[8] != "-"
    diagonal_2 = board[6] == board[4] ==board[2] != "-"
    
    # if any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner[x or o]
    if diagonal_1:
        return board[0] 
    elif diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # global variables we need
    global current_player
    # if the current player is "x" then it changes into "o" and vice versa
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return 


play_game()


import numpy as np
def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
print(board)
game_over = False

while not game_over:
    # ask for Player 1 input
    if turn == 0:
        selection = int(input("Player 1 make your selection (0-6)): ")
        print(selection)

    # Ask for Player 2 input






















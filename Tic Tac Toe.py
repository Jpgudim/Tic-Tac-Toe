# This is my first attempt at making tic-tac-toe in python entirely from scratch
# I'm not exactly sure how to do it, so i'm going to figure it out as I go

board = []
for x in range(0,3):
    board.append(["[ ]"] * 3)

print ()
print ("Welcom to Tic Tac Toe! Here is the game board, with numbers representing each sqaure")
print ()

def get_board(board):
    print ()
    for row in board:
        print (" ".join(row))
    print ()
    
get_board(board)
print ()
print ("Player 1, you are X's and player 2, you are O's")

for turn in range(9):
    turn + 1
    print ("Player " + str((turn % 2) + 1) + ", your turn!")
    row_select = int(input("Select Row: "))
    col_select = int(input("Select Col: "))

    if board[row_select][col_select] == "[X]":
        print ("That spot has already been taken!")
    else:
        if (turn % 2) == 0:
            board[row_select - 1][col_select - 1] = "[X]"
            get_board(board)
        else:
            board[row_select - 1][col_select - 1] = "[O]"
            get_board(board)

    








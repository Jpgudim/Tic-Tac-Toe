# This is my first attempt at making tic-tac-toe in python entirely from scratch
# I'm not exactly sure how to do it, so i'm going to figure it out as I go

board = []
for x in range(0,3):
    board.append(["[ ]"] * 3)

print ()
print ("Welcome to Tic Tac Toe! Here is the game board, with numbers representing each sqaure")
print ()

def get_board(board):
    print ()
    for row in board:
        print (" ".join(row))
    print ()
    
print ("Player 1, you are X's and player 2, you are O's")

for turn in range(9):
    turn + 1
    print ("Player " + str((turn % 2) + 1) + ", your turn!")
    get_board(board)
    row_select = int(input("Select Row: "))
    col_select = int(input("Select Col: "))

    if  row_select not in range(4) or col_select not in range(4):
        print()
        print ("That's not on the board! Try again player " + str((turn % 2) + 1))
        get_board(board)
        row_select = int(input("Select Row: "))
        col_select = int(input("Select Col: "))
        if (turn % 2) == 0:
            board[row_select - 1][col_select - 1] = "[X]"
            get_board(board)
        else:
            board[row_select - 1][col_select - 1] = "[O]"
            get_board(board)
    elif board[row_select - 1][col_select - 1] == "[X]" or board[row_select - 1][col_select - 1] == "[O]":
        print ()
        print ("That spot has already been taken!")
        print ()
        print ("Player " + str((turn % 2) + 1) + ", go again!")
        get_board(board)
        row_select = int(input("Select Row: "))
        col_select = int(input("Select Col: "))
        if (turn % 2) == 0:
            board[row_select - 1][col_select - 1] = "[X]"
            get_board(board)
        else:
            board[row_select - 1][col_select - 1] = "[O]"
            get_board(board)
        get_board(board)    
    else:
        if (turn % 2) == 0:
            board[row_select - 1][col_select - 1] = "[X]"
            get_board(board)
        else:
            board[row_select - 1][col_select - 1] = "[O]"
            get_board(board)

    
#scenarios I need to work on:
#1. input is not an int
#       simple if statement, just need to figure out where to put it
#2. player wins the game (3 x's or 3 o's in a line)
#       maybe something like " if board[row] or board[col] = 3 of same letters"
#       this doesnt account for diagonal line though
#3. no longer possible for a player to win the game
#       no idea how I will do this

#potential issues with code:
#1. not finished
#2. not sure yet how im going to finish it
#3. lot of repeating if/else scenarios. I feel like it could be optimized and cleaned







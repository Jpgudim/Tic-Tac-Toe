# This is my first attempt at making tic-tac-toe in python entirely from scratch
# I'm not exactly sure how to do it, so i'm going to figure it out as I go

#To do list:
# scenarios when it's impossible for a player to win


board = []
for x in range(0,3):
    board.append(["[ ]"] * 3)

print ()
print ("Welcome to Tic Tac Toe! Here is the game board, with numbers representing each square")
print ()

#function to display the board
def get_board(board):
    print ()
    for row in board:
        print (" ".join(row))
    print ()
#function when a player wins the game
def win_game(player):
    print ("Player %s, you win!" % player)
    print ()
#function to get user input for row selection
def get_row():
    row_select = input("Select Row: ")
    if row_select in "0123456789":
        row_select = int(row_select)
    while type(row_select) != int:
        row_select = input("That's not a number! Select Row Again: ")
        if row_select in "0123456789":
            row_select = int(row_select)
    return row_select
#function to get user input for column selection
def get_col():
    col_select = input("Select Column: ")
    if col_select in "0123456789":
        col_select = int(col_select)
    while type(col_select) != int:
        col_select = input("That's not a number! Select Column Again: ")
        if col_select in "0123456789":
            col_select = int(col_select)
    return col_select

print ("Player 1, you are X's and player 2, you are O's")
#start game loop
for turn in range(9):
    turn + 1
    print ("Player " + str((turn % 2) + 1) + ", your turn!")
    get_board(board)
#winning scenarios
    if board[0] == ['[X]', '[X]', '[X]'] or board[1] == ['[X]', '[X]', '[X]'] or board[2] == ['[X]', '[X]', '[X]']:
        win_game(1)
        break
    elif board[0] == ['[O]', '[O]', '[O]'] or board[1] == ['[O]', '[O]', '[O]'] or board[2] == ['[O]', '[O]', '[O]']:
        win_game(2)
        break
    elif board[0][0] == "[X]" and board[1][0] == "[X]" and board[2][0] == "[X]":
        win_game(1)
        break
    elif board[0][1] == "[X]" and board[1][1] == "[X]" and board[2][1] == "[X]":
        win_game(1)
        break
    elif board[0][2] == "[X]" and board[1][2] == "[X]" and board[2][2] == "[X]":
        win_game(1)
        break
    elif board[0][0] == "[O]" and board[1][0] == "[O]" and board[2][0] == "[O]":
        win_game(2)
        break
    elif board[0][1] == "[O]" and board[1][1] == "[O]" and board[2][1] == "[O]":
        win_game(2)
        break
    elif board[0][2] == "[O]" and board[1][2] == "[O]" and board[2][2] == "[O]":
        win_game(2)
        break
    elif board[0][0] == "[X]" and board[1][1] == "[X]" and board[2][2] == "[X]":
        win_game(1)
        break
    elif board[0][2] == "[X]" and board[1][1] == "[X]" and board[2][0] == "[X]":
        win_game(1)
        break
    elif board[0][0] == "[O]" and board[1][1] == "[O]" and board[2][2] == "[O]":
        win_game(2)
        break
    elif board[0][2] == "[O]" and board[1][1] == "[O]" and board[2][0] == "[O]":
        win_game(2)
        break
    else:
        row_select = get_row()
        col_select = get_col()
        while row_select not in range(4) or col_select not in range(4):
            print()
            print ("That's not on the board! Try again player " + str((turn % 2) + 1))
            get_board(board)
            row_select = get_row()
            col_select = get_col()
        while board[row_select - 1][col_select - 1] == "[X]" or board[row_select - 1][col_select - 1] == "[O]":
            print ()
            print ("That spot has already been taken!")
            print ()
            print ("Player " + str((turn % 2) + 1) + ", go again!")
            get_board(board)
            row_select = get_row()
            col_select = get_col()
        if (turn % 2) == 0:
            board[row_select - 1][col_select - 1] = "[X]"
        else:
            board[row_select - 1][col_select - 1] = "[O]"







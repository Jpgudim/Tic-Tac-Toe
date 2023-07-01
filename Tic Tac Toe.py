# This is my first attempt at making tic-tac-toe in python entirely from scratch
# I'm not exactly sure how to do it, so i'm going to figure it out as I go

#To do list:
# scenarios when it's impossible for a player to win
# input is not an integer

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
    
print ("Player 1, you are X's and player 2, you are O's")

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
        row_select = int(input("Select Row: "))
        col_select = int(input("Select Col: "))
        if  row_select > 3 or col_select > 3:
            
            print()
            print ("That's not on the board! Try again player " + str((turn % 2) + 1))
            get_board(board)
            row_select = int(input("Select Row: "))
            col_select = int(input("Select Col: "))
            if (turn % 2) == 0:
                board[row_select - 1][col_select - 1] = "[X]"
                #board
            else:
                board[row_select - 1][col_select - 1] = "[O]"
                #board
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
                #board
            else:
                board[row_select - 1][col_select - 1] = "[O]"
                #board

            #board   

        else:
            if (turn % 2) == 0:
                board[row_select - 1][col_select - 1] = "[X]"
                #board
            else:
                board[row_select - 1][col_select - 1] = "[O]"
                #board







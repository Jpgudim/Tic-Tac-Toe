# This is my first attempt at making tic-tac-toe in python entirely from scratch
# I'm not exactly sure how to do it, so i'm going to figure it out as I go

row_1 = ["|   |   |   |"]
row_2 = ["|   |   |   |"]
row_3 = ["|   |   |   |"]

print ()
print ("Welcom to Tic Tac Toe! Here is the game board, with numbers representing each sqaure")
print ()
print ("_____________")
print ("| 1 | 2 | 3 |")
print ("-------------")
print ("| 4 | 5 | 6 |")
print ("-------------")
print ("| 7 | 8 | 9 |")
print ("-------------")
print ()

def get_board():
    print ()
    print (row_1)
    print (row_2)
    print (row_3)
    print ()
    

print ("Player 1, you are X's and player 2, you are O's")
turn_1 = input ("Player 1, you're up! Which square do you choose? ")
if turn_1 == "1":
    row_1 = ["| X |   |   |"]
elif turn_1 == "2":
    row_1 = ["|   | X |   |"]
elif turn_1 == "3":
    row_1 = ["|   |   | X |"]
elif turn_1 == "4":
    row_2 = ["| X |   |   |"]
elif turn_1 == "5":
    row_2 = ["|   | X |   |"]
elif turn_1 == "6":
    row_2 = ["|   |   | X |"]
elif turn_1 == "7":
    row_3 = ["| X |   |   |"]
elif turn_1 == "8":
    row_3 = ["|   | X |   |"]
elif turn_1 == "9":
    row_3 = ["|   |   | X |"]

get_board()


# placeholder for how I will prevent over riding previous selections
if turn_2 == turn_1:
    print ("That spot has already been taken! Try again.")


from random import randint

board_size= int(raw_input("Size Of Board:"))
ship_amount= int(raw_input("Number of Ships:"))
turn_wanted= int(raw_input("Number of Turns:"))

##Initializing variables
#board_size= 20
#ship_amount= 2
#turn_wanted= 5


##create lists for game objects
board = []
ships = []

##generate board
for x in range(board_size):
    board.append(["O"] * board_size)

##print game board nicely
def print_board(board):
    for row in board:
        print " ".join(row)

##get random row cord
def random_row(board):
    return randint(0, len(board) - 1)

##get random col cord
def random_col(board):
    return randint(0, len(board[0]) - 1)

##generate and place ships 
def generate_ships(ship_amount):
    
    for x in range(ship_amount):
        
        ship_row = random_row(board)
        ship_col = random_col(board)
        
        ships.append([ship_row, ship_col])

    print ships

##check guess agains ship list
def check_guess(ships, row_guess, col_guess):

    for x in range(len(ships)):
        if ships[x] == [row_guess, col_guess]:
            ships.pop(x)
            print ships
            return True
       
        else:
            return false
        
##Run game
def run_game():
    print "Let's play Battleship!"
    generate_ships(ship_amount)
    print_board(board)

    ships_sunk = 0
    
    ##Turn loop
    for turn in range(turn_wanted):
        print "turn", turn + 1
        ## Get guesses
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
        
        if check_guess(ships, guess_row, guess_col):
            ships_sunk = ships_sunk + 1
            print ships_sunk
            print "Congratulations! You sunk a battleship!"
            if  ships_sunk == ship_amount:
                print "Congratulations! All enemy ships destroyed!"
                break
        else:
            if (guess_row < 0 or guess_row > board_size - 1) or (guess_col < 0 or guess_col > board_size - 1):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                
            if turn == turn_wanted:
                print "Game Over"
                break
                print_board(board)


run_game()

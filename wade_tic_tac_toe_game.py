"CSE210 W02 Prove: Developer - Solo Code Submission"
" Wade Harris"

def main():
    print()

game_board = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_"]

player_1 = "x"
player_2 = "o"
game_in_progress = True

def display_board(game_board):
    print(game_board [0] + " | " + game_board [1] + " | " + game_board [2] )
    print(game_board [3] + " | " + game_board [4] + " | " + game_board [5] )
    print(game_board [6] + " | " + game_board [7] + " | " + game_board [8] )
#display_board(game_board)

def player_move(game_board):
    player_input = int(input("Player 1 please choose your slot between 1-9"))
    if player_input >= 1 and player_input <= 9 and game_board [player_input -1] == "_":
        game_board [player_input -1] = player_1
    else:
        print("That slot has already been taken, try again")

def player_move_2(game_board):
    player_2_input = int(input("Player 2 please choose your slot between 1-9"))
    if player_2_input >= 1 and player_2_input <= 9 and game_board [player_2_input -1] == "_":
        game_board [player_2_input -1] = player_2
    else:
        print("That slot has already been taken, try again")

while game_in_progress:
    display_board(game_board)
    player_move(game_board)
    display_board(game_board)
    player_move_2(game_board)

main()
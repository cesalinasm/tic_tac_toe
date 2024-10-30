from settings_and_rules import dict_board, update_board, check_who_wins
import random
from player_settings import Player

X_0 = ["X", "0"]
player_1 = Player(1)
player_2 = Player(2)

player_1.mark = random.choice(X_0)

if player_1.mark == "X":
    player_2.mark = "0"
    player_1_start = True

else:
    player_2.mark = "X"
    player_1_start = False

print(f'Player who gets "X" will start the game. Each player will choose a number from the board to put its own mark'
      f' and whoever first completes three marks in a row (horizontal, vertical or diagonal) is the winner.\n\n'
      f"{player_1.number} plays as {player_1.mark}.\n{player_2.number} plays as {player_2.mark}.\n")
update_board(dict_board)

i = 0
game_continue = True
while game_continue:
    if player_1_start:
        while True:
            try:
                chosen_number = int(input(f"{player_1.number}, please choose a number: "))
            except ValueError:
                print("Only numbers from 1 to 9 are allowed.")
            else:
                if chosen_number == 0 or chosen_number > 10:
                    print("Wrong number, it should be between 1-9.")
                elif chosen_number == dict_board[f"{chosen_number}"]:
                    dict_board[f"{chosen_number}"] = player_1.mark
                    update_board(dict_board)
                    break
                else:
                    print("Number taken. Try again!")
        i += 1
        player_1_start = False

        if check_who_wins(dict_board):
            print(f"{player_1.number} wins!")
            game_continue = False

    else:
        while True:
            try:
                chosen_number = int(input(f"{player_2.number}, please choose a number: "))
            except ValueError:
                print("Only numbers from 1 to 9 are allowed.")
            else:
                if chosen_number == 0 or chosen_number > 10:
                    print("Wrong number, it should be between 1-9.")
                elif chosen_number == dict_board[f"{chosen_number}"]:
                    dict_board[f"{chosen_number}"] = player_2.mark
                    update_board(dict_board)
                    break
                else:
                    print("Number taken. Try again!")
        i += 1
        player_1_start = True

        if check_who_wins(dict_board):
            print(f"{player_2.number} wins!")
            game_continue = False

    if i == 9 and not check_who_wins(dict_board):
        print("Tie!")
        game_continue = False

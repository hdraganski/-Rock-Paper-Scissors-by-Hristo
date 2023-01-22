from random import randint as random

count_wins = 0
count_loses = 0
count_draws = 0
options_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("Please select one of the options or type \"Exit\" to end the game:\n1. Rock\n2. Paper\n3. Scissors\n")

while True:
    command = input()

    if command == "Exit":
        break

    try:
        player_move = int(command)
        print(f"Your choice: {options_dict[player_move]}")
    except:
        print("Invalid input!")
        print("Please select one of the options or type \"Exit\" to end the game:\n1. Rock\n2. Paper\n3. Scissors\n")
        continue

    pc_move = random(1, 3)
    print(f"Computer's choice: {options_dict[pc_move]}")
    if player_move == pc_move:
        print("It's a draw!")
        count_draws += 1

    elif (player_move == 1 and pc_move == 3) or \
            (player_move == 2 and pc_move == 1) or \
            (player_move == 3 and pc_move == 2):
        print("You win!")
        count_wins += 1
    else:
        print("You lose!")
        count_loses += 1

print(f"Game is over! Your scores: \nWins: {count_wins}\nLoses: {count_loses}\nDraws: {count_draws}")

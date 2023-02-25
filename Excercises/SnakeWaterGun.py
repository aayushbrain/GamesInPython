import random

game_item = ['Snake','Water','Gun']

random_item = random.choice(game_item)

print("choose one item")

com_score = 0
user_score = 0
game_loop = 0
game_chance = 10

while game_loop < 10:
    user_item = input("S for Snake, W for Water and G for Gun : ").upper()
    game_loop += 1
    game_chance -= 1
    if random_item == "Snake" and user_item == "W":
        com_score += 1
        print("Computer item Snake and User item Water. So computer won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Water" and user_item == "G":
        com_score += 1
        print("Computer item Water and User item Gun. So computer won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Gun" and user_item == "S":
        com_score += 1
        print("Computer item Gun and User item Snake. So computer won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Snake" and user_item == "G":
        user_score += 1
        print("Computer item Snake and User item Gun. So user won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Water" and user_item == "S":
        user_score += 1
        print("Computer item Water and User item Snake. So user won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Gun" and user_item == "W":
        user_score += 1
        print("Computer item Gun and User item Water. So user won the game.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Snake" and user_item == "S":
        print("Computer item Snake and User item Snake. So game draw.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Water" and user_item == "W":
        print("Computer item Water and User item Water. So game draw.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    elif random_item == "Gun" and user_item == "G":
        print("Computer item Gun and User item Gun. So game draw.")
        print(f"Game Score : Computer score {com_score} , User score {user_score}\n")
        print(f"Game chance remaining {game_chance}\n")
    else:
        print("Please enter valid input\n")
        print(f"Game chance remaining {game_chance}\n")

if com_score > user_score:
    print("Computer won the game")
elif com_score < user_score:
    print("User won the game")
else:
    print("Game draw")

print(f"Final Game Score : Computer {com_score} , User {user_score}")


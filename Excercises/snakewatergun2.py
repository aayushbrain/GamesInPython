import random

def game():
    swg = ["S", "W", "G"]
    a = 0  # human point
    b = 0  # comp point
    i = 10

    while i>5:
        print(f"You can play {i-5} more times ")
        i-=1
        choice=input("Enter your choice:\n"
                     "Press \"s\" for Snake\n"
                     "Press \"w\" for Water\n"
                     "Press \"g\" for Gun\n")
        choice=choice.capitalize()
        rand = (random.choice(swg))
        print(rand)
        if choice=="G":
            if rand=="G":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Draw")
            elif rand=="W":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Computer Won")
                b += 1
                print(f"computer won {b} times")
            else:
                print(f"Your choice is {choice} and computer's choice is {rand}")
                a += 1
                print("You won !!!")
                print(f"You won {a} times")
        elif choice=="S":
            if rand=="S":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Draw")
            elif rand=="G":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Computer Won")
                b += 1
                print(f"computer won {b} times")
            else:
                print(f"Your choice is {choice} and computer's choice is {rand}")
                a += 1
                print("You won !!!")
                print(f"You won {a} times")
        elif choice=="W":
            if rand=="W":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Draw")
            elif rand=="S":
                print(f"Your choice is {choice} and computer's choice is {rand}")
                print("Computer Won")
                b += 1
                print(f"computer won {b} times")
            else:
                print(f"Your choice is {choice} and computer's choice is {rand}")
                a += 1
                print("You won !!!")
                print(f"You won {a} times")
        else:
            print("Wrong input given\nPlease enter s,w or g")
            i+=1
    if a>b:
        print(f"You won the match!!!"
              f"You won by {a-b} points")
    elif a==b:
        print("Tie!!!")
    else:
        print(f"Computer won to match !!!"
              f"Computer won by {b-a} points")
    again=input("Wanna play again? y/n\n")
    game() if again=="y" else exit()

print("***This is Snake Water Gun Game***")
game()


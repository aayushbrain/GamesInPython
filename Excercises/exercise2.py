# Guess the number
import sys

n=18
number_of_guesses=1
print("Number of guesses is limited to 9 times: ")
while (number_of_guesses <=9):
     guess_number = int(input("Guess the number:\n"))

     if guess_number<18:
          print("you entered less number please input greater number.\n")
     elif guess_number>=18:
          print("you entered greater number please input smaller nuber.\n")
     else:
          print("you won.\n")
          print(number_of_guesses,"no. of guesses he took to finish.\n")
          break


     print(9-number_of_guesses,"no. of guesses he took to finish.")
     number_of_guesses = number_of_guesses + 1



if (number_of_guesses>9):
    print("Game Over")


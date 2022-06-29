# A guessing game where the computer has a secret number and a user is trying to guess the number
# In this program, we will make use of the while loop (a flow control statement)
# We shall also make use of "if" statement (a decision-making statement)
# We shall import the random module (A Python built-in module to generate random numbers)
# Finally, we shall define a function that takes in two parameters
import random as rand

def guess_game(Low, High):
    Random_Number = rand.randint(Low, High)
    User_Guess = 0
    while User_Guess != Random_Number:
        User_Guess = int(input(f"Guess a number between {Low} and {High}: "))
        print(f"Your guessed number is {User_Guess}")
        if User_Guess < Random_Number:
            print(f"Sorry, try again, your guessed number({User_Guess}) is low")
        elif User_Guess > Random_Number:
            print(f"Sorry, try again, your guessed number({User_Guess}) is high")
        else:
            print("Hurray! You've guessed the number right")
guess_game(1, 10)




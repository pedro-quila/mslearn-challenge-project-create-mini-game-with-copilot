

# create a rock paper scissors game using python with GitHub Copilot
import random

# create a list of possible choices
choices = ["rock", "paper", "scissors"]

# create a score and rounds played
score = 0
rounds = 0

# create a while loop to keep the game running
while True:
    # get the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")
    # get the computer's choice
    computer_choice = random.choice(choices)
    # print the computer's choice
    print(f"The computer chose: {computer_choice}")
    # check who won
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        score += 1
    else:
        print("You lose!")
    # increment the rounds played
    rounds += 1
    # print the score and rounds played
    print(f"Score: {score}, Rounds: {rounds}")
    # ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break

print("Thanks for playing!")


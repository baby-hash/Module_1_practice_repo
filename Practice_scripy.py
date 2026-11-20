# this is a game of rock paper scissors
import random

'''
The player has three choices to choose from,
 rock, paper or scissors. 
 The computer will also randomly choose one of the three options. 
 The player will have 5 attempts to play the game. 
 The player can also exit the game at any time by typing 'exit'. 
 The player can also choose to play again after each round. 
 The player and computer scores will be displayed after each round.
 '''

choices = ["rock", "paper", "scissors"]
attempts=0
max_attempts = 5
player_score = 0
computer_score = 0

#A while loop to keep the game running until the player has used all their attempts or chooses to exit.
while attempts< max_attempts:

    player_choice = input("What do you choose? Type 'rock', 'paper' or 'scissors': ") 

#if loop to check if the player wants to exit the game

    if player_choice == "exit":
        print("Thanks for playing!")
        break   
#if loop to check if the player wants to play again after each round

    keep_playing = input("Do you want to play again? (yes/no): ").strip().lower()
    if keep_playing != "yes":
        print("Thanks for playing!")
        break

#if loop to check if the player has entered a valid choice

    if player_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        continue
    attempts+=1

#if loop to check if the player has used all their attempts

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print("It's a tie!")



    elif (player_choice == "rock" and computer_choice == "scissors") or \
        (player_choice == "paper" and computer_choice == "rock") or \
        (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")

#the player score is incremented by 1 and printed
        player_score += 1
        print('Player wins:', player_score)
    else:
        print("You lose!")

#computer score is incremented by 1 and printed 

        computer_score +=1
        print('Computer wins:', computer_score)


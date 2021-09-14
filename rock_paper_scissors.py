import random

options = ['rock', "paper", "scissors"]
player_options = {"r": 'rock', "p":"paper", "s":"scissors"}
comp_choice = random.choice(options)
print("\nThe computer has selected an option.\n")
player_choice = input("Will you play rock, paper, or scissors? (Type r for rock, p for paper, or s for scissors)? ")
print("The computer picked:",comp_choice)
print("You picked:", player_options[player_choice])
if player_options[player_choice] == comp_choice:
    print("It's a tie!\n")
elif (player_options[player_choice] == 'rock' and comp_choice == 'scissors') or (player_options[player_choice] == 'scissors' and comp_choice == 'paper') or (player_options[player_choice] == 'paper' and comp_choice == 'rock'):
    print("You win!\n")
else: 
    print('You lose!\n')
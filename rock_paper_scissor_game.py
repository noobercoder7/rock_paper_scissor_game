import random
import os

rock = '''
    _______
---'   ____)
      (_____)
      (ROCK_)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
        PAPER ___)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       SCISSOR___)
      (____)
---.__(___)
'''


other_exit = ["Good Job!!!", "Excellent Work!!!", "Awesome!!!", "Chal be!!!!"]
game_choices = [rock, paper, scissors]

com_wins = 0
user_wins = 0

continue_game = True
while continue_game:

    user_action = int(
        input("Enter a choice :\n0 for rock.\n1 for paper.\n2 for Scissor.\n"))

    if user_action > 2 or user_action < 0:
        print("invalid Input! Try again!")
        exit()

    computer_action = random.randint(0, 2)

    print(f"You chose:\n{game_choices[user_action]}")
    print(f"\nComputer Chose:\n{game_choices[computer_action]}\n")

    if user_action == computer_action:
        print("It's a tie!!")

    elif user_action == 0:
        if computer_action == 2:
            print("You win!")
            user_wins += 1
        else:
            print("You lose.")
            com_wins += 1
    elif user_action == 1:
        if computer_action == 0:
            print("You win!")
            user_wins += 1
        else:
            print("You lose.")
            com_wins += 1

    elif user_action == 2:
        if computer_action == 1:
            print("You win!")
            user_wins += 1
        else:
            print("You lose.")
            com_wins += 1

    print(f"\nSCORE: \n Player: {user_wins} \n Computer: {com_wins}")

    try_again = input("\nPlay again (y/n)?")

    if try_again == 'y':
        os.system('cls')
    elif try_again == 'n':
        continue_game = False
    else:
        print(random.choice(other_exit))
        exit()

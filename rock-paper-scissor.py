import random


def winner_game():
<<<<<<< HEAD
    choices = ["rock", "paper", "scissors"]
=======
    choices = ["Rock", "Paper", "Scissors"]
>>>>>>> cb9386e3357f91d1ca53ac1a12bf0a6afa13d344
    while True:
        computer_choice = random.choice(choices)

        player_choice = input("Enter your choice (Rock, Paper, Scissors), or type 'I quit' to exit: ")

        if player_choice.lower() == "i quit":
            print("Thank you for playing!")
            break

        if player_choice not in choices:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        print(f"Player: {player_choice}")
        print(f"Computer: {computer_choice}")

<<<<<<< HEAD
        if player_choice.lower() == computer_choice.lower():
            print("Game Tied")
        elif (
            (player_choice.lower() == "rock" and computer_choice.lower() == "paper")
            or (player_choice.lower() == "scissors" and computer_choice.lower() == "rock")
            or (player_choice.lower() == "paper" and computer_choice.lower() == "scissors")
=======
        if player_choice == computer_choice:
            print("Game Tied")
        elif (
            (player_choice == "Rock" and computer_choice == "Paper")
            or (player_choice == "Scissors" and computer_choice == "Rock")
            or (player_choice == "Paper" and computer_choice == "Scissors")
>>>>>>> cb9386e3357f91d1ca53ac1a12bf0a6afa13d344
        ):
            print("You Lose")
        else:
            print("You Win")

        print()
<<<<<<< HEAD
print (winner_game())
=======
print (winner_game())













>>>>>>> cb9386e3357f91d1ca53ac1a12bf0a6afa13d344

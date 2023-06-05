import random


def winner_game():
    choices = ["rock", "paper", "scissors"]

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

        if player_choice.lower() == computer_choice.lower():
            print("Game Tied")
        elif (
            (player_choice.lower() == "rock" and computer_choice.lower() == "paper")
            or (player_choice.lower() == "scissors" and computer_choice.lower() == "rock")
            or (player_choice.lower() == "paper" and computer_choice.lower() == "scissors")
        ):
            print("You Lose")
        else:
            print("You Win")

        print()

print (winner_game())














>>>>>>> cb9386e3357f91d1ca53ac1a12bf0a6afa13d344

import random


def winner_game():
    choices = ["Rock", "Paper", "Scissors"]
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

        if player_choice == computer_choice:
            print("Game Tied")
        elif (
            (player_choice == "Rock" and computer_choice == "Paper")
            or (player_choice == "Scissors" and computer_choice == "Rock")
            or (player_choice == "Paper" and computer_choice == "Scissors")
        ):
            print("You Lose")
        else:
            print("You Win")

        print()
print (winner_game())














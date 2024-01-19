import random
print("Hello, let's play a game!")
def play_game():
    choices = ["rock", "paper", "scissors"]
    score = 0
    round = 0

    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ")

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            round += 1
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("Computer wins!")
                round += 1
            else:
                print("You win!")
                score += 1
                round += 1
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("Computer wins!")
                round += 1
            else:
                print("You win!")
                score += 1
                round += 1
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("Computer wins!")
                round += 1
            else:
                print("You win!")
                score += 1
                round += 1
        else:
            print("Invalid choice. Please try again.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print(f"Your final score is: {score}. You played {round} rounds.")

play_game()

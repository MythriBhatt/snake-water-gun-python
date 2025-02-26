'''
-1: Snake
1: water
0: gun
'''
import random

# Define choices
choices = {"s": -1, "w": 1, "g": 0}
reverse_choices = {-1: "Snake", 1: "Water", 0: "Gun"}

# Initialize scores
user_wins = 0
computer_wins = 0
draws = 0
rounds = 0

print("Welcome to the Snake, Water, Gun Game!")
print("Rules: Snake beats Water, Water beats Gun, Gun beats Snake.\n")

while True:
    # User input
    you = input("Enter your choice (s for Snake, w for Water, g for Gun) or 'q' to quit: ").lower()

    # Check if user wants to quit
    if you == 'q':
        print("\nFinal Scoreboard:")
        print(f"Total Rounds Played: {rounds}")
        print(f"You Won: {user_wins} times")
        print(f"Computer Won: {computer_wins} times")
        print(f"Draws: {draws}")
        print("\nGame Over! Thanks for playing!")
        if user_wins > computer_wins:
            print("You are the Overall Winner!")
        elif user_wins < computer_wins:
            print("Computer is the Winner! Better luck next time.")
        else:
            print("It's a Tie!")
        break

    # Validate input
    if you not in choices:
        print("Invalid choice! Please enter 's', 'w', 'g', or 'q' to quit.\n")
        continue

    # Get user and computer choices
    your_choice = choices[you]
    computer = random.choice([-1, 1, 0])

    # Display choices
    print(f"\nYour choice: {reverse_choices[your_choice]}")
    print(f"Computer's choice: {reverse_choices[computer]}")

    # Determine winner
    if computer == your_choice:
        print("It's a Draw!\n")
        draws += 1
    elif (computer == -1 and your_choice == 1) or \
         (computer == 1 and your_choice == 0) or \
         (computer == 0 and your_choice == -1):
        print("Computer Won this round!\n")
        computer_wins += 1
    else:
        print("You Won this round!\n")
        user_wins += 1

    rounds += 1

    # Display Scoreboard
    print("Scoreboard:")
    print(f"You: {user_wins} | Computer: {computer_wins} | Draws: {draws}\n")

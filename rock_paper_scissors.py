import random
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")




import random

possible_actions = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
ties=0

for round_num in range(1, 3):
    print(f"Round {round_num}:")
    user_action = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_action not in possible_actions:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        user_action = input("Enter your choice (rock, paper, scissors): ").lower()

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        ties += 1
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "paper" and computer_action == "rock") or \
         (user_action == "scissors" and computer_action == "paper"):
        print(f"{user_action.capitalize()} beats {computer_action}. You win this round!")
        user_score += 3
    else:
        print(f"{computer_action.capitalize()} beats {user_action}. You lose this round.")
        computer_score += 1

print("\nGame over!")
print(f"Your final score: {user_score}")
print(f"Computer's final score: {computer_score}")
print(f"Number of ties: {ties}")



import random

print("Welcome to Rock Paper Scissors Game!")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:

    user = input("\nEnter rock, paper or scissors (or quit): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Please enter a valid choice.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You win!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

print("\nGame Over!")
print("Final Score:")
print("You:", user_score)
print("Computer:", computer_score)
import random

print("Rock.....")
print("Paper.....")
print("Scissors.....")

player = input("Player 1, make your move: ")
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays: {computer}")
if player == computer:
    print("It's a tie")
elif player == "rock":
    if computer == "scissors":
        print("Player wins")
    elif computer == "paper":
        print("computer wins")
elif player == "paper":
    if computer == "scissors":
        print("Computer wins")
    elif computer == "rock":
        print("Player1 wins")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins")
    elif computer == "paper":
        print("Player1 wins")
else:
    print("Something went wrong")

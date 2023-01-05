from random import randint

print("Rock.....")
print("Paper.....")
print("Scissors.....")

player = input("Player 1, make your move: ").lower()
rand_num = randint(0, 2)
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
    else:
        print("computer wins")
elif player == "paper":
    if computer == "scissors":
        print("Computer wins")
    else:
        print("Player1 wins")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins")
    else:
        print("Player1 wins")
else:
    print("Something went wrong")

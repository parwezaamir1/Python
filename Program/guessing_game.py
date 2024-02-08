# guessing game
import random

jackpot = random.randint(1, 11)

guess = int(input("Chal guess kr number between 1 to 11: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")

    guess = int(input("Chal guess kr: "))
    counter += 1

else:
    print("Sahi jawab")
print("You took", counter, "attempts")
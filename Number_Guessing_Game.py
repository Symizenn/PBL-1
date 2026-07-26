import random
num=random.randint (1, 100)
print("Number Guessing Game")
print("Guess a number between 1 and 99:")
while True:
    guess = int(input("Enter your guess: "))
    if guess<num:
        print("Too Low, Try Again.")
    elif guess>num:
        print("Too High, Try Again.")
    else:
        print("You guessed the correct number", "You are the GOAT.")
        break

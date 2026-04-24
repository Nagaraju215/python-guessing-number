import random

secret_number = random.randint(1, 10)

guess_limit = 3
guess_count = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")
print(f"You have {guess_limit} chances")

while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess == secret_number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

else:
    print(f"❌ You lost! The correct number was {secret_number}")
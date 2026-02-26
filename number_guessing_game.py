import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 4
guessed = False

while attempts < max_attempts:
    user_guess = int(input("Enter your guess 1-100: "))
    attempts += 1
    if user_guess == secret_number:
        print("Hooray! You have guessed the number")
        guessed = True
        break
    elif user_guess < secret_number:
        print("Too low")
    else:
        print("Too High")
if not guessed:
    print("Game over! the number was", secret_number)            
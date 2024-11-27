# #number guessing game

import random

maximum_guesses = 10


while True:
    secret_number = random.randint(1,10)
    guess_count = 0

    print("\nA new round has started! You have 10 guesses")

    while guess_count <= maximum_guesses:
        guess = int(input("Guess the number (1-10): "))

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10")
            continue

        guess_count += 1
        guesses_left = maximum_guesses - guess_count

        if guess > secret_number:
            print(f"Too high! You have {guesses_left} guesses left")

        elif guess < secret_number:
            print(f"Too low! You have {guesses_left} guesses left")

        else:
            print(f"Correct! The secret number was {secret_number}")
            break

    else:
        print(f"Game over. No more guesses left. The secret number was {secret_number}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break

# rock paper scissors

import random

valid_actions = ["rock", "paper", "scissors"]

def best_of_five():
    while True:
        user_score = 0
        computer_score = 0

        print("\nBest of Five Mode: First to 3 wins!")

        while user_score < 3 and computer_score < 3:
            user_action = input("\nPlease enter your move (R / P / S): ").lower()
            if user_action == "r":
                user_action = "rock"
            elif user_action == "p":
                user_action = "paper"
            elif user_action == "s":
                user_action = "scissors"
            else:
                print("\nInvalid action!")
                continue

            computer_action = random.choice(valid_actions)

            print(f"\nYou chose {user_action}, computer chose {computer_action}\n")

            if user_action == computer_action:
                print(f"\nBoth players selected {user_action}. It's a tie!")

            elif user_action == "rock":
                if computer_action == "scissors":
                    print("\nRock smashes Scissors! You win!")
                    user_score += 1
                else:
                    print("\nPaper covers rock! You lose.")
                    computer_score += 1

            elif user_action == "paper":
                if computer_action == "rock":
                    print("\nPaper covers rock! You win!")
                    user_score += 1
                else:
                    print("\nScissors cuts paper! You lose.")
                    computer_score += 1

            elif user_action == "scissors":
                if computer_action == "paper":
                    print("\nScissors cuts paper! You win!")
                    user_score += 1
                else:
                    print("\nRock smashes scissors! You lose.")
                    computer_score += 1
        
            print(f"\nYour score: {user_score}")
            print(f"\nComputer score: {computer_score}")

        if user_score == 3:
            print("\nYou won Best of Five!")
        else:
            print("\nYou lost Best of Five...")
    
        play_again = input("\nDo you want to play again? (Y / N): ").lower()
    
        if play_again != "y":
            print("\nThanks for playing! Goodbye!")
            break

def best_of_three():
    while True:
        user_score = 0
        computer_score = 0

        print("\nBest of Three Mode: First to 2 wins!")

        while user_score < 2 and computer_score < 2:
            user_action = input("\nPlease enter your move (R / P / S): ").lower()
            if user_action == "r":
                user_action = "rock"
            elif user_action == "p":
                user_action = "paper"
            elif user_action == "s":
                user_action = "scissors"
            else:
                print("\nInvalid action!")
                continue

            computer_action = random.choice(valid_actions)

            print(f"\nYou chose {user_action}, computer chose {computer_action}\n")

            if user_action == computer_action:
                print(f"\nBoth players selected {user_action}. It's a tie!")

            elif user_action == "rock":
                if computer_action == "scissors":
                    print("\nRock smashes Scissors! You win!")
                    user_score += 1
                else:
                    print("\nPaper covers rock! You lose.")
                    computer_score += 1

            elif user_action == "paper":
                if computer_action == "rock":
                    print("\nPaper covers rock! You win!")
                    user_score += 1
                else:
                    print("\nScissors cuts paper! You lose.")
                    computer_score += 1

            elif user_action == "scissors":
                if computer_action == "paper":
                    print("\nScissors cuts paper! You win!")
                    user_score += 1
                else:
                    print("\nRock smashes scissors! You lose.")
                    computer_score += 1
        
            print(f"\nYour score: {user_score}")
            print(f"\nComputer score: {computer_score}")

        if user_score == 2:
            print("\nYou won Best of Three!")
        else:
            print("\nYou lost Best of Three...")
    
        play_again = input("\nDo you want to play again? (Y / N): ").lower()
    
        if play_again != "y":
            print("\nThanks for playing! Goodbye!")
            break

def round_by_round():
    while True:
        print("\nA new round has started")

        user_action = input("\nPlease enter your move (R / P / S): ").lower()
        if user_action == "r":
            user_action = "rock"
        elif user_action == "p":
            user_action = "paper"
        elif user_action == "s":
            user_action = "scissors"

        computer_action = random.choice(valid_actions)

        print(f"\n You chose {user_action}, computer chose {computer_action}\n")

        if user_action == computer_action:
            print(f"\nBoth players selected {user_action}. It's a tie!")

        elif user_action == "rock":
            if computer_action == "scissors":
                print("\nRock smashes Scissors! You win!")
            else:
                print("\nPaper covers rock! You lose.")

        elif user_action == "paper":
            if computer_action == "rock":
                print("\nPaper covers rock! You win!")
            else:
                print("\nScissors cuts paper! You lose.")

        elif user_action == "scissors":
            if computer_action == "paper":
                print("\nScissors cuts paper! You win!")
            else:
                print("\nRock smashes scissors! You lose.")

        play_again = input("\nDo you want to play again? (Y / N): ").lower()
    
        if play_again != "y":
            print("\nThanks for playing! Goodbye!")
            break

def game_mode_selection():
    print("\nHow would you like to play?")

    game_mode_input = input("\nR - round by round, 3 - best of three, 5 - best of five: ").lower()
    if game_mode_input == "r":
        round_by_round()
    elif game_mode_input == "3":
        best_of_three()
    elif game_mode_input == "5":
        best_of_five()

def main():
    print("""
        Welcome to Rock, Paper, Scissors! 
          
        Rules:
          - Rock smashes Scissors
          - Scissors cuts Paper
          - Paper covers Rock

          Use keys to input your moves against the computer or to exit game

          R - rock, P - paper, S - scissors

        """)
    
    start_or_exit_input = input("\nWhat would you like to do? (S - start / E - exit:) ").lower()

    if start_or_exit_input == "s":
        game_mode_selection()
    else:
        print("\nExiting game...")
    
if __name__ == "__main__":
    main()
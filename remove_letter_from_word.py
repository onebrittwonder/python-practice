
invalid_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

def contains_invalid_symbols(input_word: str):
    return any(symbol in input_word for symbol in invalid_symbols)

def remove_letter(word: str, letter: str):
    if letter in word:
        word = word.replace(letter, '', 1)
    return word

def input_has_number(input_word: str):
    return any(char.isdigit() for char in input_word)

def character_limit_exceeded(input_word: str):
    if len(input_word)> 25:
        return True

if __name__ == "__main__":

    while True:
        user_input = input("Please type in a word: ")

        if not user_input:
            print(f"Input is empty. Try again.") 
        elif character_limit_exceeded(user_input):
            print(f"{user_input} is not valid as it exceeds the 25 character limit")
        elif input_has_number(user_input):
            print(f"{user_input} is not valid as it contains a number")
        elif contains_invalid_symbols(user_input):
            print(f"{user_input} is not valid as it contains invalid symbols")
        else:
            break

    score = 0
    initial_length = len(user_input)
    print(f"There are {initial_length} letters to remove")
    print(f"Initial score: {score}")

    while user_input:

        removed_letter = input("Please type the letter you want to remove: ")

        new_word = remove_letter(user_input, removed_letter)

        if new_word != user_input:
            user_input = new_word
            letters_left = len(user_input)
            score += 1
            if user_input:
                print(f"The word is now {user_input}")
                print(f"There are {letters_left} letters left to remove")
                print(f"Current score: {score}")
        else:
            if score > 0:
                score -= 1
                print(f"The letter {removed_letter} is not in the word")
                print(f"Current score: {score}")
                
    print("You have successfully removed each letter from the word!")
    print(f"Your final score is {score}")


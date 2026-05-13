from words import rand_word, split_word


def user_guesses():
    is_guess = False
    while not is_guess:
        user_inp = input("\nGuess a letter (a-z):  ").lower()
        if len(user_inp) > 1: 
            print("\nPlease guess only one letter!\n")
        elif not user_inp.isalpha():
            print("\nNumbers & Chars are not supported..\n")
        else:
            return user_inp


def menu():
    print("<  Welcome to the Hangman game, Good luck!  >\n")
    print("1. Animals\n" \
            "2. Countries\n" \
            "3. Food\n" \
            "4. Sports\n" \
            "5. Technology\n"\
            "6. Exit\n")

    valid_choice = False
    while not valid_choice:
        category = input("- Please type the name of the category you want to play.\n" \
                                    "- Press Enter for a random game.\n" \
                                    "- Type exit to close the game.\n"\
                                    "\nYour choice:  ").lower()
        if category == "exit":
            exit("Goodbye, see you later :)")
        elif category not in ["animals", "countries", "food", "sports", "technology", ""]:
            print("Invalid choice... select only from menu!")
        else:
            valid_choice = True
    return category

def game():
    category_play = menu()
    category, word  = rand_word(category_play)
    display = split_word(word)
    choices = len(word) + 5
    letters_used = []

    print(f"The selected category is: {category}\n")
    print(f"You have - {choices} - attempts to win\n")

    while choices > 0 and "".join(display) != word:
        print(f"The secret word is: {" ".join(display)}\nLetters used: [ {' | '.join(letters_used)} ]\n")
        user_guess = user_guesses()

        if user_guess in letters_used:
            print("\nThe letter you selected is already used.. Guess again")
            continue

        letters_used.append(user_guess)
        correct_guess = False

        for index, letter in enumerate(word):
            if letter  == user_guess:
                display[index] = letter
                correct_guess = True

        if correct_guess:
            if "".join(display) != word:
                print(f"\nGood job! The letter [{user_guess}] is in the secret word")
        else:
            choices -= 1
            print(f"\nWrong guess.. Attempts left: {choices}")
            
    if "".join(display) == word:
        print(f"\nWell done, you won! The secret word is: '{word}'")
    elif choices == 0:
        print(f"\nYou're out of attempts. The secret word was: '{word}'")

game()
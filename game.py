from game_boot import rand_word, split_word, LOGO, M
from words import CATEGORY_MAP


def user_guesses():
    is_guess = False
    while not is_guess:
        user_inp = input(f"\n{M}Guess a letter (a-z):  ").lower()
        if len(user_inp) > 1: 
            print(f"\n{M}Please guess only one letter!\n")
        elif not user_inp.isascii() or not user_inp.isalpha():
            print(f"\n{M}Numbers & Chars are not supported..\n")
        else:
            return user_inp


def menu():
    print(f"{LOGO}\n")
    print(f"{M}1. Animals\n"
      f"{M}2. Countries\n"
      f"{M}3. Food\n"
      f"{M}4. Sports\n"
      f"{M}5. Technology\n"
      f"{M}6. Exit\n")

    valid_choice = False
    while not valid_choice:
        category = input(f"{M}- Please type the category you want to play.\n" \
                                    f"{M}- Press Enter for a random game.\n" \
                                    f"{M}- Type exit to close the game.\n"\
                                    f"\n{M}Your choice:  ").lower()
        if category in ["exit", "6"]:
            exit(f"{M}Goodbye, see you later :)")
        elif category in CATEGORY_MAP:
            category = CATEGORY_MAP[category]
            valid_choice = True
        elif category in ["animals", "countries", "food", "sports", "technology", ""]:
            valid_choice = True
        else:
            print(f"{M}Invalid choice... select only from menu!")

    return category

def game():
    category_play = menu()
    category, word  = rand_word(category_play)
    display = split_word(word)
    choices = len(word) + 4
    letters_used = []

    print(f"{M}The selected category is >> {category}\n")
    print(f"{M}You have - {choices} - attempts to win\n")

    while choices > 0 and "".join(display) != word:
        print(f"{M}The secret word is >> {" ".join(display)}\n" \
                f"{M}Letters used >> [ {' / '.join(letters_used)} ]\n")
        user_guess = user_guesses()

        if user_guess in letters_used:
            print(f"\n{M}The letter you selected is already used.. Guess again")
            continue

        correct_guess = False
        for index, letter in enumerate(word):
            if letter  == user_guess:
                display[index] = letter
                correct_guess = True

        if correct_guess:
            if "".join(display) != word:
                print(f"\n{M}Good job! The letter '{user_guess}' is in the secret word")
        else:
            letters_used.append(user_guess)
            choices -= 1
            print(f"\n{M}Wrong guess.. Attempts left >> {choices}")
            
    if "".join(display) == word:
        print(f"\n{M}Well done, you won! The secret word is >> '{word}'")
    elif choices == 0:
        print(f"\n{M}You're out of attempts. The secret word was >> '{word}'")


def play_game():
    game_on = True
    while game_on:
        game()
        end_game = False
        while not end_game:
            keep_planing = input(f"{M}\nDo you want to play again? (Y/N):  ").lower()
            if keep_planing == "y":
                end_game = True
            elif keep_planing == "n":
                game_on = False
                end_game = True
            else:
                print(f"{M}Invalid choice.. please type Y or N")


play_game()
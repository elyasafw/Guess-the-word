from random import choice
from words import words


def rand_word(category):
    secret_word = choice(words[category])
    return secret_word


def split_word(secret_word):
    display_word = ["-" for _ in range(len(secret_word))]
    return display_word


def menu():
    print("< Welcome to the Hangman game >\n")
    print("1. Animals\n" \
    "2. Countries\n" \
    "3. Food\n" \
    "4. Sports\n" \
    "5. Technology\n")

    valid_choice = False
    while not valid_choice:
        category = input("Please select category for play:  ").lower()
        if category not in ["animals", "countries", "food", "sports", "technology"]:
            print("Invalid choice... select only from menu!")
        else:
            valid_choice = True

    return category
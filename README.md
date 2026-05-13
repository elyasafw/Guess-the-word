# Hangman Game

A terminal-based Hangman game written in Python.

## Features

- 5 word categories: Animals, Countries, Food, Sports, Technology
- Select a category by name or number
- Press Enter to get a random category
- Tracks used letters and remaining attempts
- Play again option after each game

## Project Structure

```
├── game.py        # Main game logic and menu
├── game_boot.py   # Helper functions, logo, and styling
├── words.py       # Word lists and category map
```

## How to Run

```bash
python game.py
```

## How to Play

1. Choose a category from the menu (type the name or number)
2. Guess one letter at a time
3. You have `word length + 4` attempts to guess the word
4. The game reveals correctly guessed letters in the word
5. Win by guessing all letters before running out of attempts

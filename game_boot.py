from random import choice
from words import WORDS_DATA


LOGO = r"""
 __    __              _                             _                                          
/ / /\ \ \___  _ __ __| |   __ _ _   _  ___  ___ ___(_)_ __   __ _    __ _  __ _ _ __ ___   ___ 
\ \/  \/ / _ \| '__/ _` |  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \
 \  /\  / (_) | | | (_| | | (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
  \/  \/ \___/|_|  \__,_|  \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                           |___/                             |___/   |___/                      
"""


MARGIN = 15
M = f"{'':<{MARGIN}}"


def rand_word(category):
    if category == "":
        category = choice(list(WORDS_DATA.keys()))
    secret_word = choice(WORDS_DATA[category])
    return category, secret_word


def split_word(secret_word):
    display_word = ["_" for _ in range(len(secret_word))]
    return display_word
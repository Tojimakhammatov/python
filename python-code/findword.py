
"""
1/9/2023

Find words
"""

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word or "ь" in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # letters in words
    word_letters = set(word)
    # Users choise
    user_letters = ''
    print(f"I thought it was a {len(word)}-digit number. Can you find it? ")

    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"the letters you have entered until now : {user_letters}")

        letter = input("Enter your letter : >> ").upper()
        if letter in user_letters:
            print("You have entered this letter before. Enter another letter.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} letter is true.")
        else:
            print("There is no such letter.")
        user_letters += letter
    print(f"Congratulations !!! Letter is {word} You found it in {len(user_letters)} tries. ")

play()
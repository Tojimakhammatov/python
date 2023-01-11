"""
Find number

"""

import random

def findnumber(x=10):
    rand_number = random.randint(1,x)
    
    print(f"I thought of a number between 1 and {x}, can you find it?")
    guesses = 0
    while True:
        guesses += 1
        guess = int(input(">>> "))
        if guess < rand_number:
            print("incorrect. The number I thought is bigger than that. Try again : ")
        elif guess > rand_number:
            print("incorrect. The number I thought is smaller than that. Try again : ")
        else:
            break
    print(f"Congratulations. You found it with {guesses} guesses!!!")
    return guess 


def findmy_number(x=10):
    print(f"Think of a number from 1 to {x} and press any button. I will try to find it.")
    border_bottom = 1
    border_high = 10
    guesses = 0
    while True:
        guesses += 1
        if border_bottom != border_high:
            guess = random.randint(border_bottom, border_high)
        else:
            guess = border_bottom
        answer = input(f"You thought number {guess} : True (t), I thought bigger (+), or smaller (-)".lower())
        if answer == "-":
            border_high = guess - 1
        elif answer == "+":
            border_bottom = guess + 1
        else:
            break
    print(f"Excellent! I found it with {guesses} guess")
    return guesses


def play(x=10):
    any = True
    while True:
        your_guesses = findnumber(x)
        my_guesses = findmy_number(x)
        if your_guesses > my_guesses:
            print("I am winner!")
        elif your_guesses < my_guesses:
            print("You are win!")
        else: print("Equality..")
        any = input("Do you want any? Yes(+) / No(-)")

play()
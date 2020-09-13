#!/usr/bin/env python3
import random

number = random.randint(1, 20)
attempts = 0
win = False

name = input("Please enter a username?")
print("Welcome " + name + "." )

question = input("Would you like to play a game? [Y/N] ")
if question.lower() == "n":
    print("oh..okay")
    exit()
if question.lower() == "y":
    print("Guess a number between 1 and 20")
while not win:
    guess = int(input("Take a guess: "))
    attempts = attempts + 1
    if guess == number:
        win = True
    elif guess < number:
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")

print("You guessed correctly! {}".format(number))
print("It only took you {} guesses".format(attempts))
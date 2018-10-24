#modules to be used
import time
import random

#start the game
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")

#wait for 1 second
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

# loads the word list and gets a random word
word_list = open("words.txt").read().splitlines()
word = random.choice(word_list)

# set word to lowercase to ensure that guesses are not case sensitive
word = word.lower()

# variables for checking
guesses = ''
turns = 10

# poll input and check against word to guess`
while turns > 0:
    letters_remaining = 0

    # print current state of guesses
    for char in word:

        if char in guesses:
            print(char, end=' ')

        else:
            print("_", end=' ')
            letters_remaining += 1

# break condition for while loop. User succeeds when all letters are guessed
    if letters_remaining == 0:
        print("You won")
        break

    print()

    # ask the user go guess a character, set to lowercase to ensure that guess is not case sensitive
    guess = input("guess a character:").lower()
    guesses += guess

# check to see if guess is contained in word
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Lose! Word was ",word)

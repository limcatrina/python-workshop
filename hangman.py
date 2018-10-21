#importing the time module
import time

# import random module to get random choice
import random

#welcoming the user
name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

print("")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

# loads the word list from local folder
word_list = open("words.txt").read().splitlines()

# get random word from word word_list
word = random.choice(word_list)

# set word to lowercase to ensure that guesses are not case sensitive
word = word.lower()

#creates a variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:

    # initialize counter to keep track of letters remaining
    letters_remaining = 0

    # for every character in secret_word
    for char in word:

    # see if the character is in the players guess
        if char in guesses:

        # print then out the character
            print(char, end=' ')

        else:

        # if not found, print a dash
            print("_", end=' ')

        # and increase the failed counter with one
            letters_remaining += 1

    # if number of letters remaining is zero, means the word has been solved
    # print You Won
    if letters_remaining == 0:
        print("You won")

    # exit the script
        break

    print()

    # ask the user go guess a character, set to lowercase to ensure that guess is not case sensitive
    guess = input("guess a character:").lower()

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

    # print wrong
        print("Wrong")

    # how many turns are left
        print("You have", + turns, 'more guesses')

    # if the turns are equal to zero
        if turns == 0:

        # print "You Lose"
            print("You Lose! Word was ",word)

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    value = random.randint(min, max)

    #Guess the number
    guess = input("Guess the number")
    if guess == value:
        print("Congratulations, you got it right!")
    else:
        print("Wrong :(")
    print("Actual value", value)
    roll_again = input("Roll the dice again?")

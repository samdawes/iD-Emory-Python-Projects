#created by Sam Dawes
#Random number guessing game with HINTS and SCORE

#Random numbers
import random

#The number to be guessed (range 0-20)
number = random.randint(0, 20)

#Bool: will change to True if number is guessed
is_guessed = False

#Score: set to 0 at beginning and incremented
score = 0

#Main Loop
#Increment score and provide hints
while (is_guessed == False):

    score = score + 1

    guess = int(input("Guess the number: "))

    if (guess == number):
        is_guessed = True
    elif (guess > number):
        print ("Lower!")
    else :
        print ("Higher!")

print ("Congrats! You guessed the number in " + str(score) + " guesses!")

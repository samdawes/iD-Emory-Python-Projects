#created by Sam Dawes
#Simple Number guessing game with RANDOM number

#Python library for pseudorandom numbers
import random

#number: The number to be guessed (this number is random!)
#Will pick a random number between 0 and 20
number = random.randint(0, 20)

#Boolean: is_guessed is set to false b/c the number hasn't been guessed yet
#Will change to True when the number is guessed
is_guessed = False

#Main Loop
#Keep asking for guesses until the number is guessed!
while (is_guessed == False):
    guess = int(input("Guess the number: "))

    if (guess == number):
        is_guessed = True

print("Congratulations! You guessed the number!")

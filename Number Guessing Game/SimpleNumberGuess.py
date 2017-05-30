#created by Sam Dawes
#Simple number guessing game with static number

print("Guess the number!")

#number: the number to be guessed
number = 10

#Boolean: is_guessed is set to false b/c the number hasn't been guessed yet
#Will change to True when the number is guessed
is_guessed = False

#Main Loop
#Keep asking for guesses until the number is guessed!
while (is_guessed == False):
    guess = int(input("Guess the number: "))

    if(guess == number):
        is_guessed = True

print("Congratulations! You guessed the number!!!")

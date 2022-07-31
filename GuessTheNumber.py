import random

print('Welcome to the Game1 - "Guess The Number(GTN) Game!"')
# print()
playerName = input('May I know your name?:')

number = random.randint(1, 25)
print('Hi ' + playerName + ", I'm thinking of a number between 1 and 25, you will be given 5 chanced to guess the number. Good Luck.")

numberOfGuesses = 0

for guess in range(5):
    numberOfGuesses += 1
    guessedNumber = int(input('Guess the number: '))

    if guessedNumber < number:
        print('Guessed number is too low.')
    
    if guessedNumber > number:
        print('Guessed number is too high')

    if guessedNumber == number:
        break

if guessedNumber == number:
    if numberOfGuesses == 1:
        placeHolder = ' guess'
    else:
        placeHolder = ' guesses'
    print('Great!, you guessed the number in ' + str(numberOfGuesses) + placeHolder + '. My number is ' + str(number))

else:
    print('You failed to guess correct number, better luck next time. My number is ' + str(number))
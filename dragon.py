import random
import time

def displayIntro():
    print("""
Welcome to the Game-5 Dragon Cave. There are two caves infront of you, you can only enter only one cave.
Each cave have treasures which are guarded by Dragons!!!.
Only one cave have friendly dragon, who shares it's treasure, but the ferocious dragon in the 
other cave will eat you.

Be careful and Good Luck Hero!!!""")

def chooseCave():

    cave = ''

    while cave != '1' and cave != '2':
        print('Which cave you wish to enter? (1 or 2)')
        cave = input()
    
    return cave

def checkCave(choosenCave):

    print('You have entered the cave ' + choosenCave + ' ...')
    time.sleep(2)

    print('It\'s very dark and silent...')
    time.sleep(2)

    print('Suddenly a Dragon leaps before you and ...')

    friendlyCave = random.randint(1, 2)

    if choosenCave == str(friendlyCave):
        print('Shares it\'s treasure and talks with you about all of it\'s experiences and it\'s feelings.')
    else:
        print('The dragon opens it\'s mouth and eats you in one gulp!!!')


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    choosenCave = chooseCave()
    checkCave(choosenCave)

    print('Do you want to play again?')
    playAgain = input()
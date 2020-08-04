import random

def start_dice_roll():
    min = 1
    max = 6
    roll_again = 'yes'
    while roll_again == 'y' or roll_again == 'yes':
        diceroll = random.randint(min, max)
        print('Roll 1: ' + str(diceroll))
        diceroll = random.randint(min, max)
        print('Roll 2: ' + str(diceroll))
        roll_again = input('Roll the dice again? ').lower()
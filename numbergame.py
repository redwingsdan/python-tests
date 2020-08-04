import random

def start_number_game():
    number = random.randint(1, 10)

    user_name = input('What is your name?')

    number_guesses = 0;

    print('Alright, ' + user_name + ' I guessed a number: ')

    while number_guesses < 5:
        guess = int(input())
        number_guesses += 1
        if guess < number:
            print('Too low!')
        if guess > number:
            print('Too high!')
        if guess == number:
            break

    if guess == number:
        print('YOU GOT IT! Took ' + str(number_guesses) + ' tries')
    else:
        print('YOU FAILED! The number was ' + str(number))
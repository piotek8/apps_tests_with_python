# Guess that number game

import random


def guess_number(guess, the_number):
    if not isinstance(guess, int):
        raise ValueError('Faulty format')
    if guess not in range(0, 100):
        raise ValueError('Faulty number outside range')

    if guess < the_number:
        return 'Too low'
    elif guess > the_number:
        return 'Too high'
    else:
        return 'You win this game'


def main():
    the_number = random.randint(0, 100)
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    while guess != the_number:
        guess_text = input('Guess a number between 0 and 100: ')
        guess = int(guess_text)
        guess_number(guess, the_number)

    print('done')


# za duza liczba high
# jesli wywolam metode -3 -4 pokaze arytmetyke opis- failed
#
days_until_birthday nie jest
if __name__ == '__main__':
    main()

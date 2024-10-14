from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)

# input from user?
# check that input is a number 1~10


def check_guess(guess, answer):
    if guess and 0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')


def run_game():
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if check_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue


if __name__ == '__main__':
    run_game()

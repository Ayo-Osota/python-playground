from sys import argv
from random import randint
from pyjokes import get_joke


guess = argv[0]

tete = randint(1, 10)

if guess == tete:
    print("win")
else:
    print("loser")


print(get_joke())

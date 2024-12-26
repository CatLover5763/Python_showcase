import random
import sys

def if_decimal(x):
    if x.isdecimal():
        x = int(x)
    else:
        x = 0
    return x

while True:
    number_cap = input("Level: ")
    number_cap = if_decimal(number_cap)
    if number_cap >= 1:
        number_cap = int(number_cap)
        break
random_number = random.randint(1, number_cap)
while True:
    guess_number = input("Guess: ")
    guess_number = if_decimal(guess_number)
    if guess_number > random_number and guess_number >= 1:
        print("Too large!")
    elif guess_number < random_number and guess_number >= 1:
        print("Too small!")
    elif guess_number == random_number and guess_number >= 1:
        sys.exit("Just right!")
    else:
        pass

"""
In a file called game.py, implement a program that:

Prompts the user for a level,
. If the user does not input a positive integer,
the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer.
If the guess is not a positive integer,
the program should prompt the user again.
If the guess is smaller than that integer,
the program should output Too small! and prompt the user again.
If the guess is larger than that integer,
the program should output Too large! and prompt the user again.
If the guess is the same as that integer,
the program should output Just right! and exit.
Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
"""
from random import randint
import sys

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
            else:
                continue
        except:
            continue

    answer = randint(1,n)

    while True:
        try:
            guess = int(input("guess: "))

            if guess < 0:
                continue
            elif guess < answer:
                print("Too small!")
                continue
            elif guess > answer:
                print("Too large!")
                continue
            else:
                print("Just right!")
                break

        except:
            continue
    sys.exit(0)

main()





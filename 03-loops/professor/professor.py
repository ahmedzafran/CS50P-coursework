"""
One of David’s first toys as a child, funny enough, was Little Professor,
a “calculator” that would generate ten different math problems for David to solve.
 For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4.
 If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
 If David were to answer incorrectly, the toy would display EEE.
   And after three incorrect answers for the same problem,
 the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems.
 If an answer is not correct (or not even a number),
 the program should output EEE and prompt the user again,
 allowing the user up to three tries in total for that problem.
 If the user has still not answered correctly after three tries,
   the program should output the correct answer.
The program should ultimately output the user’s score:
the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts
 (and, if need be, re-prompts) the user for a level and returns
   1, 2, or 3, and generate_integer returns a randomly generated
 non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random

def main():
    rslt_level = get_level()
    if rslt_level:
        generate_integer(rslt_level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level

        except ValueError:
            continue

def generate_integer(level):
    x = []
    y = []
    equation = []
    answers = []
    if level == 1:
        for i in range(10):
            x.append(random.randint(0,9))
            y.append(random.randint(0,9))
            answers.append(x[i]+y[i])
            equation.append(f"{str(x[i])} + {str(y[i])} = ")

    elif level == 2:
        for i in range(10):
            x.append(random.randint(10,99))
            y.append(random.randint(10,99))
            answers.append(x[i]+y[i])
            equation.append(f"{str(x[i])} + {str(y[i])} = ")

    elif level == 3:
        for i in range(10):
            x.append(random.randint(100,999))
            y.append(random.randint(100,999))
            answers.append(x[i]+y[i])
            equation.append(f"{str(x[i])} + {str(y[i])} = ")

    s = 0
    score = 0
    while s < 10:
        stopper = 3
        while 0 < stopper:
            try:
                guess = int(input(equation[s]))
                stopper = stopper - 1
                if guess == answers[s]:
                    score += 1
                    break
                print("EEE")
                if (guess != answers[s]) and (stopper == 0):
                    print(f"{equation[s]}{answers[s]}")
                    break

            except ValueError:
                continue
        s += 1
    print(f"Score: {score}")

if __name__ == "__main__":
    main()

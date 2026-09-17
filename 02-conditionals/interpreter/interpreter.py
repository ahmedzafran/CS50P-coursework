"""
In a file called interpreter.py, implement a program that prompts the user for an
arithmetic expression and then calculates and outputs the result as a floating-point value
formatted to one decimal place. Assume that the user’s input will be formatted as x y z,
 with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!

Recall that a str comes with quite a few methods,
per docs.python.org/3/library/stdtypes.html#string-methods, including split,
which separates a str into a sequence of values, all of which can be assigned to variables at once.
For instance, if expression is a str like 1 + 1, then

x, y, z = expression.split(" ")
will assign 1 to x, + to y, and 1 to z.
"""

def main():
    question = input("enter a maths expression (format: x y z): ")
    exprs(question)


def exprs(b):
    x,y,z = b.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        a = x + z
    elif y == "-":
        a = x - z
    elif y == "*":
        a = x * z
    elif y == "/" and z != 0:
        a = x / z
    else:
        print("cannot divide against 0!")
    a = float(a)
    print(a)
    return a

main()

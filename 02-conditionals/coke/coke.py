"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin,
 one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents,
 output how many cents in change the user is owed. Assume that the user will only input integers,
 and ignore any integer that isn’t an accepted denomination.

"""

def main():
    coke_machine()

def coke_machine():
    total = 50
    while total > 0:
        prompt = int(input("please enter cents in the form of 5, 10 or 25: "))
        match prompt:
            case 5 | 10 | 25:
               total = total - prompt
        if total > 0:
            print("Amount Due:", total)
        else:
            print("Change Owed:", abs(total))
    return total



main()


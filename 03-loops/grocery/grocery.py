"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items,
one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
 Treat the user’s input case-insensitively.
"""
def main():
    grcys = {}
    try:
        while True:
            s = input()
            s = s.upper()
            if s not in grcys:
                grcys[s] = 1
            else:
                grcys[s] += 1
    except EOFError:
        s_g = sorted(grcys.items())
        s_d_g = dict(s_g)
        for grcy in s_d_g:
            print(s_d_g[grcy], grcy)

main()



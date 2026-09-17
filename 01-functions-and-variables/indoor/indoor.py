def main():
    userInput = input("enter a \"Caps\" string:" + " ")
    lowered = lowerCaps(userInput)
    print(f"{lowered}")



def lowerCaps(x):
    y = x.lower()
    return y


main()

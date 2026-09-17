from validator_collection import validators, checkers, errors
import sys

def main():
    if walrus := validate(input("What's your email address? ")) is True:
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    return checkers.is_email(s)

if __name__ == "__main__":
    main()

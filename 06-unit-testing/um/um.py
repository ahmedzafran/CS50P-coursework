import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    number = re.findall(r"\bum\b",s, re.IGNORECASE)
    return len(number)



if __name__ == "__main__":
    main()

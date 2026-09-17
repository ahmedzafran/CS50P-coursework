"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
 as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
 implement a program that prompts the user for a str of text and then outputs that
 same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

"""

def main():
    prompt = input("please enter a tweet: ")
    print(shorten(prompt))

def shorten(word):
        for letter in word:
            match letter:
                case  "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                    twtt = word.replace(letter, "")

        return(twtt)




if __name__ == "__main__":
    main()



def main():
    question = input("what is the answer to the Great Question?" + " ")
    answer(question)

def answer(x):
    try:
        x = int(x)
    except:
        x = x.lower()
    match x:
        case 42 | "forty-two" | "forty two":
            print("yes")
        case _:
            print("no")
    return x


main()



def main():
    askEmoticon = input()
    askEmoticon
    convert(askEmoticon)

def convert(x):
    if x.rfind(":)") >=0 and x.rfind(":(") >=0:
        y = x.replace(":)", "🙂")
        z = y.replace(":(", "🙁")
        print(f"Zaf: {z}")
        return z
    elif x.rfind(":)") >= 0:
        y = x.replace(":)", "🙂")
        print(f"Zaf: {y}")
        return y
    else:
        y = x.replace(":(", "🙁")
        print(f"Zaf: {y}")
        return y

main()




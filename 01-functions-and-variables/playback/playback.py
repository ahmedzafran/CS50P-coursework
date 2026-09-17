
def main():
    slowInput = input("enter a sentence:" + " ")
    slowInput
    slowedDown = slowDown(slowInput)
    print(f"{slowedDown}")

def slowDown(x):
    y = x.replace(" ", "...")
    return y

main()


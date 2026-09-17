def main():
    ask = int(input("please enter a int for mass in kg :" + " "))
    ask
    emc(ask)

def emc(x):
    y = x * pow(300000000, 2)
    print(f" E = {y}")
    return y

main()


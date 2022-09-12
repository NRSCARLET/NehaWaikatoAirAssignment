from time import sleep


def greeting():
    hello = ("Welcome {} to Waikato Airlines Discount Centre!\n".format(name))
    return hello


name = input("What's your name? ").title()
for char in greeting():
    sleep(0.1)
    print(char, end="", flush=True)
place = input("Where would you like to travel?")

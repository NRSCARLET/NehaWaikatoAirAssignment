from time import sleep
#making the class
#class Hello:
#e = "wow"
#calling it back
#p1 = Hello()
#printing the class
#print(p1.e)

name = input("What is your name? ").title()


class Greeting:
    welcome = "Welcome {} to Waikato Airlines discount centre"


p2 = Greeting()
for char in Greeting():
    sleep(0.2)
    print(char, end="", flush=True)
print(p2.welcome.format(name))

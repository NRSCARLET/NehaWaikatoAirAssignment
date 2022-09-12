name = True
print("Hello and Welcome to the Waikato Airline Discount Section")
while name == True:
    name = input("What is Your Name? (MINIMUM 3 CHARACTERS)\n>> ").title()
    if len(name) < 3:
        print("Please Enter A Minimum Of 3 Characters")
        name = True
    elif len(name) >= 3:
        print("Hello {}, Where Would You Like to Travel?".format(name))
        name = False

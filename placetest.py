flight_time = False
destination = True
yes_dict = {"yes", "y", "yup"}
no_dict = {"no", "nah", "n"}
print("Hello and Welcome to the Waikato Airline Discount Section")
name = input("What is Your Name?\n>> ").title()
print("Hello {}, Where Would You Like to Travel?".format(name))
while destination == True:
    place = input("Auckland, Hamilton, or Wellington\n>> ").title()
    if place == "Auckland":
        #random time + date generator (line 10, 12, 14)
        print("Your Next Available Flight is at 5:00pm")
        destination = False
    elif place == "Hamilton":
        print("Your Next Available Flight is at 6:00am")
        destination = False
    elif place == "Wellington":
        print("Your Next Available Flight is at 3:00pm")
        destination = False
    else:
        print("That Isn't An Appropriate Answer")
        destination = True
#add prices and discounts
while flight_time == False:
    time = input("Can You Make It To the Given Flight Time?\n>> ").lower()
    if time in yes_dict:
        print("Alright, Your Current Price Is ${}")
        flight_time = True
    elif time in no_dict:
        print("Ok...")
        print("Your Next Available Flight is at")  #input new time
        flight_time = False
    else:
        print("That Isn't An Appropriate Answer")
        #give new time (random)
food = input("Would You Like An Extra Meal?\n>> ")
if food in yes_dict:
    print("Your New Price Is ${}")
elif food in no_dict:
    print("Ok Moving On...")
else:
    print("That Isn't An Appropriate Answer")

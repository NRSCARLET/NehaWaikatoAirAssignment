import random
import time
name = True
destination = True
flight_time = False
yes_dict = {"yes", "y", "yup"}
no_dict = {"no", "nah", "n"}
""" copied and pasted random departure time from stack overflow - changed name of definitions and times"""
def departure_time(start, end, time_format, prop):
    mintime = time.mktime(time.strptime(start, time_format))
    maxtime = time.mktime(time.strptime(end, time_format))
    ptime = mintime + prop * (maxtime - mintime)
    return time.strftime(time_format, time.localtime(ptime))
def random_date(start, end, prop):
    return departure_time(start, end, '%d/%m/%Y %I:%M %p', prop)

    
print("Hello and Welcome to the Waikato Airline Discount Section")
while name == True:
    name = input("What is Your Name? (MINIMUM 3 CHARACTERS)\n>> ").title()
    if len(name) <3:
        print("Please Enter A Minimum Of 3 Characters")
        name = True
    elif len(name) >= 3:
        print("Hello {}, Where Would You Like to Travel?".format(name))
        name = False
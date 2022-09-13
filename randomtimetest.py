#copy and paste this into main 
""" copied and pasted from stack overflow - changed name of definitions and times"""
import random
import time


def departure_time(start, end, time_format, prop):

    mintime = time.mktime(time.strptime(start, time_format))
    maxtime = time.mktime(time.strptime(end, time_format))

    ptime = mintime + prop * (maxtime - mintime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return departure_time(start, end, '%d/%m/%Y %I:%M %p', prop)


print("Your departure time is on {}".format(random_date("1/1/2022 1:30 PM", "1/1/2022 4:50 AM", random.random())))

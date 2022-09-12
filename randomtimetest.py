import random
import time


def random_time(start, end, time_format, prop):
    mintime = time.mktime(time.strptime(start, time_format))
    maxtime = time.mktime(time.strptime(end, time_format))
    ptime = mintime + prop * (mintime - maxtime)
    return time.strftime(time_format, time.localtime(ptime))
def random_date(start, end, prop):
    return random_time(start, end, '%d/%m/%Y %I:%M %p', prop)

print("random_date("1/1/2022 1:30 PM", "31/12/2022 4:50 AM", random.random())
#copy and paste this into main 
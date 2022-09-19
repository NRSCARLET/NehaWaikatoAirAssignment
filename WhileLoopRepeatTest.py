flight_time = 0
max_departure_time = 3
yes_dict = {"yes", "y", "yup"}
no_dict = {"no", "nah", "n"}
#while flight_time == False:
while flight_time < max_departure_time:
    time = input("Can You Make It To the Given Flight Time?\n>> ").lower()
    if time in yes_dict:
        print("Alright, Your Current Price Is ${}")
        if flight_time >= max_departure_time:
            print("Would You Still Like To Book A Flight")
    elif time in no_dict:
        print("Ok...")
        print("Your Next Available Flight is at")  #input new time
        flight_time + 1
    else:
        print("That Isn't An Appropriate Answer")

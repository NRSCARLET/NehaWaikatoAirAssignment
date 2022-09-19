#trying to add an extra meal
yes_dict = {"yes", "y", "yup"}
no_dict = {"no", "nah", "n"}
food = input("Would You Like An Extra Meal?\n>> ")
if food in yes_dict:
    print("Your New Price Is ${}")
elif food in no_dict:
    print("Ok Moving On...")
else:
    print("That Isn't An Appropriate Answer")
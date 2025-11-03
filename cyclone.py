# Installing an entry system (height requirement is 137 cm and cost is 10 credits).
Height=int(input("Please enter your height (in cm):"))
Credit=int(input("Enter how many credits you have:"))
if Height>=137 and Credit >= 10:
  print("Enjoy your ride")
elif Height<=137 and Credit >= 10:
  print("You are not tall enough to ride")
elif Height>=137 and Credit<10:
  print("You don't have enogh credit")
else:
  print("You have not met either requirements")


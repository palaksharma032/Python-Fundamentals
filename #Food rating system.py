#Food rating system
rating=float(input("Enter your rating here:"))
if rating>4.5:
  print("Extraordinary")
elif rating>4:
  print("Excellent")
elif rating>3:
  print("Good")
elif rating>2:
  print("Fair")
else :
  print("Poor")


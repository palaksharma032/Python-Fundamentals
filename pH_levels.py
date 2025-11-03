#ph_levels to check wheter pH level is basic, acidic or neutral.
ph=int(input("Enter value of ph between o to 14:"))
if (ph>7):
  print("Basic")
elif (ph<7):
  print("Acidic")
else:
  print("Neutral")

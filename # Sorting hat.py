# Sorting hat
#House initilization
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
print("Welcome! The Sorting Hat will now determine your house.")
print("---")
# --- Q1 ---
print("Q1) Do you like Dawn or Dusk?")
print("a) Dawn")
print("b) Dusk")
# Use .lower() to make the input case-insensitive (e.g., 'A' is treated as 'a')
answer = input("Enter your answer (a or b): ").lower() 
if answer == 'a':
  print("Gryffindor and Ravenclaw both get a +1.")
  gryffindor += 1
  ravenclaw += 1
elif answer == 'b':
  print("Huffelpuff and Slytherin both get a +1.")
  hufflepuff += 1
  slytherin += 1
else:
  print("Input not recognized.")
print("---")
# --- Q2 ---
print("Q2) When I'm dead i want people to remember me as:")
print("a) The Good")
print("b) The Great")
print("c) The Wise")
print("d) The Bold")
answer = input("Enter your answer (a, b, c, or d): ").lower()
if answer == 'a':
  print("Hufflepuff +2")
  hufflepuff += 2
elif answer == 'b':
  print("Slytherin +2")
  slytherin += 2
elif answer == 'c':
  print("Ravenclaw +2")
  ravenclaw += 2
elif answer == 'd':
  print("Gryffindor +2")
  gryffindor += 2
else:
  print("Input not recognized for Q2.")
print("---")
# --- Q3 ---
print("Q3) Which kind of instrument most pleases your ear?")
print("a) The violin")
print("b) The trumpet")
print("c) The piano")
print("d) The drum")
answer = input("Enter your answer (a, b, c, or d): ").lower()
if answer == 'a':
  print("Slytherin +4")
  slytherin += 4
elif answer == 'b':
  print("Hufflepuff +4")
  hufflepuff += 4
elif answer == 'c':
  print("Ravenclaw +4")
  ravenclaw += 4
elif answer == 'd':
  print("Gryffindor +4")
  gryffindor += 4
else:
  print("Input not recognized for Q3.")
print("---")
# --- Final Sorting ---
print("Calculating final house...")
# Create a dictionary to easily find the house with the max score
house_scores = {
    "Gryffindor": gryffindor,
    "Hufflepuff": hufflepuff,
    "Ravenclaw": ravenclaw,
    "Slytherin": slytherin
}

# Find the house with the maximum score
# max(iterable, key=function) finds the item that has the max value 
# when the function is applied (in this case, the score of the house)
final_house = max(house_scores, key=house_scores.get)

print(f"\nYour House Scores:")
print(f"  Gryffindor: {gryffindor}")
print(f"  Hufflepuff: {hufflepuff}")
print(f"  Ravenclaw: {ravenclaw}")
print(f"  Slytherin: {slytherin}")
print("\n**The Sorting Hat has decided...**")
print(f"**Your house is... {final_house.upper()}!**")
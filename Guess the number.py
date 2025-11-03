# Guess the number
tries=0
Max_tries=6
guess=0
print("I am thinkin of a number between 1-10. Can you guess it?")
while guess!= 6 and tries<=Max_tries:
    guess= int(input("Guess the number:"))
    tries+=1
    if guess ==6:
      print("You Got it!")
      break
    else:
      print("Try Again")
if guess!=6:
  print("You Lost")



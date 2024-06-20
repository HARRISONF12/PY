import random

print("Welcome to the Random Number Generator!")

randomnumber = random.randint(1, 100)
count = 0
check = False
Name = input("What is your name? ")

while check == False:
  guessnumber = int(input("Guess the random number:"))
  if guessnumber == randomnumber:
    print("Great guess,", Name, "! Your guess was correct!")
    check = True
  elif guessnumber > randomnumber:
    print("Go lower")
    count = count + 1
    if count >= 8:
      print ("Good try", Name, ". The number was actually", randomnumber)
      break
  else:
    print("Even Higher")
    count = count + 1
    if count >= 8:
      print ("Good try", Name, ". The number was actually", randomnumber)
      break

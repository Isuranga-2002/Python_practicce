# Write code below 💖

guess = 0
tries = 0

guess = int(input("Guess the number:  "))
tries += 1

while guess != 6 and tries < 5:
  guess = int(input("You are incorrect. Guess the number again:  "))
  tries += 1
  
if tries == 5:
  print("You loss!")
else: 
  print("You got it!")
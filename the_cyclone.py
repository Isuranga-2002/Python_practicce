# Write code below 💖

height = int(input('What is your height (cm)? '))

if height <= 0:
  print("Invalid input!")
  exit()
elif height < 137:
  print("You are not tall enough to ride.")
  exit()

credits = int(input('How many credits do you have? '))

if credits < 0:
  print("Invalid input!")
  exit()
  exit()
elif credits < 10:
  print("You don't have enough credits.")
  exit()
else:
  print("Enjoy the ride!")

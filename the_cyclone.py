# Write code below 💖

height = int(input('What is your height (cm)? '))

if height <= 0:
  print("Invalid input!")
  exit()

credits = int(input('How many credits do you have? '))
if credits < 0:
  print("Invalid input!")
  exit()

if height >= 137 and credits >= 10:
  print("Enjoy the ride!")
elif height < 137 and credits >= 10:
  print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
  print("You don't have enough credits.")
else:
  print("Sorry! You have not met either requirement.")
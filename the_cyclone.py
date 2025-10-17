# Write code below 💖
height = 0
credits = 0

while height <= 0:
  height = int(input("Enter your height in cm: "))
  if height <= 0:
    print("Invalid input! Height must be greater than zero.\n")
    continue

if height >= 137:
  while credits <= 0:
    credits = int(input("Enter number of credits you have: "))
    if credits <= 0:
      print("Invalid input! Credits must be greater than zero.\n")
      continue
  if credits >= 10:
      print("You can ride the cyclone!")
  else:
      print("You need at least 10 credits to ride the cyclone.")
else:
  print("You need to be at least 137 cm tall to ride the cyclone.")

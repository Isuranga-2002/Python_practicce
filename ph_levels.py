# Write code below 💖

ph = int(input('Enter a pH value (0-14): '))

if ph < 0 or ph > 14:
  print("Invalid Input!")
elif ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
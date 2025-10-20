from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

def radius(r):
    return 4*pi*r*r

if random_planet == 'Mercury':
    print(f"The area of Mercury is {radius(2440)}")
elif random_planet == 'Venus':
    print(f"The area of Venus is {radius(6052)}")
elif random_planet == 'Earth':
    print(f"The area of Earth is {radius(6371)}")
elif random_planet == 'Mars':
    print(f"The area of Mars is {radius(3390)}")
elif random_planet == 'Saturn':
    print(f"The area of Saturn is {radius(58232)}")
else:
    print("Oops! An error occurred.")
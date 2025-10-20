# Write code below 💖

print("Please select the moon phase:\n")
print("  1) New Moon")
print("  2) Waxing Crescent")
print("  3) First Quarter ")
print("  4) Waxing Gibbous")
print("  5) Full Moon")
print("  6) Waning Gibbous ")
print("  7) Last Quarter ")
print("  8) Waning Crescent ")

imojis = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']

def moon_phase(a):
  return imojis[a-1]

while True:
    try:
        phase = int(input("\nSelect(1-8) or 'i' for quit: "))
        print("\nThe imoji is: ",moon_phase(phase))
        break
    except ValueError:
        print("⚠️ Please enter a valid number between 1-8!\n")
        continue
    except IndexError:
        print("⚠️ Please enter a valid number between 1-8!\n")
        continue
  

print("Please select the moon phase:\n")
print("  1) New Moon")
print("  2) Waxing Crescent")
print("  3) First Quarter")
print("  4) Waxing Gibbous")
print("  5) Full Moon")
print("  6) Waning Gibbous")
print("  7) Last Quarter")
print("  8) Waning Crescent")

emojis = ['🌑','🌒','🌓','🌔','🌕','🌖','🌗','🌘']

def moon_phase(a):
    return emojis[a - 1]

while True:
    user_input = input("\nSelect (1-8) or 'i' to quit: ").strip().lower()

    if user_input == 'i':
        print("\n🌙 Goodbye! See you next lunar cycle!")
        break

    try:
        phase = int(user_input)
        if 1 <= phase <= 8:
            print("\nThe emoji is:", moon_phase(phase))
            break
        else:
            print("⚠️ Please enter a number between 1 and 8!\n")
    except ValueError:
        print("⚠️ Please enter a valid number between 1 and 8!\n")

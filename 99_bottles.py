# Write code below 💖

for i in range(99, 0, -1):  # start at 99, stop before 0, step down by 1
    print(f"{i} bottle{'s' if i != 1 else ''} of beer on the wall")
    print(f"{i} bottle{'s' if i != 1 else ''} of beer")
    print("Take one down and pass it around")

    next_bottle = i - 1
    if next_bottle > 0:
        print(f"{next_bottle} bottle{'s' if next_bottle != 1 else ''} of beer on the wall")
    else:
        print("No more bottles of beer on the wall")

    print("\n")

import math

while True:
    print("\n📏 AREA CALCULATOR 📏")
    print("---------------------")
    print("  1) Square")
    print("  2) Rectangle")
    print("  3) Triangle")
    print("  4) Circle")

    try:
        shape = int(input("\nEnter a number (1-4): "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    # --- Square ---
    if shape == 1:
        try:
            side = float(input("\nEnter the length of one side: "))
            area = side * side
            print(f"\n✅ The area of the square is: {area:.2f}")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    # --- Rectangle ---
    elif shape == 2:
        try:
            length = float(input("\nEnter the length: "))
            width = float(input("Enter the width: "))
            area = length * width
            print(f"\n✅ The area of the rectangle is: {area:.2f}")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    # --- Triangle ---
    elif shape == 3:
        try:
            a = float(input("\nEnter the 1st side: "))
            b = float(input("Enter the 2nd side: "))
            c = float(input("Enter the 3rd side: "))

            # Check for triangle validity
            if a + b > c and a + c > b and b + c > a:
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                print(f"\n✅ The area of the triangle is: {area:.2f}")
            else:
                print("⚠️ These sides cannot form a valid triangle.")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    # --- Circle ---
    elif shape == 4:
        try:
            radius = float(input("\nEnter the radius: "))
            area = math.pi * radius * radius
            print(f"\n✅ The area of the circle is: {area:.2f}")
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    else:
        print("⚠️ Invalid choice. Please choose a number between 1 and 4.")
        continue

    # Ask if user wants to continue
    again = input("\nWould you like to calculate another area? (y/n): ").lower()
    if again != 'y':
        print("\n👋 Thank you for using the Area Calculator!")
        break

items = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']

def drive_thru_item(a):
    if 1 <= a <= len(items):
     return items[a - 1]
    else:
     return "❌ Invalid choice. Please select a number from 1 to 5."


def welcome():
    print("🚗🍟 Welcome to Drive-Thru Express! 🍔🥤")
    print("------------------------------------")
    print("Please select your item by entering the number:\n")
    print("  1) Burger")
    print("  2) Fries")
    print("  3) Fried Chicken")
    print("  4) Sandwich")
    print("  5) Coffee")

    try:
        item = int(input("\nEnter a number: "))
        print("\nYou selected: ", drive_thru_item(item))
    except ValueError:
        print("⚠️ Please enter a valid number!\n")

welcome()




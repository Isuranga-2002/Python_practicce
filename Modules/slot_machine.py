import random

# List of symbols
symbols = ['🍒', '🍇', '🍉', '7️⃣']

def play():
    while True:
        # Spin the slot machine
        results = random.choices(symbols, k=3)
        print(" | ".join(results))

        # Check for jackpot
        if results == ['7️⃣', '7️⃣', '7️⃣']:
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")

        # Ask if the player wants to continue
        choice = input("Play again? (Y/N): ").strip().upper()

        if choice != 'Y':
            print("Goodbye! 👋")
            break

# Run the game
play()



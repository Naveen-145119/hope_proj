# ============================================================
#  Mini Project: Coffee Making Machine
#  Hope Foundation Internship – Basic Python
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

import time

# ── Coffee menu: name → list of preparation steps ──────────
COFFEE_MENU = {
    1: {
        "name": "Espresso",
        "steps": [
            "Grinding fresh coffee beans...",
            "Heating water to 93°C...",
            "Tamping the ground coffee...",
            "Pulling the espresso shot (25 seconds)...",
            "Your Espresso is ready! ☕",
        ],
    },
    2: {
        "name": "Cappuccino",
        "steps": [
            "Grinding fresh coffee beans...",
            "Heating water to 93°C...",
            "Pulling the espresso shot...",
            "Steaming milk to 65°C...",
            "Frothing milk to a thick foam...",
            "Pouring steamed milk over espresso...",
            "Adding milk foam on top...",
            "Your Cappuccino is ready! ☕",
        ],
    },
    3: {
        "name": "Latte",
        "steps": [
            "Grinding fresh coffee beans...",
            "Heating water to 93°C...",
            "Pulling the espresso shot...",
            "Steaming milk to 70°C...",
            "Pouring a generous amount of steamed milk...",
            "Adding a light layer of foam...",
            "Your Latte is ready! ☕",
        ],
    },
    4: {
        "name": "Black Coffee",
        "steps": [
            "Measuring coffee grounds...",
            "Heating water to 95°C...",
            "Pouring hot water over the grounds...",
            "Allowing to brew for 4 minutes...",
            "Your Black Coffee is ready! ☕",
        ],
    },
}


# ── Display the coffee menu ─────────────────────────────────
def display_menu():
    print("\n" + "=" * 45)
    print("       WELCOME TO HOPE FOUNDATION CAFÉ")
    print("=" * 45)
    print("  Please choose your coffee:\n")
    for key, value in COFFEE_MENU.items():
        print(f"  [{key}] {value['name']}")
    print("  [0] Exit")
    print("=" * 45)


# ── Simulate the brewing process step by step ──────────────
def brew_coffee(choice):
    coffee = COFFEE_MENU[choice]
    print(f"\n  🫘 Starting your {coffee['name']}...\n")
    time.sleep(1)
    for step in coffee["steps"]:
        print(f"  ➤  {step}")
        time.sleep(1.2)
    print()


# ── Get and validate user input ────────────────────────────
def get_user_choice():
    while True:
        try:
            raw = input("\n  Enter your choice: ")
            choice = int(raw)          # TypeError fix: always convert input to int
            if choice == 0 or choice in COFFEE_MENU:
                return choice
            else:
                print(f"  ⚠  Invalid option. Please enter a number between 0 and {len(COFFEE_MENU)}.")
        except ValueError:
            print("  ⚠  Please enter a number, not text.")


# ── Main loop ───────────────────────────────────────────────
def main():
    print("\n  Powering up the coffee machine...")
    time.sleep(1)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 0:
            print("\n  Thank you for visiting Hope Foundation Café! Goodbye. 👋\n")
            break

        brew_coffee(choice)

        again = input("  Would you like another coffee? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thank you for visiting Hope Foundation Café! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()

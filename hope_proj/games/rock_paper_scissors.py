# ============================================================
#  Game: Rock, Paper and Scissors
#  Concepts : Control Structure Statements + random module
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

import random

CHOICES = ["Rock", "Paper", "Scissors"]

RULES = {
    ("Rock",     "Scissors"): "Rock crushes Scissors",
    ("Paper",    "Rock"):     "Paper covers Rock",
    ("Scissors", "Paper"):    "Scissors cuts Paper",
}


# ── Determine round result ──────────────────────────────────
def get_result(player, computer):
    if player == computer:
        return "draw", "It's a Draw! 🤝"
    elif (player, computer) in RULES:
        return "win", f"You Win! 🎉  ({RULES[(player, computer)]})"
    else:
        return "lose", f"You Lose! 💻  ({RULES[(computer, player)]})"


# ── Get valid player input ──────────────────────────────────
def get_player_choice():
    print("\n  Options:  [1] Rock   [2] Paper   [3] Scissors")
    while True:
        try:
            choice = int(input("  Your choice (1/2/3): "))
            if 1 <= choice <= 3:
                return CHOICES[choice - 1]
            else:
                print("  ⚠  Enter 1, 2, or 3.")
        except ValueError:
            print("  ⚠  Please enter a number.")


# ── Play one round ──────────────────────────────────────────
def play_round():
    player   = get_player_choice()
    computer = random.choice(CHOICES)          # random module: pick computer move

    print(f"\n  You chose   : {player}")
    print(f"  Computer chose: {computer}")

    outcome, message = get_result(player, computer)
    print(f"  {message}")
    return outcome


# ── Main game loop ──────────────────────────────────────────
def main():
    wins = losses = draws = 0

    print("\n" + "=" * 45)
    print("      ROCK, PAPER AND SCISSORS GAME")
    print("=" * 45)

    while True:
        outcome = play_round()

        # Update scoreboard using control structure statements
        if outcome == "win":
            wins += 1
        elif outcome == "lose":
            losses += 1
        else:
            draws += 1

        print(f"\n  📊 Score  →  Wins: {wins}  |  Losses: {losses}  |  Draws: {draws}")

        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n" + "=" * 45)
    print("  FINAL SCORE")
    print(f"  Wins   : {wins}")
    print(f"  Losses : {losses}")
    print(f"  Draws  : {draws}")
    print("  Thanks for playing! 🎮")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()

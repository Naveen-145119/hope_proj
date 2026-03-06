# ============================================================
#  Practice: Loops and Pattern Programs
#  Topics   : for, while, nested loops, break/continue
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

# ── 1. for loop with range() ────────────────────────────────
print("=== for loop: Multiplication Table ===")
n = int(input("Enter a number for its table: "))
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

# ── 2. while loop – Countdown ──────────────────────────────
print("\n=== while loop: Countdown ===")
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Go! 🚀")

# ── 3. break and continue ───────────────────────────────────
print("\n=== break: Stop at first multiple of 7 ===")
for i in range(1, 50):
    if i % 7 == 0:
        print(f"First multiple of 7 in range: {i}")
        break

print("\n=== continue: Skip multiples of 3 (1–15) ===")
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# ── 4. Pattern: Right-angled triangle ──────────────────────
print("\n=== Pattern: Right-Angled Triangle ===")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("* " * i)

# ── 5. Pattern: Pyramid ─────────────────────────────────────
print("\n=== Pattern: Pyramid ===")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# ── 6. Pattern: Number triangle ────────────────────────────
print("\n=== Pattern: Number Triangle ===")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ── 7. Factorial using while ────────────────────────────────
print("\n=== Factorial ===")
num = int(input("Enter a number to find factorial: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print(f"{num}! = {factorial}")

# ── 8. Sum of digits ───────────────────────────────────────
print("\n=== Sum of Digits ===")
number = int(input("Enter a number: "))
total = 0
temp = abs(number)
while temp > 0:
    total += temp % 10
    temp //= 10
print(f"Sum of digits of {number} = {total}")

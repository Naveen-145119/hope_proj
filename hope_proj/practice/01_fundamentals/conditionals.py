# ============================================================
#  Practice: Conditional Statements
#  Topics   : if, if-else, elif, nested conditions
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

# ── 1. Simple if-else ───────────────────────────────────────
print("=== Even or Odd ===")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# ── 2. elif chain – Grade Calculator ───────────────────────
print("\n=== Grade Calculator ===")
marks = float(input("Enter your marks (0–100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

print(f"Marks: {marks}  →  Grade: {grade}")

# ── 3. Nested conditions – Voting Eligibility ───────────────
print("\n=== Voting Eligibility ===")
age        = int(input("Enter your age      : "))
is_citizen = input("Are you a citizen? (yes/no): ").strip().lower()

if age >= 18:
    if is_citizen == "yes":
        print("✅ You are eligible to vote.")
    else:
        print("❌ You are not eligible – not a citizen.")
else:
    print(f"❌ You are not eligible – must be at least 18 (you are {age}).")

# ── 4. Positive / Negative / Zero ──────────────────────────
print("\n=== Positive, Negative, or Zero ===")
n = float(input("Enter a number: "))
if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

# ── 5. Largest of three numbers ────────────────────────────
print("\n=== Largest of Three Numbers ===")
a = float(input("Enter first  number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third  number: "))

if a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")

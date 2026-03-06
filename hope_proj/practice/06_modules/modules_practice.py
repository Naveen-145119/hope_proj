# ============================================================
#  Practice: Standard Library Modules
#  Topics   : math, random, datetime, os
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

import math
import random
import datetime
import os


# ─────────────────────────────────────────────────────────────
#  math module
# ─────────────────────────────────────────────────────────────
print("=" * 45)
print("   math module")
print("=" * 45)

r = float(input("Enter radius of a circle: "))
print(f"  Circumference : {2 * math.pi * r:.4f}")
print(f"  Area          : {math.pi * r ** 2:.4f}")

num = float(input("\nEnter a number: "))
print(f"  sqrt({num})    = {math.sqrt(num):.4f}")
print(f"  ceil({num})    = {math.ceil(num)}")
print(f"  floor({num})   = {math.floor(num)}")
print(f"  log10({num})   = {math.log10(num):.4f}")
print(f"  factorial(5)   = {math.factorial(5)}")
print(f"  sin(90°)       = {math.sin(math.radians(90)):.4f}")
print(f"  pi             = {math.pi:.6f}")
print(f"  e              = {math.e:.6f}")


# ─────────────────────────────────────────────────────────────
#  random module
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("   random module")
print("=" * 45)

print(f"  random()             : {random.random():.6f}")
print(f"  randint(1, 100)      : {random.randint(1, 100)}")
print(f"  randrange(0, 50, 5)  : {random.randrange(0, 50, 5)}")

items = ["Python", "Java", "C++", "JavaScript", "Kotlin"]
print(f"  choice({items})      : {random.choice(items)}")

sample = random.sample(items, 3)
print(f"  sample (3 items)     : {sample}")

nums = list(range(1, 11))
random.shuffle(nums)
print(f"  shuffle(1–10)        : {nums}")


# ─────────────────────────────────────────────────────────────
#  datetime module
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("   datetime module")
print("=" * 45)

now   = datetime.datetime.now()
today = datetime.date.today()

print(f"  Current date & time  : {now.strftime('%d-%m-%Y  %H:%M:%S')}")
print(f"  Today's date         : {today}")
print(f"  Day of week          : {now.strftime('%A')}")
print(f"  Month name           : {now.strftime('%B')}")
print(f"  Year                 : {now.year}")

# Days between two dates
start  = datetime.date(2026, 1, 28)   # internship start
end    = datetime.date(2026, 2, 28)   # internship end
delta  = end - start
print(f"\n  Internship start     : {start}")
print(f"  Internship end       : {end}")
print(f"  Duration             : {delta.days} days")


# ─────────────────────────────────────────────────────────────
#  os module
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("   os module")
print("=" * 45)

print(f"  Current directory    : {os.getcwd()}")
print(f"  OS name              : {os.name}")

# List files in current directory
entries = os.listdir(".")
print(f"  Files/folders here   : {entries[:5]} ...")   # show first 5

# Path operations
sample_path = os.path.join("practice", "06_modules", "modules_practice.py")
print(f"  Joined path          : {sample_path}")
print(f"  Basename             : {os.path.basename(sample_path)}")
print(f"  Dirname              : {os.path.dirname(sample_path)}")

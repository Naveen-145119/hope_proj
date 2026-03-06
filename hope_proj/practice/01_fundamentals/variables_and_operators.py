# ============================================================
#  Practice: Python Fundamentals
#  Topics   : Variables, Data Types, Operators, Input/Output
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

# ── 1. Variables and Dynamic Typing ────────────────────────
name   = "Naveen"
age    = 21
height = 5.9
is_student = True

print("=== Variables and Data Types ===")
print(f"Name    : {name}   | Type: {type(name)}")
print(f"Age     : {age}    | Type: {type(age)}")
print(f"Height  : {height} | Type: {type(height)}")
print(f"Student : {is_student} | Type: {type(is_student)}")

# ── 2. Type Conversion ──────────────────────────────────────
print("\n=== Type Conversion ===")
num_str = "42"
num_int = int(num_str)
print(f"String '42' converted to int: {num_int} + 8 = {num_int + 8}")

# ── 3. Arithmetic Operators ─────────────────────────────────
a, b = 17, 5
print("\n=== Arithmetic Operators ===")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")
print(f"{a} // {b} = {a // b}  (floor division)")
print(f"{a} % {b}  = {a % b}   (modulus)")
print(f"{a} ** {b} = {a ** b}  (exponent)")

# ── 4. Relational and Logical Operators ─────────────────────
x, y = 10, 20
print("\n=== Relational & Logical Operators ===")
print(f"x={x}, y={y}")
print(f"x > y  : {x > y}")
print(f"x < y  : {x < y}")
print(f"x == y : {x == y}")
print(f"x != y : {x != y}")
print(f"x > 5 and y > 5  : {x > 5 and y > 5}")
print(f"x > 15 or  y > 15: {x > 15 or y > 15}")
print(f"not (x > y)      : {not (x > y)}")

# ── 5. Input / Output with f-strings ───────────────────────
print("\n=== Input & Output ===")
user_name = input("Enter your name: ")
user_age  = int(input("Enter your age : "))
print(f"Hello, {user_name}! You are {user_age} years old.")
print(f"In 10 years you will be {user_age + 10} years old.")

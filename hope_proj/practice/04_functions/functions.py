# ============================================================
#  Practice: Functions
#  Topics   : def, return, arguments, scope, lambda
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

# ── 1. Fibonacci Series ─────────────────────────────────────
def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("=== Fibonacci Series ===")
terms = int(input("How many terms? "))
print(f"First {terms} terms: {fibonacci(terms)}")


# ── 2. Armstrong Number Check ──────────────────────────────
def is_armstrong(num):
    """Return True if num is an Armstrong number."""
    digits = str(num)
    power  = len(digits)
    return num == sum(int(d) ** power for d in digits)

print("\n=== Armstrong Number Check ===")
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} IS an Armstrong number ✅")
else:
    print(f"{n} is NOT an Armstrong number ❌")

print("\nArmstrong numbers from 1 to 999:")
print([x for x in range(1, 1000) if is_armstrong(x)])


# ── 3. Prime Number Check ──────────────────────────────────
def is_prime(num):
    """Return True if num is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("\n=== Prime Number Check ===")
n = int(input("Enter a number: "))
print(f"{n} is {'PRIME ✅' if is_prime(n) else 'NOT prime ❌'}")

print("\nPrime numbers from 1 to 50:")
print([x for x in range(2, 51) if is_prime(x)])


# ── 4. Calculator using Functions ──────────────────────────
def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Map operator symbols to functions (elegant design pattern)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("\n=== Calculator ===")
try:
    x  = float(input("Enter first  number : "))
    op = input("Enter operator (+, -, *, /): ").strip()
    y  = float(input("Enter second number : "))

    if op in operations:
        result = operations[op](x, y)
        print(f"Result: {x} {op} {y} = {result}")
    else:
        print("Invalid operator.")
except ValueError:
    print("Please enter valid numbers.")


# ── 5. Different Argument Types ────────────────────────────
def greet(name, greeting="Hello", punctuation="!"):
    """Demonstrates default and keyword arguments."""
    return f"{greeting}, {name}{punctuation}"

print("\n=== Argument Types ===")
print(greet("Naveen"))                              # positional
print(greet("Naveen", greeting="Good morning"))     # keyword arg
print(greet("Naveen", "Hi", "..."))                 # all positional

def total(*args):
    """*args: accepts any number of positional arguments."""
    return sum(args)

print(f"\nSum of 1,2,3     : {total(1, 2, 3)}")
print(f"Sum of 5,10,15,20: {total(5, 10, 15, 20)}")

def show_info(**kwargs):
    """**kwargs: accepts any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nStudent info:")
show_info(name="Naveen", usn="U19MT23S0117", semester=6, branch="BCA")

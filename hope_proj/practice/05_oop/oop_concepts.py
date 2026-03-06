# ============================================================
#  Practice: Object-Oriented Programming
#  Topics   : Classes, Inheritance, Polymorphism, Encapsulation
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================


# ─────────────────────────────────────────────────────────────
#  1. Basic Class – Student
# ─────────────────────────────────────────────────────────────
class Student:
    """Represents a student with name, roll number, and marks."""

    institution = "East Point College of Higher Education"   # class variable

    def __init__(self, name, roll_number, marks):
        self.name        = name           # instance variables
        self.roll_number = roll_number
        self.marks       = marks          # list of marks in subjects

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:   return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else:           return "F"

    def display(self):
        print(f"\n  Name        : {self.name}")
        print(f"  Roll Number : {self.roll_number}")
        print(f"  Marks       : {self.marks}")
        print(f"  Average     : {self.average():.2f}")
        print(f"  Grade       : {self.grade()}")

    def __str__(self):
        return f"Student({self.name}, {self.roll_number})"


print("=" * 45)
print("   CLASS: Student")
print("=" * 45)

s1 = Student("Naveen Reddy", "U19MT23S0117", [88, 76, 82, 79, 91])
s2 = Student("Ananya Sharma", "U19MT23S0118", [95, 92, 98, 90, 97])

s1.display()
s2.display()
print(f"\nInstitution: {Student.institution}")


# ─────────────────────────────────────────────────────────────
#  2. Encapsulation – Bank Account
# ─────────────────────────────────────────────────────────────
class BankAccount:
    """Demonstrates encapsulation with private balance."""

    def __init__(self, owner, initial_balance=0):
        self.owner    = owner
        self.__balance = initial_balance   # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"  ✅ Deposited ₹{amount:.2f}. New balance: ₹{self.__balance:.2f}")
        else:
            print("  ⚠  Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"  ❌ Insufficient funds. Balance: ₹{self.__balance:.2f}")
        elif amount <= 0:
            print("  ⚠  Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"  ✅ Withdrew ₹{amount:.2f}. New balance: ₹{self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount({self.owner}, ₹{self.__balance:.2f})"


print("\n" + "=" * 45)
print("   CLASS: BankAccount (Encapsulation)")
print("=" * 45)

acc = BankAccount("Naveen Reddy", 1000)
print(f"  Owner: {acc.owner}")
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
print(f"  Final balance: ₹{acc.get_balance():.2f}")


# ─────────────────────────────────────────────────────────────
#  3. Inheritance and Polymorphism – Vehicle hierarchy
# ─────────────────────────────────────────────────────────────
class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year

    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

    def fuel_type(self):
        return "Unknown"

    def __str__(self):
        return f"{self.describe()} [{self.fuel_type()}]"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def fuel_type(self):               # method overriding
        return "Petrol / Diesel"

    def describe(self):
        return f"{super().describe()} ({self.doors}-door car)"


class ElectricCar(Car):
    def __init__(self, brand, model, year, doors, range_km):
        super().__init__(brand, model, year, doors)
        self.range_km = range_km

    def fuel_type(self):               # override again
        return "Electric"

    def describe(self):
        return f"{super().describe()} | Range: {self.range_km} km"


class Motorcycle(Vehicle):
    def fuel_type(self):
        return "Petrol"

    def describe(self):
        return f"{super().describe()} (motorcycle)"


print("\n" + "=" * 45)
print("   INHERITANCE & POLYMORPHISM: Vehicles")
print("=" * 45)

vehicles = [
    Car("Toyota", "Camry", 2022, 4),
    ElectricCar("Tesla", "Model 3", 2023, 4, 560),
    Motorcycle("Royal Enfield", "Classic 350", 2021),
]

# Polymorphism: same method call, different behavior per class
for v in vehicles:
    print(f"  {v}")

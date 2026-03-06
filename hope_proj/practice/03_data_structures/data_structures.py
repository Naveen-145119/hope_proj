# ============================================================
#  Practice: Data Structures
#  Topics   : Lists, Tuples, Sets, Dictionaries
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

# ─────────────────────────────────────────────────────────────
#  LISTS
# ─────────────────────────────────────────────────────────────
print("=" * 45)
print("           LISTS")
print("=" * 45)

fruits = ["apple", "banana", "cherry", "mango", "grape"]
print(f"Original list : {fruits}")
print(f"Index 0       : {fruits[0]}")
print(f"Last element  : {fruits[-1]}")
print(f"Slice [1:3]   : {fruits[1:3]}")

fruits.append("orange")
print(f"After append  : {fruits}")

fruits.remove("banana")
print(f"After remove  : {fruits}")

fruits.sort()
print(f"After sort    : {fruits}")

fruits.reverse()
print(f"After reverse : {fruits}")

print(f"Length        : {len(fruits)}")

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares 1-5   : {squares}")


# ─────────────────────────────────────────────────────────────
#  TUPLES
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("           TUPLES")
print("=" * 45)

coordinates = (10.5, 20.3, 5.0)
print(f"Coordinates   : {coordinates}")
print(f"X             : {coordinates[0]}")
print(f"Count of 10.5 : {coordinates.count(10.5)}")
print(f"Index of 20.3 : {coordinates.index(20.3)}")

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked      : x={x}, y={y}, z={z}")

# Tuples are immutable – this would raise a TypeError:
# coordinates[0] = 99


# ─────────────────────────────────────────────────────────────
#  SETS
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("           SETS")
print("=" * 45)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A         : {set_a}")
print(f"Set B         : {set_b}")
print(f"Union         : {set_a | set_b}")
print(f"Intersection  : {set_a & set_b}")
print(f"Difference A-B: {set_a - set_b}")

# Remove duplicates from a list using a set
nums_with_dups = [1, 2, 2, 3, 4, 4, 5, 1]
unique = list(set(nums_with_dups))
unique.sort()
print(f"\nOriginal      : {nums_with_dups}")
print(f"Duplicates removed: {unique}")


# ─────────────────────────────────────────────────────────────
#  DICTIONARIES
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 45)
print("           DICTIONARIES")
print("=" * 45)

student = {
    "name"  : "Naveen Reddy",
    "usn"   : "U19MT23S0117",
    "branch": "BCA",
    "marks" : {"Python": 88, "DBMS": 76, "OS": 82},
}

print(f"Name   : {student['name']}")
print(f"USN    : {student['usn']}")
print(f"Branch : {student['branch']}")
print(f"Marks  : {student['marks']}")

# Add and update
student["semester"] = 6
student["marks"]["Networking"] = 79
print(f"\nAfter update: {student}")

# Iterate
print("\nAll subjects and marks:")
for subject, mark in student["marks"].items():
    print(f"  {subject:<15}: {mark}")

# Dictionary methods
print(f"\nKeys   : {list(student.keys())}")
print(f"Values : {list(student.values())}")
print(f"'usn' in student: {'usn' in student}")

# Hope Foundation Internship – Python Programming Projects

**Intern:** P. Naveen Reddy  
**USN:** U19MT23S0117  
**Institution:** East Point College of Higher Education, Bengaluru  
**Organization:** Hope Foundation, Bengaluru  
**Period:** 28 January 2026 – 28 February 2026 (90 Hours)  

---

## Repository Structure

```
hope_proj/
│
├── mini_project/
│   └── coffee_making_machine.py      ← Mini Project (Basic Python)
│
├── games/
│   ├── rock_paper_scissors.py        ← Control Structures + random module
│   └── snake_game.py                 ← User Defined Functions + turtle module
│
├── practice/
│   ├── 01_fundamentals/
│   │   ├── variables_and_operators.py
│   │   └── conditionals.py
│   ├── 02_loops/
│   │   └── loops_and_patterns.py
│   ├── 03_data_structures/
│   │   └── data_structures.py
│   ├── 04_functions/
│   │   └── functions.py
│   ├── 05_oop/
│   │   └── oop_concepts.py
│   └── 06_modules/
│       └── modules_practice.py
│
└── README.md
```

---

## Projects

### ☕ Mini Project: Coffee Making Machine
**File:** `mini_project/coffee_making_machine.py`  
**Concepts:** Dictionaries, Functions, Loops, `time` module  

A console-based coffee simulator. The user selects a coffee type from a menu, and the program walks through each preparation step one by one using `time.sleep()` for a realistic brewing effect.

**How to run:**
```bash
python mini_project/coffee_making_machine.py
```

---

### ✂️ Rock, Paper and Scissors Game
**File:** `games/rock_paper_scissors.py`  
**Concepts:** Control Structure Statements, `random` module  

A fully playable Rock Paper Scissors game against the computer. Uses `random.choice()` to pick the computer's move, and nested `if-elif-else` control structures to evaluate every possible outcome. Tracks wins, losses, and draws across multiple rounds.

**How to run:**
```bash
python games/rock_paper_scissors.py
```

---

### 🐍 Snake Game
**File:** `games/snake_game.py`  
**Concepts:** User Defined Functions, `turtle` module  

A classic Snake Game with a graphical window built using Python's built-in `turtle` module. Each game concern (movement, collision detection, food placement, score display) is isolated in its own User Defined Function. Use arrow keys or W/A/S/D to control the snake.

**How to run:**
```bash
python games/snake_game.py
```
> Requires a display (does not run in headless terminals).

---

## Practice Programs

| Folder | Topics Covered |
|--------|---------------|
| `01_fundamentals` | Variables, data types, operators, input/output, conditionals |
| `02_loops` | for, while, nested loops, break/continue, pattern programs |
| `03_data_structures` | Lists, Tuples, Sets, Dictionaries |
| `04_functions` | def, return, argument types (*args, **kwargs), scope |
| `05_oop` | Classes, `__init__`, encapsulation, inheritance, polymorphism |
| `06_modules` | math, random, datetime, os standard library modules |

---

## Requirements

- Python 3.x (developed on Python 3.12)
- No external libraries required – all standard library
- `snake_game.py` requires a graphical display (uses `tkinter` via `turtle`)

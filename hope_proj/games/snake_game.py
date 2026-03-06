# ============================================================
#  Game: Snake Game
#  Concepts : User Defined Functions + turtle module
#  Hope Foundation Internship
#  Author : P. Naveen Reddy | USN: U19MT23S0117
# ============================================================

import turtle
import random
import time

# ── Constants ───────────────────────────────────────────────
WIDTH        = 600
HEIGHT       = 600
SEGMENT_SIZE = 20
DELAY        = 0.1


# ── 1. Initialize the game window and turtles ───────────────
def setup_window():
    win = turtle.Screen()
    win.title("Snake Game – Hope Foundation Internship")
    win.bgcolor("black")
    win.setup(width=WIDTH, height=HEIGHT)
    win.tracer(0)          # turn off auto-update for smooth movement
    return win


def create_head():
    head = turtle.Turtle()
    head.shape("square")
    head.color("lime green")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    return head


def create_food():
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.shapesize(0.75, 0.75)
    place_food(food)
    return food


def create_score_display():
    pen = turtle.Turtle()
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, HEIGHT // 2 - 30)
    return pen


# ── 2. Place food at a random position ─────────────────────
def place_food(food):
    x = random.randint(-(WIDTH  // 2 - 20) // SEGMENT_SIZE, (WIDTH  // 2 - 20) // SEGMENT_SIZE) * SEGMENT_SIZE
    y = random.randint(-(HEIGHT // 2 - 20) // SEGMENT_SIZE, (HEIGHT // 2 - 20) // SEGMENT_SIZE) * SEGMENT_SIZE
    food.goto(x, y)


# ── 3. Update the score display ────────────────────────────
def update_score(pen, score, high_score):
    pen.clear()
    pen.write(f"Score: {score}   High Score: {high_score}",
              align="center", font=("Courier", 14, "bold"))


# ── 4. Move the snake head one step ────────────────────────
def move(head):
    if head.direction == "up":
        head.sety(head.ycor() + SEGMENT_SIZE)
    elif head.direction == "down":
        head.sety(head.ycor() - SEGMENT_SIZE)
    elif head.direction == "left":
        head.setx(head.xcor() - SEGMENT_SIZE)
    elif head.direction == "right":
        head.setx(head.xcor() + SEGMENT_SIZE)


# ── 5. Direction control functions (bound to keys) ─────────
def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"


# ── 6. Detect wall collision ────────────────────────────────
def hit_wall(head):
    return (abs(head.xcor()) > WIDTH  // 2 - SEGMENT_SIZE // 2 or
            abs(head.ycor()) > HEIGHT // 2 - SEGMENT_SIZE // 2)


# ── 7. Detect self collision ────────────────────────────────
def hit_self(head, segments):
    for seg in segments:
        if seg.distance(head) < SEGMENT_SIZE:
            return True
    return False


# ── 8. Add a new body segment ──────────────────────────────
def add_segment():
    seg = turtle.Turtle()
    seg.shape("square")
    seg.color("green")
    seg.penup()
    return seg


# ── 9. Update body positions ───────────────────────────────
def update_body(head, segments):
    # Move each segment to the position of the segment ahead of it
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())


# ── 10. Reset after collision ───────────────────────────────
def reset_snake(head, segments):
    time.sleep(0.5)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)   # move off-screen
    segments.clear()


# ── Main game function ──────────────────────────────────────
def main():
    win       = setup_window()
    head      = create_head()
    food      = create_food()
    pen       = create_score_display()
    segments  = []
    score     = 0
    high_score = 0

    # Key bindings
    win.listen()
    win.onkeypress(lambda: go_up(head),    "Up")
    win.onkeypress(lambda: go_down(head),  "Down")
    win.onkeypress(lambda: go_left(head),  "Left")
    win.onkeypress(lambda: go_right(head), "Right")
    win.onkeypress(lambda: go_up(head),    "w")
    win.onkeypress(lambda: go_down(head),  "s")
    win.onkeypress(lambda: go_left(head),  "a")
    win.onkeypress(lambda: go_right(head), "d")

    update_score(pen, score, high_score)

    while True:
        win.update()

        # Wall collision
        if hit_wall(head):
            if score > high_score:
                high_score = score
            score = 0
            reset_snake(head, segments)
            update_score(pen, score, high_score)
            continue

        # Self collision
        if hit_self(head, segments):
            if score > high_score:
                high_score = score
            score = 0
            reset_snake(head, segments)
            update_score(pen, score, high_score)
            continue

        # Food eaten
        if head.distance(food) < SEGMENT_SIZE:
            place_food(food)
            segments.append(add_segment())
            score += 10
            update_score(pen, score, high_score)

        update_body(head, segments)
        move(head)
        time.sleep(DELAY)

    turtle.done()


if __name__ == "__main__":
    main()

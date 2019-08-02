import turtle
import time
import random

# Delay
dy = 0.1

# Screen

scr = turtle.Screen()
scr.title("Snake Game -Test1-")
scr.bgcolor("black")
scr.setup(width=600, height=600)
# Turns off the screen updates
scr.tracer(0)

# Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("gray")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Body stuff

seg = []

# Functions


def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard

scr.listen()
scr.onkeypress(go_up, "w")
scr.onkeypress(go_down, "s")
scr.onkeypress(go_left, "a")
scr.onkeypress(go_right, "d")

# Main game loop

while True:
    scr.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor(
    ) > 290 or head.ycor() < -290:
        time.sleep(0.8)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for sg in seg:
            sg.goto(1000, 1000)
        # Clear the segments list
        seg.clear()
    # Check for a collision
    if head.distance(food) < 20:
        # Move the food randomly
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Body stuff ( add a segment )
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        seg.append(new_seg)

    # Move the end segments first in reverse order
    for index in range(len(seg) - 1, 0, -1):
        x = seg[index - 1].xcor()
        y = seg[index - 1].ycor()
        seg[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(seg) > 0:
        x = head.xcor()
        y = head.ycor()
        seg[0].goto(x, y)

    move()
    time.sleep(dy)

scr.mainloop()
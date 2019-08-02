import turtle
import time
import random

# Delay
dy = 0.1

# Score

score = 0
high_score = 0

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

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0",
          align="center",
          font=("Courier", 24, "normal"))

# Functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
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
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for sg in seg:
            sg.goto(1000, 1000)
        # Clear the segments list
        seg.clear()

        # Reset dy

        dy = 0.1

        # Reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}    High Score {}".format(score, high_score),
                  align="center",
                  font=("Courier", 24, "normal"))
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

        # Dificulty ++
        dy -= 0.007

        # Score ++
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}    High Score {}".format(score, high_score),
                  align="center",
                  font=("Courier", 24, "normal"))

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

    # Colision with the body
    for sg in seg:
        if sg.distance(head) < 20:
            time.sleep(0.4)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for sg in seg:
                sg.goto(1000, 1000)
                # Clear the segments list
            seg.clear()

            # Reset dy

            dy = 0.1

            # Reset the score
            score = 0

            pen.clear()
            pen.write("Score: {}    High Score {}".format(score, high_score),
                      align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(dy)

scr.mainloop()
import turtle
import random

w = 500
h = 500
fs = 10
d = 100  # milliseconds

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global snake_game_with_python, kata, khanaT, pen
    snake_game_with_python = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    kata = "up"
    khanaT = nun()
    food.goto(khanaT)
    hall()

def hall():
    global kata

    new_head = snake_game_with_python[-1].copy()
    new_head[0] = snake_game_with_python[-1][0] + offsets[kata][0]
    new_head[1] = snake_game_with_python[-1][1] + offsets[kata][1]

    if new_head in snake_game_with_python[:-1]:  
        r()
    else:
        snake_game_with_python.append(new_head)

        if not khana():
            snake_game_with_python.pop(0)  

        if snake_game_with_python[-1][0] > w / 2:
            snake_game_with_python[-1][0] -= w
        elif snake_game_with_python[-1][0] < - w / 2:
            snake_game_with_python[-1][0] += w
        elif snake_game_with_python[-1][1] > h / 2:
            snake_game_with_python[-1][1] -= h
        elif snake_game_with_python[-1][1] < -h / 2:
            snake_game_with_python[-1][1] += h

        pen.clearstamps()
 #clears all the stamps

        for segment in snake_game_with_python:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
 #updates the turtle.screen screen

        turtle.ontimer(hall, d)

def khana():
    global khanaT
    if dist(snake_game_with_python[-1], khanaT) < 20:
        khanaT = nun()
        food.goto(khanaT)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    y = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def mathi():
    global kata
    if kata != "down":
        kata = "up"

def go_right():
    global kata
    if kata != "left":
        kata = "right"

def go_down():
    global kata
    if kata != "up":
        kata = "down"

def go_left():
    global kata
    if kata != "right":
        kata = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("snake_game_with_python")
screen.bgcolor("#144914")
screen.setup(500, 500)
screen.tracer(0)

pen = turtle.Turtle("circle")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(fs / 20) 
food.penup()

screen.listen()
screen.onkey(mathi, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

r()
turtle.done()

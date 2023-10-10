import turtle
import math
import random

def random_position():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    return x, y

def duplicat(num):
	return num * 2

num_turtles = 1
max_turtles = duplicat(num_turtles)
num_turtles = max_turtles
turtles = []

for i in range(num_turtles):
    t = turtle.Turtle()
    t.penup()
    t.goto(*random_position())
    turtles.append(t)

for t in turtles:
    t.goto(*random_position())

turtle.done()

import turtle
import math
import random

def random_position():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    return x, y

def duplicat(num):
	num_turtles = num
	return num * 2

num_turtles = duplicat(2)
turtles = []
gen = 0

def creat_new_turtle():
	global turtles
	repete = len(turtles)
	for i in range(repete*2):
		t = turtle.Turtle()
		t.penup()
		t.goto(*random_position())
		turtles.append(t)

while True:
    for t in turtles:
        t.goto(*random_position())
	
	if gen % 2 == 0:
		create_new_turtles()
		
turtle.done()


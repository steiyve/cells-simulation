import turtle
import math
import random


def random_position():
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    return x, y

def duplicat(num):
	num_turtles = num
	return num * 2

num_turtles = duplicat(2)
turtles = []
gen = 0

for i in range(2):
		t = turtle.Turtle()
		t.color("green")
		t.shape("circle")
		t.begin_fill()
		t.name = f"normal"
		#mutation
		if random.randint(0,20) == 20:
			t.color("red")
			t.name = f"mutated"
			if random.randint(0,2) == 2:
				t.name = f"mutated-infectious"

		t.penup()
		
		t.goto(*random_position())
		turtles.append(t)

def creat_new_turtle():
	global turtles
	repete = len(turtles)
	for i in range(repete*2):
		t = turtle.Turtle()
		t.shape("circle")
		t.color("green")
		t.begin_fill()
		t.name = f"normal"
		#mutation
		if random.randint(0,20) == 20:
			t.color("red")
			t.name = f"mutated"
			if random.randint(0,2) == 2:
				t.name = f"mutated-infectious"
		t.penup()
		
		t.goto(*random_position())
		turtles.append(t)

def find_nearest_turtle(target_turtle, turtles):
    nearest_turtle = None
    min_distance = float('inf')

    for t in turtles:
        if t == target_turtle:
            continue
        dx = t.position()[0] - target_turtle.position()[0]
        dy = t.position()[1] - target_turtle.position()[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance < min_distance:
            min_distance = distance
            nearest_turtle = t

    return nearest_turtle

while True:

	if gen % 10 == 0:
		creat_new_turtle()
	for t in turtles:
		if t.name == "mutated-infectious":
			for i in turtles:
				if i.name == "normal":
					nearest_turtle = find_nearest_turtle(i, t)
					if random.randint(0,3) == 2:
						nearest_turtle.color("black")
						nearest_turtle.name = f"dead"
						print("dead")

 


		
	gen += 1
turtle.done()


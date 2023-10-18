import turtle
import math
import random


def random_position():
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    return x, y


bg = turtle.Screen()
bg.bgcolor("black")
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
		
		t.goto(0,0)
		turtles.append(t)

def creat_new_turtle():
	global turtles
	for i in range(2):
		t = turtle.Turtle()
		t.color("green")
		t.shape("circle")
		t.begin_fill()
		t.speed(0)
		t.name = f"normal"
		#mutation
		if random.randint(0,20) == 20:
			t.color("red")
			t.name = f"mutated"
			if random.randint(0,2) == 2:
				t.name = f"mutated-infectious"
		t.penup()
		print(t.name)

		t.goto(*random_position())
		turtles.append(t)

while True:

	for t in turtles:
		if t.name == "normal" or t.name == "mutated":
			if gen % 10 == 0:
				creat_new_turtle()
				print("penis")

		
		elif t.name == "mutated-infectious":
			print("penis")
			for i in turtles:
				print("penis")
				if i.name == "normal" or t.name == "mutated" or t.name == "mutated-infectious":
					if random.randint(0,3) == 2:
						i.color("black")
						i.name = f"dead"
						print("dead")
	
	#verifier la taille de la population
	if len(turtles) >= 300:
		break



		
	gen += 1
turtle.done()


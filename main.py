import turtle
import random

#fonction qui retourne une position
def random_position():
    x = random.randint(-600, 600)
    y = random.randint(-600, 600)
    return x, y


bg = turtle.Screen()
turtles = []
gen = 0

#creer les premiere tortue
for i in range(2):
	        #attribut de la tourtue
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

#duplication de la cellule
def mitose():
	global turtles
	for i in range(2):
		#attribut de la fonction
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
		#si tortue est normal ou mutante non infectieuse
		if t.name == "normal" or t.name == "mutated":
			#tout les 10 gen
			if gen % 10 == 0:
				mitose()

		
		elif t.name == "mutated-infectious":
			for i in turtles:
				#si tortue est normal ou mutante ou mutante infectieuse
				#peit mourrir
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

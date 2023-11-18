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
	chance = random.randint(0,20)

	if chance == 20:
		t.color("red")
		t.name = f"mutated"

		maladie = random.randint(0,3)
		if maladie == 1:
			t.name = f"cancer"
			type_cancer = random.randint(0,100)
			if type_cancer % 10 == 0:
				t.name = f"leucemie"
				t.color("white")

			if 0 <= type_cancer <= 2:
				t.name = f"melanome"
				t.color("blue")

		if maladie == 2:
			t.name = f""
			t.color("blue")

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
		
	chance = random.randint(0,20)

	if chance == 20:
		t.color("red")
		t.name = f"mutated"

		maladie = random.randint(0,3)
		if maladie == 1:
			type_cancer = random.randint(0,100)
			if type_cancer % 10 == 0:
				t.name = f"leucemie"
				t.color("white")

			if 0 <= type_cancer <= 2:
				t.name = f"melanome"
				t.color("blue")

		if maladie == 2:
			t.name = f""
			t.color("blue")
		
		t.penup()
		print(t.name)

		t.goto(*random_position())
		turtles.append(t)

while True:
	for t in turtles:
		#si tortue est normal ou mutante non infectieuse
		if t.name == "normal" or t.name == "leucemie" or t.name == "melanome":
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

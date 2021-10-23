#AYMEN DEV 

import turtle

def draw_drapo(taille,couleur):
	
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color(couleur)
	brad.speed(1)
	brad.width(13)
	brad.goto(-150,0)

	i=0
	while i < 5:	
		brad.forward(300)
		brad.right(180*4/5)
		
		i+=1
	brad.ht()
	#brad.end_fill()	

window = turtle.Screen()
window.bgcolor("red")
window.title("Morocco-المغرب" )
draw_drapo(250,"green")

window.exitonclick()

from turtle import Turtle, Screen
import random


timi_turtle=Turtle()
# turtle draws dashed line
for _ in range(50):
    timi_turtle.forward(10)
    timi_turtle.penup()
    timi_turtle.forward(10)
    timi_turtle.pendown()
# turtle draws different shapes
color=["red","green","blue","medium aquamarine","dark sea green","violet","firebrick","purple"]
side=3
while side<11:
    timi_turtle.pencolor(random.choice(color))
    for _ in range(side):
        timi_turtle.right(360/side)
        timi_turtle.forward(100)
    side+=1
    



screen=Screen()
screen.exitonclick()
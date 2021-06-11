from turtle import Turtle,Screen
import random
import turtle
tim = Turtle()
turtle.colormode(255)
tim.speed(10)
tim.pensize(width="10")
def random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   my_tuple=(r,b,g)
   return my_tuple

turn=[0,90,180,270,360]
for _ in range(500):
    tim.pencolor(random_color())
    tim.forward(20)
    tim.right(random.choice(turn))






screen=Screen()
screen.exitonclick()
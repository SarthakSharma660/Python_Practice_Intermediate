import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
def random_color():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   my_tuple=(r,b,g)
   return my_tuple


for _ in range(45):
    tim.color(random_color())
    tim.circle(100)
    tim.forward(1)
    tim.degrees(90)
    tim.right(2)

#Alternative way of doing the question

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)







screen=t.Screen()
screen.exitonclick()
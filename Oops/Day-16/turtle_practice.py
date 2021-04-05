from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("firebrick","firebrick1")
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
my_screen=Screen()
print(my_screen.screensize())
my_screen.exitonclick()


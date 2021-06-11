import random
from turtle import Turtle,Screen

is_race_on=False
sc=Screen()
sc.bgcolor("black")
sc.setup(width=600,height=600)
user_bet=sc.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a color: ")
colours=["red","orange","yellow","green","white","purple"]
y_pos=[-100,-60,-20,20,60,100,]
all_turtle=[]
for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-290,y=y_pos[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on=True

while is_race_on :
    for turtle in all_turtle:
        if turtle.xcor()>280:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_bet== winning_color:
                print(f"You've won! The {winning_color} turtle won the race!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race!")
        turtle.forward(random.randint(0,10))
 



sc.exitonclick()
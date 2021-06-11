# import colorgram

# colors = colorgram.extract('Day-18/hirst/img.jpg',30)
# color_list=[]
# for colour in colors:
#     r=colour.rgb.r
#     g=colour.rgb.g
#     b=colour.rgb.b
#     my_color=(r,g,b)    
#     color_list.append(my_color)

# print(color_list)
import random
import turtle as t


Colors_list=[(231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226), (30, 110, 159), (235, 81, 44), (215, 222, 228), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144), (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68), (227, 171, 162), (73, 135, 188), (172, 204, 174)]
screen=t.Screen()
t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
for i in range(10):
    for _ in range(10) :
        tim.fd(50)
        tim.color(Colors_list[random.randint(0,len(Colors_list)-1)])
        tim.dot(20)
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(500)
    tim.setheading(0)












screen.exitonclick()
import turtle as t


tim=t.Turtle()
sc=t.Screen()
sc.listen()


def fwd():
    return tim.fd(20)

def move_back():
    return tim.backward(20)

def turn_right():
    return tim.right(15)

def turn_left():
    return tim.left(15)

def clear():
    return tim.reset()


sc.onkey(key='w',fun = fwd)
sc.onkey(key='s',fun = move_back)
sc.onkey(key='d',fun = turn_left)
sc.onkey(key='a',fun = turn_right)
sc.onkey(key='c',fun = clear)










sc.exitonclick()
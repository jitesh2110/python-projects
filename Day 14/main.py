#etch-A-sketch 
from turtle import Turtle,Screen

rock = Turtle()
screen = Screen()
screen.listen()

def forward():
    rock.fd(10)
def backward():
    rock.back(10)
def right():
    rock.right(10)
def left():
    rock.left(10)
def clear():
    rock.reset()


screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun = backward)
screen.onkey(key='a',fun=left)
screen.onkey(key='d',fun=right)
screen.onkey(key='c',fun=clear)


screen.exitonclick()

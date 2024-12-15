from random import randint
from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)

rock = Turtle()
my_screen = Screen()


def color():
    r=randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour
rock.shape("turtle")
rock.color("red")
rock.hideturtle()
i=360
rock.speed(0)
rock.width(2)
rock.penup()
my_screen.screensize(700,700)
rock.setposition(-300,-300)
for x in range(0,10):
    for y in range(0,10):
        rock.dot(20,color())
        rock.forward(50)

    rock.back(500)
    rock.left(90)
    rock.fd(50)
    rock.right(90)

my_screen.exitonclick()

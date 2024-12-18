from turtle import Turtle
import pandas

class Pen:
    def __init__(self):
        pass

    def update(self,name):
        data =pandas.read_csv("50_states.csv")
        x = int(data[data.state == name].x)
        y = int(data[data.state == name].y)
        n = Turtle()
        n.penup()
        n.hideturtle()
        n.goto(x,y)
        n.write(name,font=('Arial',8,'bold'))
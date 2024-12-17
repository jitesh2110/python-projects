from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(0,0)
        self.direction = randint(0, 360)
        self.setheading(self.direction)
        self.flow()

    def flow(self):
        self.fd(10)
    def changex(self):
        self.setheading(360-self.heading())
    def changey(self):
        self.setheading((180-self.heading())%360)






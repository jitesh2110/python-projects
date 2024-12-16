import turtle
from random import randint

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.refresh()
    def refresh(self):
        self.x = randint(-280,280)
        self.y = randint(-280,280)
        self.penup()
        self.goto(self.x, self.y)

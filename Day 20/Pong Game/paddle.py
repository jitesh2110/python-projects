from turtle import  Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(4,1)
        self.color('white')
        self.penup()

    def paddle1(self):
        self.goto(-380,0)
    def paddle2(self):
        self.goto(380,0)
    def moveup(self):
        if self.ycor()<280:
            self.sety(self.ycor()+15)

    def down(self):
        if self.ycor() > -280:
            self.sety(self.ycor()-15)









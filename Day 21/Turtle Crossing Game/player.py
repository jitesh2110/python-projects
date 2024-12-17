from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto_start()
        self.setheading(90)
    def move(self):
        self.fd(10)

    def at_finish_line(self):
        if self.ycor() > 280:
         return True
    def goto_start(self):
        self.goto(0,-280)
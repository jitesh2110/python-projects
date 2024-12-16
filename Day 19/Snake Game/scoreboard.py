from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color('white')
        self.s=0
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score: {self.s}",False,'center',("Arial",13,'normal'))
    def over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, 'center', ("Arial", 13, 'bold'))

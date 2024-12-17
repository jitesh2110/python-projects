from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250,270)
        self.write(f"Level: {self.level}",False,'left',("Arial",15,"bold"))
    def update(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", False, 'left', ("Arial", 15, "bold"))

    def over(self):
        self.goto(-80,0)
        self.write(f"GAME OVER!", False, 'left', ("Arial", 25, "bold"))
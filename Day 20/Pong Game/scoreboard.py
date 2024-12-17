from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.x =pos_x
        self.y =pos_y
        self.goto(self.x,self.y)
        self.pendown()
        self.score =0
        self.write(f"{self.score}",False,font=("Arial",20,'bold'))

    def update(self):
        self.clear()
        self.score+=1
        self.write(f"{self.score}",False,font=("Arial",20,'bold'))
    def over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",False,font=("Arial",20,'bold'))


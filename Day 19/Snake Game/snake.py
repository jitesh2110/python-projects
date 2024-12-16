from turtle import Turtle

class Snake():
    def __init__(self):
        self.body = []

    def add(self):
        snake1 = Turtle(shape='square')
        snake1.color("white")
        snake1.penup()
        self.body.append(snake1)
        lenght = len(self.body)
        x = self.body[lenght - 1].xcor() - 20
        y = self.body[lenght - 1].ycor()
        snake1.goto(x=x, y=y)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)

        self.body[0].fd(20)

    def turn_right(self):
        self.body[0].right(90)
    def turn_left(self):
        self.body[0].left(90)

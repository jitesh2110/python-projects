COLORS = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

from turtle import Turtle
from random import randint,choice

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.cars =[]
    def createcar(self):
        chance = randint(1,6)
        if chance== 1:
            new_car =Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(1,2)
            y =randint(-250,250)
            new_car.goto(300,y)
            self.cars.append(new_car)

    def movecar(self):
        for car in self.cars:
            car.back(10)

    def level_up(self):
        self.speed+=5

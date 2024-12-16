import random
from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=400)
screen.listen()
rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
user = screen.textinput(title="Make a bet!",prompt="Choose a color of turtle from rainbow: ").title()
racers = []
y=-90
for i in range(0,7):
    rocki =Turtle(shape="turtle")
    rocki.color(rainbow_colors[i])
    rocki.penup()
    rocki.goto(x=-240,y=y)
    y = y+30
    racers.append(rocki)


def race():
    on = True
    while on:
        for i in racers:
            i.forward((random.randint(0,10)))
            if i.xcor() >= 230:
                return i.pencolor()

winner = race()
if winner == user:
    print("You Won!")
else:
    print("You Lost!")
    print(f"winner is {winner}")


screen.exitonclick()

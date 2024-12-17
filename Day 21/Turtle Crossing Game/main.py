from turtle import Screen
from time import sleep
from player import Player
from carmanager import CarManager
from scoreboard import ScoreBoard

screen =Screen()
screen.setup(600,600)
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.onkey(player.move,'space ')
game = True
while game:
    screen.update()
    sleep(0.1)

    car_manager.createcar()
    car_manager.movecar()
    for car in car_manager.cars:
        if player.distance(car)<20:
            scoreboard.over()
            game = False
    if player.at_finish_line():
        car_manager.level_up()
        player.goto_start()
        scoreboard.update()

screen.exitonclick()

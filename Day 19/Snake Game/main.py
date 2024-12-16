from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
food = Food()
score = ScoreBoard()
snake = Snake()
snake.add()
snake.add()
snake.add()

screen.onkey(snake.turn_right, 'd')
screen.onkey(snake.turn_left, 'a')
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.body[0].distance(food)<15:
        food.refresh()
        score.s+=1
        score.update()
        snake.add()
    if snake.body[0].xcor()>290 or snake.body[0].xcor()<-290 or snake.body[0].ycor()>290 or snake.body[0].ycor()<-290:
        game = False
        score.over()
        print("game over!")
    for i in snake.body:
        if i == snake.body[0]:
            pass
        elif i.distance(snake.body[0])<10:
            game =False
            score.over()
            print("game over")


screen.exitonclick()


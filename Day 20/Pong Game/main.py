from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.title("Pong")

paddle1 = Paddle()
paddle2 = Paddle()
paddle1.paddle1()
paddle2.paddle2()

p1u = p1d = p2u =p2d = False

def move():
    if p1u:
        paddle1.moveup()
    if p1d:
        paddle1.down()
    if p2u:
        paddle2.moveup()
    if p2d:
        paddle2.down()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.changex()
    if ball.distance(paddle1)<35 or ball.distance(paddle2)<35:
        ball.changey()
    if ball.xcor()>400:
        ball.refresh()
        scoreL.update()
        if scoreL.score>=2:
            scoreL.over()
            return
    if ball.xcor()>400 or ball.xcor()<-400:
        ball.refresh()
        scoreR.update()
        if scoreR.score>=2:
            scoreR.over()
            return


    screen.update()
    screen.ontimer(move,20)
    screen.ontimer(ball.flow,20)

def paddle1_moveup():
    global p1u
    p1u = True
def paddle1_down():
    global p1d
    p1d = True
def paddle2_moveup():
    global p2u
    p2u = True
def paddle2_down():
    global p2d
    p2d = True
def paddle1_stop():
    global p1u,p1d
    p1u = p1d = False
def paddle2_stop():
    global p2u,p2d
    p2u = p2d = False


screen.onkeypress(paddle1_moveup,'w')
screen.onkeyrelease(paddle1_stop,'w')
screen.onkeypress(paddle1_down,'s')
screen.onkeyrelease(paddle1_stop,"s")


screen.onkeypress(paddle2_moveup, 'Up')
screen.onkeyrelease(paddle2_stop, 'Up')
screen.onkeypress(paddle2_down, 'Down')
screen.onkeyrelease(paddle2_stop, 'Down')

ball = Ball()
scoreL = ScoreBoard(pos_x=-200,pos_y=250)
scoreR = ScoreBoard(pos_x=200,pos_y=250)

move()



screen.exitonclick()

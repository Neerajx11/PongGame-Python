from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

leftPaddle = Paddle((-350, 0))
rightPaddle = Paddle((350, 0))

screen.listen()

screen.onkey(rightPaddle.moveUp, "Up")
screen.onkey(rightPaddle.moveDown, "Down")
screen.onkey(leftPaddle.moveUp, "w")
screen.onkey(leftPaddle.moveDown, "s")

ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # detect collision with r_paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # right paddle miss
    if ball.xcor() > 380:
        ball.reset()
        score.lPoint()

    # left paddle miss
    if ball.xcor() < -380:
        ball.reset()
        score.rPoint()

screen.exitonclick()

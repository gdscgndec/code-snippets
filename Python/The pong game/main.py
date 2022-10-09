from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #right paddle misses
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    #left paddle missed
    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
from math import gamma
from turtle import Screen
from  paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "a")
screen.onkeypress(left_paddle.down, "z")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()


#detect collision with wall
    if ball.ycor() > 280 and ball.xcor() > 0:
        ball.y_bounce()
    elif ball.ycor() < -280 and ball.xcor() > 0:
        ball.y_bounce()
    elif ball.ycor() > 280 and ball.xcor() < 0:
       ball.y_bounce()
    elif ball.ycor() < -280 and ball.xcor() < 0:
        ball.y_bounce()

    #detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.move_speed *= 0.9
        ball.setx(340)
        ball.x_bounce()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.move_speed *= 0.9
        ball.setx(-340)
        ball.x_bounce()

    #detct when paddle misses
    if ball.xcor() > 380 and ball.distance(right_paddle) > 49:
        print(f"Right loses")
        scoreboard.update_left()
        print(scoreboard.l_score)
        ball.reset_ball("x")
    elif ball.xcor() < -380 and ball.distance(left_paddle) > 49:
        print("Left loses")
        scoreboard.update_right()
        print(scoreboard.r_score)
        ball.reset_ball("y")


screen.exitonclick()
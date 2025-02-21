from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Calling imported classes
snake = Snake()
food = Food()
score = Score()

# Listen to key clicks
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Collison with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        score.reset_score()
        snake.resett()

    #Collision with the body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            score.reset_score()
            snake.resett()






screen.exitonclick()
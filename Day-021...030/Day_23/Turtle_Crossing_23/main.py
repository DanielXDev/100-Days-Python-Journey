from turtle import Screen
from cars import CarManager
from turt import Player
from notify import Notify
import time




screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



cars = CarManager()
player = Player()
notify = Notify()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")




is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            notify.game_over()

    #detect crossing
    if player.ycor() == 280:
        notify.clean()
        player.start_over()
        cars.leve_up()

screen.exitonclick()
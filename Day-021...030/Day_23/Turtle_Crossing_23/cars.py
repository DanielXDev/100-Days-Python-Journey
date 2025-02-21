from turtle import Turtle
import random

COLORS = ["yellow", "blue", "red", "black", "green", "purple"]
MOVING_DISTANCE = 5
INCREMENT = 5

class CarManager:
    def __init__(self):
       self.all_cars = []
       self.speed = MOVING_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            new_car.goto(310, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def leve_up(self):
        self.speed += INCREMENT
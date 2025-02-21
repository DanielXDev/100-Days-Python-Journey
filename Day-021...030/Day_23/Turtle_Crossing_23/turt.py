from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.seth(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def start_over(self):
        self.goto(0, -280)

import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.y_cor = None
        self.speed("fastest")
        self.cord = cord
        self.create_paddle()

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len= 1, stretch_wid= 5)
        self.penup()
        self.goto(self.cord)
        
    def up(self):
        self.y_cor = self.ycor() + 20
        if self.y_cor < 270:
            self.goto(x=self.xcor(),y=self.y_cor)
        
    def down(self):
        self.y_cor = self.ycor() - 20
        if self.y_cor > -270:
            self.goto(x=self.xcor(), y=self.y_cor)   
    
        
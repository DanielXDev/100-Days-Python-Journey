from pickletools import UP_TO_NEWLINE
from tkinter.constants import RIGHT
from turtle import Turtle
STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")

        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.create_segment(position)
        
           

    def create_segment(self, position):
        snake_box = Turtle(shape="square")
        snake_box.color("white")
        snake_box.shapesize(stretch_wid=0.5, stretch_len=0.5)
        snake_box.penup()
        snake_box.speed("fastest")
        snake_box.goto(position)
        self.segments.append(snake_box)

    def resett(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")

    def extend(self):
        #create new segment
        self.create_segment(self.segments[-1].pos())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
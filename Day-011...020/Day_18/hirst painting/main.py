import turtle as t
from turtle import Screen
import random


color_list = [(140, 165, 192), (211, 155, 116), (23, 37, 56), (192, 142, 152), (60, 102, 134), (148, 69, 58), (231, 212, 107), (143, 177, 162), (141, 68, 77), (145, 28, 35), (46, 36, 32), (46, 32, 37), (66, 110, 96), (33, 51, 46), (135, 32, 27), (227, 168, 174), (234, 169, 161), (186, 98, 107), (194, 95, 82), (175, 188, 216), (18, 92, 69), (110, 124, 158), (33, 61, 105), (173, 203, 193), (21, 79, 98), (60, 149, 185)]

ash = t.Turtle()
t.colormode(255)
x = -230
y = -230
ash.hideturtle()
# ash.setpos(x, y)

def move_pos():
    ash.speed("fastest")
    ash.penup()
    ash.setpos(x, y)
    ash.pendown()
move_pos()

for n in range(10):
    for _ in range(10):
        ash.speed("fast")
        ash.dot(20, random.choice(color_list))
        ash.penup()
        ash.fd(50)
        ash.pendown()

    y += 50
    move_pos()






screen = Screen()
screen.exitonclick()

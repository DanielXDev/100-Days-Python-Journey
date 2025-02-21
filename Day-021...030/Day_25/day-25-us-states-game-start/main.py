import turtle
import time
from show import Show

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. State Game")
screen.setup(height=492)
# screen.tracer(0)



show = Show()




screen.exitonclick()
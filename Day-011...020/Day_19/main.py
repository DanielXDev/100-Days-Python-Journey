from turtle import Turtle, Screen


charles = Turtle()
screen = Screen()

def foward():
    charles.forward(20)

def backward():
    charles.backward(20)

def anti_clockwise():
    charles.left(30)

def clockwise():
    charles.right(30)



screen.listen()
screen.onkey(key="w", fun=foward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=charles.reset)




screen.exitonclick()
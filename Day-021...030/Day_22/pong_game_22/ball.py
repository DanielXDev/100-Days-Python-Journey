from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("slow")
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        self.x_cor = self.xcor() + self.x_move
        self.y_cor = self.ycor() + self.y_move
        self.goto(self.x_cor, self.y_cor)
    
    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset_ball(self, b_pos):
        self.reset()
        self.__init__()
        if b_pos == "x":
            self.x_bounce()

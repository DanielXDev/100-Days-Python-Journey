from turtle import Turtle

class Notify(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_b()

    def score_b(self):
        self.goto(-250, 280)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 14, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 18, "normal"))

    def clean(self):
        self.clear()
        self.score += 1
        self.score_b()

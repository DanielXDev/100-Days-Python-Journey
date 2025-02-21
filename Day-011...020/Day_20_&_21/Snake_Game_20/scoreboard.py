from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 275)
        self.score = 0
        self.write_score(self.score)


    def write_score(self, count):
        self.write(arg=f"Score: {count}   HighScore: {self.read_highscore()}", move=True, align=ALIGNMENT, font=FONT)

    def read_highscore(self):
        self.penup()
        with open("data.txt", mode="r") as data:
            read = int(data.read())
            highscore = read
        return highscore

    def edit_highscore(self, high):
        self.penup()
        with open("data.txt", mode="w") as data:
            data.write(str(high))

    def reset_score(self):
        if self.score > self.read_highscore():
            self.edit_highscore(self.score)
        self.undo()
        self.score = 0
        self.write_score(self.score)
        
    def increase_score(self):
        self.score += 1
        self.undo()
        self.write_score(self.score)



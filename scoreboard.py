from turtle import Turtle
FONT = ("Courier", 28, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f'{self.r_score}', align=ALIGNMENT, font=FONT)

    def lPoint(self):
        self.l_score += 1
        self.updateScore()

    def rPoint(self):
        self.r_score += 1
        self.updateScore()

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        self.xAdder = 10
        self.yAdder = 10
        self.moveSpeed = 0.1
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        bxcor = self.xcor()+self.xAdder
        bycor = self.ycor()+self.yAdder
        self.goto(bxcor, bycor)

    def bounceY(self):
        self.yAdder *= -1
        self.moveSpeed *= 0.9

    def bounceX(self):
        self.xAdder *= -1
        self.moveSpeed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.fast = 0
        self.xAdder *= -1

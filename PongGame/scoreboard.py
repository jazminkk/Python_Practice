import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.renew()

    def renew(self):
        self.clear()
        self.setpos(-100, 250)
        self.write(f"Score : {self.l_score}", move=False, align='left', font=('Arial', 20, 'normal'))
        self.setpos(100, 250)
        self.write(f"Score : {self.r_score}", move=False, align='left', font=('Arial', 20, 'normal'))

    def add_l_score(self):
        self.l_score += 1
        self.renew()

    def add_r_score(self):
        self.r_score += 1
        self.renew()

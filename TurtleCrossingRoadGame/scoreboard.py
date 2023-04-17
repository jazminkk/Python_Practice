from turtle import Turtle
import emoji
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.level = 1
        self.renew()

    def renew(self):
        self.clear()
        self.setpos(-250, 270)
        self.write(f"LEVEL: {self.level}, SCORE: {self.score}", move=False, align='left', font=FONT)

    def add_score(self):
        self.score += 1
        self.level += 1
        self.renew()

    def game_over(self):
        self.setpos(-210, 0)
        face = "\U0001F929"
        self.write(f"GAME OVER!! AT LEVEL {self.level}.{face}", move=False, align='left', font=FONT)

from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.setpos(0, 230)
        self.pencolor("white")
        self.renew()

    def renew(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.renew()

    def add_score(self):
        self.score += 1
        self.renew()

    def read_high_score(self):
        with open("./score_data.txt", mode='r') as f:
            self.high_score = int(f.read())

    def save_high_score(self):
        with open("./score_data.txt", mode='w') as f:
            f.write(str(self.high_score))



"""
    def game_over(self):
        self.penup()
        self.setpos(0, 0)
        self.write("Game over", move=False, align=ALIGNMENT, font=FONT)
"""
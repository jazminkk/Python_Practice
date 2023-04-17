from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 230)
        self.pencolor("white")
        self.write(f"score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def renew(self):
        self.clear()
        self.score += 1
        self.write(f"score = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.setpos(0, 0)
        self.write("Game over", move=False, align=ALIGNMENT, font=FONT)

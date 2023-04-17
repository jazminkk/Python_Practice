from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_pos = x_position
        self.y_pos = y_position
        self.x_gap = 10
        self.y_gap = 10
        self.ball_speed = 0.1
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setpos(self.x_pos, self.y_pos)

    def move(self):
        self.x_pos += self.x_gap
        self.y_pos += self.y_gap
        self.setpos(self.x_pos, self.y_pos)

    def bounce_from_wall(self):
        self.y_gap *= -1

    def bounce_from_paddle(self):
        self.x_gap *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.x_pos = 0
        self.y_pos = 0
        self.x_gap *= -1
        self.ball_speed = 0.1

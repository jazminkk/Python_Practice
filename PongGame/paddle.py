from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.x_pos = x_position
        self.y_pos = y_position
        self.penup()
        self.shape("square")
        self.color("deep pink")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(self.x_pos, self.y_pos)

    def move_up(self):
        self.y_pos += 20
        self.setpos(self.x_pos, self.y_pos)

    def move_down(self):
        self.y_pos -= 20
        self.setpos(self.x_pos, self.y_pos)

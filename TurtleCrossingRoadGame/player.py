from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("deep pink")
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.ready()

    def move_up(self):
        self.setpos(0, self.ycor() + MOVE_DISTANCE)

    def ready(self):
        self.setpos(STARTING_POSITION)

    def has_reached(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.ready()
            return True
        return False


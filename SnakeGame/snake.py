from turtle import Screen, Turtle

TURTLE_SIZE = 20
SNAKE_INIT_LENGTH = 3
# INIT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
INIT_POSITION = [(part * -TURTLE_SIZE, 0) for part in range(SNAKE_INIT_LENGTH)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in INIT_POSITION:
            self.add_segment(position)
        # print(self.snake_body[0])

    def add_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("deep pink")
        snake_part.penup()
        snake_part.setpos(position)
        # print(snake_part)
        self.snake_body.append(snake_part)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            # new_x = self.snake_list[part-1].xcor()
            # new_y = self.snake_list[part-1].ycor()
            new_pos = self.snake_body[i - 1].pos()
            self.snake_body[i].goto(new_pos)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_body[-1].pos())

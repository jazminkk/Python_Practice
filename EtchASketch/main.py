from turtle import Turtle, Screen
import turtle

turtle_a = Turtle()
screen = Screen()
turtle_a.color("deep pink")


def move_forwards():
    turtle_a.forward(10)


def move_backwards():
    turtle_a.backward(10)


def counter_clockwise():
    turtle_a.left(10)


def clockwise():
    turtle_a.right(10)


def clear_drawing():
    turtle_a.reset()
    turtle_a.color("deep pink")


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
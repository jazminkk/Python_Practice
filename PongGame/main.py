from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
# screen.tracer(1)
ball = Ball(0, 0)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)
    if ball.x_pos == 330 and ball.distance(right_paddle) <= 50:
        ball.bounce_from_paddle()
    if ball.x_pos == -330 and ball.distance(left_paddle) <= 50:
        ball.bounce_from_paddle()
    if ball.y_pos > 280 or ball.y_pos < -280:
        ball.bounce_from_wall()
    if ball.x_pos > 370:
        scoreboard.add_l_score()
        ball.reset_position()
    if ball.x_pos < -370:
        scoreboard.add_r_score()
        ball.reset_position()


screen.exitonclick()

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)    # Close a tracer, not display real time

# Create a snake body
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Snake move
game_is_on = True
while game_is_on:
    screen.update()  # display
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        score.renew()
        snake.extend()

    # Detect collision with wall
    head = snake.snake_body[0]
    if head.xcor() < -230 or head.xcor() > 230 or head.ycor() < -230 or head.ycor() > 230:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if segment.distance(head) < 15:
            game_is_on = False
            score.game_over()


screen.exitonclick()

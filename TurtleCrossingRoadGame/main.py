import time
from turtle import Screen, Turtle
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")
level = 0
counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter % 6 == 0:
        car_manager.add_car()
    car_manager.move_cars()
    car_manager.remove_car(screen)
    if car_manager.has_collision(player):
        game_is_on = False
        scoreboard.game_over()
    if player.has_reached():
        scoreboard.add_score()
        car_manager.level_up()


screen.exitonclick()

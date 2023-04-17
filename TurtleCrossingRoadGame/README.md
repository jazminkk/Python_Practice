"""TurtleCrossingGame"""
--
# Goal:

## It's a game use the keypress "Up" and let turtle cross traffic lanes to reach the finish line.
## When turtle reach it, player's score will be a plus and cars will speed up. 

# requirement:

## 1. Move the turtle with keypress "Up".
## 2. Create and move the cars.
## 3. Detect collision with car.
## 4. Detect when turtle reaches the other side.
## 5. Create a scoreboard and renew play's grade and level.

# class:
### 1. Player(turtle):
* ready: at the bottom and ready to start. 
* move_up: move with keypress only "Up"
* has_reached: Detect turtle on the top.
### 2. Car
* move:Move at the setting of speed level
* delete_car:When car is out of screen, delete the car item.
### 3. CarManager
* add_car:Add a car Every six times
* move_cars:
* has_collision:Detect collision.
* remove_car:When car is out of screen, remove the car from car's list.
### 4. Scoreboard
* renew:Renew score.
* add_score:Add score.
* game_over:Print game_over.

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Car()
        self.car_list.append(car)

    def move_cars(self):
        for item in self.car_list:
            item.move(self.cars_speed)

    def has_collision(self, player):
        for item in self.car_list:
            if item.distance(player) <= 20:
                return True
        return False

    # some bugs QAQ. cannot clear those cars that out of range.
    def remove_car(self, screen):
        for item in self.car_list:
            if item.x_pos <= -340:
                item.delete_car()
                self.car_list.remove(item)
                idx = screen.turtles().index(item)
                screen.turtles().pop(idx)
        # print(len(self.car_list), len(screen.turtles()))

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.car_color = random.choice(COLORS)
        self.color(self.car_color)
        self.penup()
        self.x_pos = 300
        self.y_pos = random.randint(-250, 250)
        self.setpos(self.x_pos, self.y_pos)

    def move(self, cars_speed):
        self.x_pos -= cars_speed
        self.setpos(self.x_pos, self.y_pos)

    def delete_car(self):
        self.hideturtle()
        self.clear()

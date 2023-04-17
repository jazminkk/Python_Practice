from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Turtle Coordinate Guess Game")
screen.setup(width=500, height=500)
screen.bgcolor("light cyan")

user_guess = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? \n [red, orange, yellow, green, blue, purple]\n Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# end line
judge = Turtle()
judge.hideturtle()
judge.speed("fastest")
judge.penup()
judge.setpos(230, -250)
judge.color("deep pink")
judge.pendown()
# heading E = 0, N = 90, W=180, S = 270
judge.setheading(90)
judge.forward(500)

# msg
msg = Turtle()
msg.hideturtle()
msg.penup()
msg.setpos(0, 50)
msg.color("deep pink")

is_race_start = False
y_position = [gap*50 for gap in range(6)]

# create turtles
turtle_list = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setpos(-230, -160 + y_position[i])
    turtle_list.append(new_turtle)

if user_guess:
    is_race_start = True

# race start
while is_race_start:
    for t in turtle_list:
        move_distance = random.randint(1, 10)
        t.forward(move_distance)
        # one turtle finished
        if t.xcor() > 230:
            is_race_start = False
            winning_color = t.pencolor()
            msg.color(winning_color)
            msg.pendown()
            if winning_color == user_guess:
                msg.write(f"You've won!\nThe {winning_color} turtle is the winner.\n", align="center", font=('Arial', 20, 'normal'))
            else:
                msg.write(f"You've lost!\nThe {winning_color} turtle is the winner.\n", align="center", font=('Arial', 20, 'normal'))
            # print(user_msg)
            # if user_msg == "no":
            #     screen.bye()

screen.exitonclick()




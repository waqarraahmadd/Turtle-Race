from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
user_guess = screen.textinput("Make a bet", "Who will win the race? Enter a color:")
screen.setup(width=500, height=400)
colors = ["Blue", "Cyan", "Pink", "Red", "Green", "Yellow", "Purple"]
y_axis = [-80, -50, -20, 10, 40, 70]

turtle_list = []


for num in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_axis[num])
    new_turtle.speed("fastest")
    turtle_list.append(new_turtle)


if user_guess:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() >= 200:
            is_race_on = False
            winner = turtle.pencolor()
            print(f"{winner} won the race")
            if user_guess == winner:
                print(f"YOU WIN! 🥳 {winner} won the race.")
            else:
                print(f"You lose. 😒 {winner} won the race")
        else:
            distance = random.randint(1, 5)
            turtle.forward(distance)

screen.exitonclick()

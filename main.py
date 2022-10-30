from turtle import Screen
from turtleguy import Turtleguy
from cars import Car
from scorekeeper import Scorekeeper
import time

TURTLE_SPEED = 15
car_speed = 3

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("white")
screen.tracer(0)

turtle = Turtleguy(TURTLE_SPEED)
scorekeeper = Scorekeeper()

screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")
screen.onkey(turtle.move_right, "Right")
screen.onkey(turtle.move_left, "Left")

game_on = True
spawn_countdown = 10
car_list = []
scorekeeper.display()
while game_on:
    time.sleep(0.1)
    screen.update()
    spawn_countdown -= 1
    if spawn_countdown == 0:
        car = Car(car_speed)
        car_list.append(car)
        if scorekeeper.level < 10:
            spawn_countdown = 10 - scorekeeper.level
        else:
            spawn_countdown = 1
    for car in car_list:
        car.move()
        if car.distance(turtle) < 15:
            game_on = False
            scorekeeper.game_over()
        if car.xcor() < -320:
            car_list.remove(car)
    if turtle.ycor() > 295:
        scorekeeper.level += 1
        scorekeeper.display()
        turtle.reset()
        car_speed = car_speed * 1.2
    print(len(car_list))


screen.exitonclick()




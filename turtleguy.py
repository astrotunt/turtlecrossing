from turtle import Turtle

class Turtleguy(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(0, -280)
        self.setheading(90)
        self.speed = speed

    def move_up(self):
        self.setheading(90)
        self.forward(self.speed)

    def move_down(self):
        if self.ycor() > -290:
            self.setheading(270)
            self.forward(self.speed)

    def move_right(self):
        if self.xcor() < 290:
            self.setheading(0)
            self.forward(self.speed)

    def move_left(self):
        if self.xcor() > -290:
            self.setheading(180)
            self.forward(self.speed)

    def reset(self):
        self.setposition(0, -280)
        self.setheading(90)

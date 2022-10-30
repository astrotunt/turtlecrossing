from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.penup()
        self.setposition(310, random.randint(-250, 250))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color_choices = ["red", "blue", "green", "yellow", "orange", "purple"]
        self.color(random.choice(self.color_choices))
        self.speed = speed
        print("Car spawned")

    def move(self):
        self.goto(self.xcor() - self.speed, self.ycor())

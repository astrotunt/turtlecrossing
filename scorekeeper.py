from turtle import Turtle

class Scorekeeper(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-280, 280)
        self.level = 1

    def display(self):
        self.clear()
        self.write(f"Level:{self.level}", font=("Arial", 10, "bold"))

    def game_over(self):
        self.goto(-40, 0)
        self.write("SQUISHED", font=("Arial", 14, "bold"))
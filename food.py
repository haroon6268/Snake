from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))
    def clear(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))


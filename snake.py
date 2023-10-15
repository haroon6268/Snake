import random
from turtle import Turtle, Screen

MOVEMENT = 10
import time

screen = Screen()
colors = ["blue", "black"]


class Snake:
    def __init__(self):
        super().__init__()
        self.head = Turtle()
        self.head.goto(0, 0)
        self.all_snake = []
        self.head.color("blue")
        self.head.shape("square")
        self.head.penup()
        self.coords = [(-20, 0), (-40, 0)]
        for coord in self.coords:
            self.create_snake()
            self.snake.goto(coord)

    def create_snake(self):
        self.snake = Turtle()
        self.snake.color(random.choice(colors))
        self.snake.shape("square")
        self.snake.penup()
        self.all_snake.append(self.snake)

    def movement(self):
        x, y = self.head.xcor(), self.head.ycor()
        self.head.forward(10)
        for snake in range(len(self.all_snake) - 1, 0, -1):
            new_x, new_y = self.all_snake[snake - 1].xcor(), self.all_snake[snake - 1].ycor()
            self.all_snake[snake].goto(new_x, new_y)
        self.all_snake[0].goto(x, y)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def create_n_snake(self):
        self.snake = Turtle()
        self.snake.color(random.choice(colors))
        self.snake.shape("square")
        self.snake.penup()
        self.all_snake.append(self.snake)
        x = self.all_snake[-1].xcor()
        y = self.all_snake[-1].ycor()
        self.snake.goto(x, y)

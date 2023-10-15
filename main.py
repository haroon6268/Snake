from turtle import Screen
from snake import Snake
from time import *
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("green")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_down, "s")

food = Food()
score = Score()
screen.update()



while True:
    screen.update()
    sleep(0.1)
    snake.movement()

    if snake.head.distance(food) < 15:
        food.clear()
        snake.create_n_snake()
        score.add_score()
        score.update_score()

    if snake.head.ycor() < -270:
        score.high_score()
        score.update_score()
    elif snake.head.xcor() < -270:
        score.high_score()
        score.update_score()
    elif snake.head.ycor() > 270:
        score.high_score()
        score.update_score()
    elif snake.head.xcor() > 270:
        score.high_score()
        score.update_score()





screen.exitonclick()
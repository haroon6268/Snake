from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.goto(0, 270)
        self.write(f"Score:{self.score} Highscore:{self.highscore}", align="center", font=("arial", 28, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.highscore}", align="center", font=("arial", 28, "normal"))

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.highscore}")

    def add_score(self):
        self.score += 1

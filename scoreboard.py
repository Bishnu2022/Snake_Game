from turtle import Turtle
from snake_food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f"score : {self.score}", align="center", font=("times new roman", 20, "normal"))

    def Game_Over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("times new roman", 20, "normal"))

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.scoreboard_update()

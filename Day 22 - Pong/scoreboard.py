from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.x = x
        self.goto(self.x, 180)
        self.write(f"{self.score}", align="center", font=("Courier", 30, "bold"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.penup()
        self.goto(self.x, 180)
        self.write(f"{self.score}", align="center", font=("Courier", 30, "bold"))

    def game_over(self, message=str):
        self.goto(0,0)
        self.write(message, align="center", font=("Courier", 30, "bold"))

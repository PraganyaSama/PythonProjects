from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "bold"))
        self.hideturtle()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

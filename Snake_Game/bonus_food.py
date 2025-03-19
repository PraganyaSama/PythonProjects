from turtle import Turtle
import random
import time


class BonusFood(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(1000, 1000)

    def create_food(self):
        a = random.randint(1, 5)
        if a == 5:
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            self.goto(random_x, random_y)

    def remove_food(self):
        self.goto(1000, 1000)

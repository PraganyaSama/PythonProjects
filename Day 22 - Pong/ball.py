from turtle import Turtle
import random

sign_x = random.choice([1, -1])
sign_y = random.choice([1, -1])


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.x = 3
        self.y = 3
        self.move_speed = 0.005

    def move(self, x=10, y=10):
        new_x = self.xcor() + self.x * sign_x
        new_y = self.ycor() + self.y * sign_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        # self.move_speed *= 0.9

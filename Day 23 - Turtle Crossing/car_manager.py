from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.probability = 6
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, self.probability)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.setheading(180)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_level(self):
        self.speed += MOVE_INCREMENT
        self.probability -= 1

from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
screen = Screen()


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Adds a new turtle
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.turtles.append(new_segment)

    def extend(self):
        # Extends the snake when it eats food by adding turtle segments
        self.add_segment(self.turtles[-1].position())

    def move(self):
        position = 0
        for i in range(len(self.turtles)):
            if i == 0:
                position = self.turtles[i].pos()
                self.turtles[i].forward(MOVING_DISTANCE)
            else:
                a = self.turtles[i].pos()
                self.turtles[i].goto(*position)
                position = a

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def reset(self):
        for turtles in self.turtles:
            turtles.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()

    def slither(self):
        screen.listen()
        screen.onkey(key="Left", fun=self.left)
        screen.onkey(key="Right", fun=self.right)
        screen.onkey(key="Up", fun=self.up)
        screen.onkey(key="Down", fun=self.down)

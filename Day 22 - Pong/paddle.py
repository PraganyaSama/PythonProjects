from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.start = starting_position
        self.shape("square")
        self.turtlesize(stretch_len=3)
        self.penup()
        self.color("white")
        self.goto(*self.start)
        self.setheading(90)

    def move(self, distance):
        self.forward(distance)

    def up(self):
        # Makes the paddle move up
        if self.heading() == 90:
            pass
        else:
            self.setheading(90)
        if 185 > self.ycor():
            self.move(50)

    def down(self):
        # Makes the paddle move down
        if self.heading() == 270:
            pass
        else:
            self.setheading(270)
        if self.ycor() > -180:
            self.move(50)

    def movement_player(self, key1, key2):
        # This integrates keypress, up, down, to make the paddle move
        screen.listen()
        screen.onkeypress(key=key1, fun=self.up)
        screen.onkeypress(key=key2, fun=self.down)

    def movement_computer(self):
        # Gives the computer's paddle a periodic movement.
        if 185 > self.ycor() > -180:
            self.move(10)
        elif self.ycor() > 185:
            self.setheading(270)
            if self.ycor() > -180:
                self.move(10)
        elif self.ycor() < -180:
            self.setheading(90)
            if self.ycor() < 185:
                self.move(10)
        else:
            self.move(10)

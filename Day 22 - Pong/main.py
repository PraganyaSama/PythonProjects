from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

STARTING_POSITION_PLAYER = (-490, 0)
STARTING_POSITION_COMPUTER = (480, 0)

screen = Screen()

screen.setup(width=1000, height=450)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_player = Paddle(STARTING_POSITION_PLAYER)
paddle_computer = Paddle(STARTING_POSITION_COMPUTER)
ball = Ball()
scoreboard_player = Scoreboard(-100)
scoreboard_opponent = Scoreboard(100)
screen.update()

game = True
while game:
    screen.update()
    time.sleep(ball.move_speed)
    paddle_player.movement_player("w", "s")
    # paddle_computer.movement_computer()
    paddle_computer.movement_player("Up", "Down")
    ball.move()
    if ball.ycor() > 215 or ball.ycor() < -215:
        ball.bounce_y()
    if ball.distance(paddle_player) < 37 and ball.xcor() < -480 or paddle_computer.distance(
            ball) < 37 and ball.xcor() > 480:
        ball.bounce_x()
    if ball.xcor() > 500:
        scoreboard_player.increase_score()
        ball.goto(0,0)
    elif ball.xcor() < -500:
        scoreboard_opponent.increase_score()
        ball.goto(0,0)
    if scoreboard_player.score == 10:
        scoreboard_player.game_over("YOU WIN")
        game = False
    elif scoreboard_opponent.score == 10:
        scoreboard_opponent.game_over("YOU LOSE")
        game = False

screen.exitonclick()

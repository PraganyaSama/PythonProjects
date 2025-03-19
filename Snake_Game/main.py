from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from bonus_food import BonusFood

screen = Screen()
screen.tracer(0)
snake = Snake()
food = Food()
bonus_food = BonusFood()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.slither()
    if snake.turtles[0].distance(food) < 15:
        food.new_food()
        bonus_food.create_food()
        snake.extend()
        score.increase_score(point=1)
    if snake.turtles[0].distance(bonus_food) < 25:
        score.increase_score(10)
        bonus_food.remove_food()
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or \
            snake.turtles[0].ycor() < -280:
        snake.reset()
        score.reset_highscore()
        user_input = screen.textinput(title="What do you want to do?", prompt="Enter: Play again, 0: exit")
        if user_input == "0":
            game = False
            score.game_over()
        else:
            continue
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            snake.reset()
            score.reset_highscore()
            user_input = screen.textinput(title="What do you want to do?", prompt="Enter: Play again, 0: exit")
            if user_input == "0":
                game = False
                score.game_over()
            else:
                continue

screen.exitonclick()

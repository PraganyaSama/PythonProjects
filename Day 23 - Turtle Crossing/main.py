import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from level import Level

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Level()
car_manager = CarManager()
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    if player.ycor() > 280:
        player.level_up()
        car_manager.increase_level()
        level.increase_level()
    for car in car_manager.cars:
        if player.distance(car) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()

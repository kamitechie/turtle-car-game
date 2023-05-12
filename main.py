import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_1 = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.move, "Up")

game_is_on = True
tracking_number = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if tracking_number % 6 == 0:
        cars.create_cars()
    cars.drive()
    tracking_number += 1

    # check if turtle collides with car
    for car in cars.all_cars:
        if player_1.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    # checks reaching the end
    if player_1.is_there_finnish():
        player_1.restart_position()
        cars.level_up()
        scoreboard.new_board()

screen.exitonclick()

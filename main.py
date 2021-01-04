import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create new player from player class
player = Player()
car_manager = CarManager()
# we need to listen to key strokes on screen
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # while the game is on, we will create a car every 0.1 seconds
    car_manager.create_car()
    # we will also move the car
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False

    # detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()

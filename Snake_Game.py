from turtle import Screen
import time
from snake_body import Snake
from snake_food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_scoreboard()
        snake.extend()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.Game_Over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.Game_Over()

screen.exitonclick()

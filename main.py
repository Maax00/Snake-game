
from scoreboard import Score_Board
from food import Food
from snake import Snake
from turtle import Screen
import time

GAME_BORDER_Y = 300
GAME_BORDER_X = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")
Borders_x = []
Borders_y = []
score = Score_Board()

on = True
while on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        snake.add_body()
        food.refresh()
        score.clear()
        score.add_point()

    if abs(snake.head.xcor()) >= GAME_BORDER_Y or abs(snake.head.ycor()) >= GAME_BORDER_X:
        score.new_game()
        snake.new_snake()
        #on = False

    for position in snake.snake_body[1:]:
        if snake.head.distance(position) < 15:
            score.new_game()
            snake.new_snake()
            #on = False
screen.exitonclick()

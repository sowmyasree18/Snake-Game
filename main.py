from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import winsound

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

tim = Turtle()
tim.color("white")
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        winsound.PlaySound("sounds/eating.wav", winsound.SND_ASYNC)

    # Detect collision with wall
    if snake.head.xcor() > 279 or snake.head.xcor() < -279 or snake.head.ycor() > 259 or snake.head.ycor() < -279:
        winsound.PlaySound("sounds/out.wav", winsound.SND_ALIAS)
        time.sleep(1)
        scoreboard.reset()
        snake.delete_snake()
        screen.update()
        tim.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        winsound.PlaySound("sounds/gameover.wav", winsound.SND_ASYNC)
        time.sleep(2)
        tim.clear()
        for count in range(5, -1, -1):
            tim.write(f"Game will restart in {count}sec...", align=ALIGNMENT, font=FONT)
            time.sleep(1)
            tim.clear()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            winsound.PlaySound("sounds/out.wav", winsound.SND_ALIAS)
            time.sleep(1)
            scoreboard.reset()
            snake.delete_snake()
            screen.update()
            tim.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
            winsound.PlaySound("sounds/gameover.wav", winsound.SND_ASYNC)
            time.sleep(2)
            tim.clear()
            for count in range(5, -1, -1):
                tim.write(f"Game will restart in {count}sec...", align=ALIGNMENT, font=FONT)
                time.sleep(1)
                tim.clear()
            snake.reset()

screen.exitonclick()

# Import required modules for game implementation
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create and setup a screen for game
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong with Python")
screen.bgcolor("black")
screen.tracer(0)

# Create paddles, ball, and score board to display
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Setup the screen events when the keys are pressed
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# Start the game
game_is_on = True
# While the game is running
while game_is_on:
    # Make the screen animated
    time.sleep(ball.move_speed)
    screen.update()

    # Move the ball
    ball.move()

    # Detection with upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Change the y-axis of the ball
        ball.bounce_y()

    # Detection with the paddles
    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        # Change the x-axis of the ball
        ball.bounce_x()

    # Detect the right paddle miss
    if ball.xcor() > 380:
        # Give the point to the left player
        scoreboard.l_point()
        # reset the ball's position
        ball.reset_position()

    # Detect the left paddle miss
    if ball.xcor() < -380:
        # Give the point to the right player
        scoreboard.r_point()
        # reset the ball's position
        ball.reset_position()

# Exit the screen on click
screen.exitonclick()

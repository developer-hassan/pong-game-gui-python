# Import turtle module for its functionality
from turtle import Turtle


class Ball(Turtle):
    """
    Responsible for creating a ball on screen that moves on the screen.
    """

    def __init__(self):
        super().__init__()
        # Creates a Ball with specific properties and behaviors
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Updates the x and y position of the ball and position the ball there.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the y-position of the ball.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverses the x-position of the ball.
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Moves the ball back to origin and change its direction of moving. Resets the move speed of ball.
        """
        self.bounce_x()
        self.goto(0, 0)
        self.move_speed = 0.1

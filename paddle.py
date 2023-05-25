# Import turtle module for its functionality
from turtle import Turtle


class Paddle(Turtle):
    """
    Responsible for generating the paddles to move up and down on the screen.
    """

    def __init__(self, position):
        super().__init__()
        # Create a paddle with specific properties and behaviors
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def go_up(self):
        """
        Moves the paddle up 20 paces.
        """
        # set the new y-coordinate by incrementing the previous y-coordinate by 20 paces
        new_y = self.ycor() + 20
        # Set the new position of paddle
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the paddle down 20 paces.
        """
        # set the new y-coordinate by decrementing the previous y-coordinate by 20 paces
        new_y = self.ycor() - 20
        # Set the new position of paddle
        self.goto(self.xcor(), new_y)
